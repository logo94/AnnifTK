import os
from csv import reader
from tqdm import tqdm
from kit.pytools import create_folder, write_txt, write_key, convert_keys, vocab_append

def check_header(row: list[str]):
    if (row[0] == 'ID' and row[1] == 'Text' and row[2] == 'Key'): 
        return True
    else: 
        return False

def read_csv(filepath: str):
    try:
        num_lines = sum(1 for line in open(filepath, 'r'))
        vocab_array = []
        with open(filepath, 'r', encoding='utf-8') as csv_file:
            read = reader(csv_file)
            header = next(read)
            if not check_header(header):
                print('Errore: intestazione file CSV non conforme')
                raise
            else:
                foldername = create_folder(filepath)

                for line in tqdm(read, total=num_lines, desc='Conversione .txt/.key:', bar_format='{l_bar}{bar} {n_fmt}/{total_fmt}'):
                    
                    filename = str(line[0]).strip()
                    text = str(line[1])
                    keys = convert_keys(str(line[2]))
                               
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

def vocab_csv(filepath: str):
    try:
        num_lines = sum(1 for line in open(filepath, 'r'))
        vocab_array = []
        with open(filepath, 'r', encoding='utf-8') as csv_file:
            read = reader(csv_file)
            header = next(read)
            if not check_header(header):
                print('Errore: intestazione file CSV non conforme')
                raise
            else:
                for line in read:
                    keys = convert_keys(str(line[2]))
                    vocab_array = vocab_append(vocab_array, keys)                          
            return vocab_array
                    
    except:
        raise Exception()

        
    
