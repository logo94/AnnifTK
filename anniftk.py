#!/usr/bin/env python3
import os, sys
import argparse
import tkinter as tk
from tkinter import filedialog

from kit.csv_tool import read_csv, vocab_csv
from kit.excel_tool import read_excel, vocab_excel
from kit.pdf_tool import read_pdf
from kit.json_tool import read_json, vocab_json
from kit.vocab_tool import create_vocab

def process_file(path: str):
    try:
        if path.endswith('.csv'):
            vocab_array = read_csv(path)
        elif path.endswith('.xlsx'):
            vocab_array = read_excel(path)
        elif path.endswith('.pdf'):
            vocab_array = read_pdf(path)
        elif path.endswith('.json'):
            vocab_array = read_json(path)
        else:
            print('Errore: formato ' + path.split('/')[-1].split('.')[1] + ' non supportato')
        return vocab_array
    except:
        raise Exception()
    
def process_vocab(path: str):
    try:
        if path.endswith('.csv'):
            vocab_array = vocab_csv(path)
        elif path.endswith('.xlsx'):
            vocab_array = vocab_excel(path)
        elif path.endswith('.json'):
            vocab_array = vocab_json(path)
        else:
            print('Errore: formato ' + path.split('/')[-1].split('.')[1] + ' non supportato')
        return vocab_array
    except:
        raise Exception()

def main():

    root = tk.Tk()
    root.withdraw()

    parser = argparse.ArgumentParser(
        prog='anniftk.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Annif ToolKit, software a supporto della preparazione di corpora e vocabolari per l\'addestramento di Annif',
        #usage='%(prog)s [options]'
        )
    parser.add_argument('-i', '--file', action='store_true', help='Selezione di un singolo file per la conversione in coppie di file .txt/.key. Per selezionare più file utilizzare le opzioni --folder oppure --cli. Può essere utilizzato in combinazione con il parametro -v o --vocab per creare anche il file vocabolario')
    parser.add_argument('-o', '--folder', action='store_true', help='Selezione di una cartella contenente più file in formato PDF. Per ogni file verrà creato un file omonimo con estensione .txt')
    parser.add_argument('-c', '--cli', action='store_true', help='Selezione di file o cartelle tramite riga di comando, non richiede interfaccia grafica. Verrà richiesto di inserire il PATH a un file o a una cartella. Può essere utilizzato in combinazione al parametro -v o --vocab per creare anche il file vocabolario')
    parser.add_argument('-v', '--vocab', action='store_true', help='Selezione di un singolo file per la trasformazione in un file vocabolario compatibile con Annif. Partendo dai valori KEYS contenuti nel file di input, per ogni etichetta viene cercato l\'URI corrispettivo in Wikidata e salvato all\'interno del vocabolario *_voc_it.csv.  Può essere utilizzato in combinazione ai parametri --file o --cli')
    args = parser.parse_args()

    # Help
    if not args.file and not args.folder and not args.cli and not args.vocab:
        print('')
        logo = '''
          /\               (_)/ _| |__   __| |/ /
         /  \   _ __  _ __  _| |_     | |  | ' / 
        / /\ \ | '_ \| '_ \| |  _|    | |  |  <  
       / ____ \| | | | | | | | |      | |  | . \ 
      /_/    \_\_| |_|_| |_|_|_|      |_|  |_|\_\

'''
        print(logo)
        parser.print_help()
        print('')
        sys.exit()

    # -i | --file
    if args.file and not args.vocab and not args.folder and not args.cli:
        file = filedialog.askopenfilename(title = "Seleziona file",filetypes= (("Tutti i file","*.*"),("CSV","*.csv"),("Excel", "*.xlsx"),("JSON", "*.json")), multiple=False)
        try:
            process_file(file)
        except Exception as err:
            print(str(err))
            sys.exit()
    
    # -i -v | --file --vocab
    elif args.file and args.vocab and not args.folder and not args.cli:
        file = filedialog.askopenfilename(title = "Seleziona file",filetypes= (("Tutti i file","*.*"),("CSV","*.csv"),("Excel", "*.xlsx"),("JSON", "*.json")), multiple=False)
        try:
            vocab_array = process_file(file)
        except:
            print('Errore durante la conversione del file')
            sys.exit()
        try:
            create_vocab(file, vocab_array)
        except Exception as err:
            print('Errore durante la creazione del vocabolario')
            print(str(err))
            sys.exit()

    # -v | --vocab
    elif not args.file and args.vocab and not args.folder and not args.cli:
        file = filedialog.askopenfilename(title = "Seleziona file",filetypes= (("Tutti i file","*.*"),("CSV","*.csv"),("Excel", "*.xlsx"),("JSON", "*.json")), multiple=False)
        try:
            vocab_array = process_vocab(file)
        except:
            print('Errore durante la conversione del file')
            sys.exit()
        try:
            create_vocab(file, vocab_array)
        except:
            print('Errore durante la creazione del vocabolario')
            sys.exit()
    
    # -o | --folder
    elif args.folder and not args.file and not args.vocab and not args.cli:
        folder = filedialog.askdirectory()
        read_pdf(folder)
        
    # -c | --cli
    elif args.cli and not args.vocab and not args.file and not args.folder:
        path = input('Full-path: ')
        if '.' in path:
            try:
                process_file(path)
            except Exception as err:
                print(str(err))
                sys.exit()    
        else:
            read_pdf(path)
    
    # -c -v | --cli --vocab
    elif args.cli and args.vocab and not args.file and not args.folder:
        path = input('Full-path: ')
        if not '.' in path:
            print('Errore: il parametro --vocab richiede un file, non una cartella')
            sys.exit()
        else:
            try:
                vocab_array = process_vocab(path)
            except:
                print('Errore durante la conversione del file')
                sys.exit()
            try:
                create_vocab(path, vocab_array)
            except:
                print('Errore durante la creazione del vocabolario')
                sys.exit()
    
    # Controllo input
    else:
        print('Errore: combinazione di comandi non valida')
        sys.exit()

    return print('Operazione completata')


if __name__ == '__main__':
    main()
    
