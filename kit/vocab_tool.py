import requests
from csv import writer
import json
from tqdm import tqdm

def wikidata_api(label):
    query = {
        "q0": {
            "query": label,
            "limit": 5,
            "type_strict": "should"
        }
    }
    http = requests.Session()
    payload = {'queries': json.dumps(query)}
    response = http.post('https://wikidata.reconci.link/it/api', data=payload).json()
    try:
        if len(response['q0']['result']) == 0:
            obj = {
                "uri": "",
                "label": label
            }   
        else:
            for candidate in response['q0']['result']:
                if candidate['match'] == True:
                    wikidata_id = "https://www.wikidata.org/wiki/" + candidate['id']
                    obj = {
                        "uri": wikidata_id if wikidata_id is not None else '',
                        "label": str(candidate['name'])
                    }
                    break
                else:  
                    if str(candidate['score']) == '100.0':
                        wikidata_id = "https://www.wikidata.org/wiki/" + candidate['id']
                        obj = {
                            "uri": '[!] ' + wikidata_id if wikidata_id is not None else '',
                            "label": label
                        }
                        break

        return obj   
    except:
        return {
            "uri": "",
            "label": label
        }

def create_vocab(filepath: str, keys: list[str]):
    try:
        filename = filepath.split('.')[0]
        vocab_file = filename + '_voc_it.csv'
        with open(vocab_file, 'w+', encoding='utf-8', newline='') as voc_file:
            voc = writer(voc_file)
            headerow = ['uri', 'label_it', 'notation']
            voc.writerow(headerow)
            for key in tqdm(keys, total=len(keys), desc='Creazione _voc_it:', bar_format='{l_bar}{bar} {n_fmt}/{total_fmt}'):
                row = []
                obj = wikidata_api(key)
                row.append(obj['uri'])
                row.append(obj['label'])
                voc.writerow(row)
    except:
        raise Exception()
