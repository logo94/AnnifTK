[![it](https://img.shields.io/badge/lang-it-blue.svg)](https://github.com/logo94/excel2text-key/blob/main/README.md)
![](https://img.shields.io/badge/Python-3.8%2B-green.svg)

# AnnifTK
Python script a supporto della preparazione di corpora di addestramento per il software Annif

<p align="center">
  <img src="https://github.com/logo94/AnnifTK/blob/main/examples/img/AnnifTK_screen.png" />
</p>

Annif Toolkit mette a disposizione i seguenti servizi:
- conversione di file dal formato `.csv`, `.xlsx`, `.json` a coppie di file `.txt` e `.key` compatibili con il software Annif: dato un file d'ingresso con intestazione fissa, AnnifTK esegue in automatico la conversione di ogni riga creando in una cartella omonima al file processato coppie di file contenenti testo e relativi tag semantici.
- conversione di file dal formato `.pdf` al formato `.txt`: data una cartella di ingresso, per ogni file contenuto nella cartella viene creato un nuovo file con lo stesso nome ma con estensione `.txt`.
- creazione di un file vocabolario in un formato compatibile con Annif. Dato un file di ingresso, da ogni riga vengono estratti i tag semantici (Colonna `Key`), vengono cercati gli URI in Wikidata e le coppie di URI / etichetta vengono salvati in un file `.csv` già predisposto per il caricamento in Annif.

> Per ogni tag semantico viene cercato l'URI di Wikidata, se il termine ottiene un match l'URI viene riportato cosi com'è, nel caso invece in cui il tag sia soggetto ad ambiguità verrà riportato l'URI candidato preceduto da un `[!]` per la disambiguazione manuale


## Installazione ##
> Per le istruzioni di installazione consultare la sezione [wiki](https://github.com/logo94/AnnifTK/wiki)


## Utilizzo ##
Per il suo funzionamento AnnifTK richiede la preparazione di un file di ingresso strutturato nel seguente modo:

### CSV, Excel ###
Per essere letto e convertito correttamente un file in formato CSV o XLSX deve riportare il seguente header e la seguente struttura:


| ID | Text | Key
| --- | --- | ---
| xxx | xxx | xxx


### JSON ###
Per essere letto e convertito correttamente un file in formato JSON deve essere strutturato come un array di oggetti, quindi:

```
[
    {
        "ID": "xxx",
        "Text": "xxx",
        "Key": "xxx; xxx; xxx"
    }
]

```
In cui:

**ID**: I valori contenuti nella colonna `ID` verranno utilizzati per nominare le coppie di file .txt e .key, i valori ID devono essere univoci all'interno del file

**Text**: I valori contenuti nella colonna `Text` verranno convertiti in file .txt contenenti il testo da utilizzare per l'addestramento

**Key**: I valori contenuti nella colonna `Key` verranno convertiti in file .key contenenti i tag semantici associati al testo. 

Nel caso in cui il campo Key contenga più di un'etichetta, i separatori validi sono `; `, ` - `, ` § ` 

> Per visualizzare degli esempi di file consultare la cartella [examples](https://github.com/logo94/AnnifTK/tree/main/examples)


## Conversione

Una volta preparato il file di input, scaricato il repository e scaricate le librerie necessarie, per avviare l'applicazione sarà sufficiente eseguire il comando:
```
python anniftk.py [options]
```
oppure:
```
python3 anniftk.py [options]
```

In cui [options] equivale ad uno o più comandi specifici

### Comandi ###
Per selezionare la modalità sostituire [options] con uno o più dei seguenti comandi:
| Comando | Descrizione |
| --- | --- |
| [-h] --help | Viene mostrato il messaggio di aiuto in cui sono riportati tutti i comandi e descrizioni |
| [-i]  --file | Selezione di un singolo file da processare tramite finestra di sistema (UI) |
| [-o] --folder | Selezione, tramite finestra di sistema (UI), di una cartella contente uno o più file PDF da convertire in formato TXT|
| [-c] --cli | Selezione di un file o di una cartella tramite riga di comanda, verrà richiesto l'inserimento di un full-path |
| [-v] --vocab | Selezione di un file da convertire in un file vocabolario in formato CSV, può essere utilizzato in combinazione ai comandi --file e --cli |
