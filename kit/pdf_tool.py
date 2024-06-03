import os
from tqdm import tqdm
from PyPDF2 import PdfReader

def read_pdf(folderpath):
    file_list = os.listdir(folderpath)
    
    for file in tqdm(file_list, total=len(file_list), desc='Conversione .txt:', bar_format='{l_bar}{bar} {n_fmt}/{total_fmt}'):
        try:
            if str(file).endswith('.pdf'):
                
                reader = PdfReader(folderpath + "/" + file)
                pp = len(reader.pages)

                txt_file = folderpath + "/" + file.split(".")[0] + ".txt"
                with open(txt_file, 'w+', encoding='utf-8', newline='') as tf:
                    for p in range(1, pp):
                        page = reader.pages[p]
                        text = page.extract_text().replace("-\n", "").replace("a`", "à ").replace("`a", "à ").replace("e`", "è ").replace("`e", "è ").replace("e´", "é ").replace("i`u", "iù ").replace("i`", "ì ").replace("`i", "ì ").replace("o`", "ò ").replace("`o", "ò ").replace("u`", "ù ").replace("`u", "ù ")
                        tf.write(text)
            else: continue
        except: continue
    
    return