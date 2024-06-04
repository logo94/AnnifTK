import os
import json
from tqdm import tqdm
from kit.pytools import create_folder, write_txt, write_key, convert_keys, vocab_append

def read_json(filepath: str):
    try:
        with open(filepath) as json_file:
            data = json.load(json_file)
        vocab_array = []
        foldername = create_folder(filepath)
        
        for item in tqdm(data, total=len(data), desc='Conversione .txt/.key:', bar_format='{l_bar}{bar} {n_fmt}/{total_fmt}'):
            try:
                filename = str(item['ID']).strip()
                text = str(item['Text'])
                keys = convert_keys(str(item['Key']))         
            except:
                print('Errore: campi file JSON non conformi')
                break
            
            txt_file = os.path.join(foldername, filename + '.txt')
            if write_txt(txt_file, text): pass
            else: 
                print('Errore: ' + filename + '  contiene un valore non valido')
                continue
            
            key_file = os.path.join(foldername, filename + ".key")
            if write_key(key_file, keys): pass
            else: print('Errore durante la scrittura di ' + filename + '.key')

            vocab_array = vocab_append(vocab_array, keys)

        return vocab_array
    
    except:
        raise Exception()
    
def vocab_json(filepath: str):
    try:
        with open(filepath) as json_file:
            data = json.load(json_file)
        vocab_array = []
        for item in data:
            try:
                filename = str(item['ID']).strip()
                text = str(item['Text'])
                keys = convert_keys(str(item['Key']))         
            except:
                print('Errore: campi file JSON non conformi')
                break
            vocab_array = vocab_append(vocab_array, keys)

        return vocab_array
    
    except:
        raise Exception()
