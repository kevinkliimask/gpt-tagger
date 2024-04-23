import requests
import json
from collections import defaultdict


counts = defaultdict(lambda : 0)

def get_datasets_list():
    x = requests.get('https://avaandmed.eesti.ee/api/datasets?limit=1787')
    return json.loads(x.content)['data']


def get_dataset(uuid):
    x = requests.get(f'https://avaandmed.eesti.ee/api/datasets/{uuid}')
    return json.loads(x.content)['data']


if __name__ == '__main__':
    data = get_datasets_list()
    i = 0

    try:
        for obj in data:
            dataset = get_dataset(obj['id'])
            counts[len(dataset['keywords'])] += 1
            i += 1
    except:
        print(counts)

    print(counts)
