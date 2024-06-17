import os

def create_folder(filepath: str):
    try:
        folder_name = filepath.split("/")[-1].split(".")[0]
        folder_path = filepath.rsplit("/", 1)[0]
        folder = os.path.join(folder_path + "/", folder_name)
        os.mkdir(folder)
        return folder
    except:
        return False

def write_txt(txt_file: str, txt):
    try:
        with open(txt_file, 'w+', encoding='utf-8') as tf:
            tf.write(txt)
        return True
    except:
        return False

def key_clean(key: str):
    if key.__contains__(","):
        try:
            surname = key.split(", ")[0]
            name = key.split(", ")[1]
            key = name + " " + surname
        except:
            pass
    return key
        
def write_key(key_file: str, keys: list[str]):
    try:
        with open(key_file, 'w+', encoding='utf-8') as kf:
            for key in keys:
                kf.write(key_clean(key.strip()) + '\n')
        return True
    except:
        return False

def convert_keys(sbj: str):
    if ' - ' in sbj:
        keys = sbj.split(' - ')
    elif " – " in sbj:
        keys = sbj.split(" – ")
    elif " § " in sbj:
        keys = sbj.split(" § ")
    elif "; " in sbj:
        keys = sbj.split("; ")
    else: 
        keys = []
        keys.append(sbj)
    return keys

def vocab_append(vocs: list[str], keys: list[str]):
    for key in keys:
        key = key_clean(key)
        if key not in vocs:
            vocs.append(key)
    return vocs
