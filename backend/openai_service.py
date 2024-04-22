import codecs
import csv
import re

from typing import Literal, List, TypedDict, Dict
from fastapi import UploadFile
from openai import OpenAI

import translator_service
from config import Settings

settings = Settings()
client = OpenAI(api_key=settings.chatgpt_api_key)


class TagsData(TypedDict):
    english: List[str]
    estonian: List[str]


async def handle_tagging(file: UploadFile, count: int) -> Dict[Literal["data"], TagsData]:
    reader = csv.reader(codecs.iterdecode(file.file, "utf-8"))

    messages = [{"role": "system", "content": "You will generate tags for a dataset. I will provide your the first rows"
                                              "of the dataset, whereas the very first row will be the column titles of the dataset."
                                              "The first row will be in the following form: title1,title2,title3,etc..."
                                              "The next rows will be in the following form: value1,value2,value3,etc..."
                                              f"Output {count} tags that describe the dataset best. Output only the "
                                              "suitable tags in the form of: tag1,tag2,tag3,etc... Tags should be in English"}]

    i = 0
    user_message = ""
    for row in reader:
        if i == 10:
            break
        user_message += (",".join(row) + "\n")
        i += 1
    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages)
    english_tags = re.split(r"\s?,\s?", response.choices[0].message.content)
    estonian_tags = translator_service.translate_text(english_tags, src="en", dest="et")

    return {"data": {"english": english_tags, "estonian": estonian_tags}}
