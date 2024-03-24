import codecs
import csv
from typing import List
from fastapi import UploadFile
from openai import OpenAI

from config import Settings

settings = Settings()
client = OpenAI(api_key=settings.chatgpt_api_key)

messages = [{"role": "system", "content": "You will generate tags for a dataset. I will provide your the first 6 rows"
                                          "of the dataset, whereas the very first row will be the column titles of the dataset."
                                          "The first row will be in the following form: title1,title2,title3,etc..."
                                          "The next rows will be in the following form: value1,value2,value3,etc..."
                                          "Output 5-10 tags that describe the dataset best. Output only the suitable"
                                          "tags in the form of: tag1,tag2,tag3,etc..."}]

async def handle_tagging(file: UploadFile) -> List[str]:
    reader = csv.reader(codecs.iterdecode(file.file, "utf-8"))

    i = 0
    for row in reader:
        messages.append({"role": "user", "content": ",".join(row)})
        if i == 5:
            break

    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=messages)

    return response.split(",")