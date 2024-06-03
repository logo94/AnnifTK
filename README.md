[![it](https://img.shields.io/badge/lang-it-blue.svg)](https://github.com/logo94/excel2text-key/blob/main/README.md)
![](https://img.shields.io/badge/Python-3.8%2B-green.svg)

# AnnifTK
Python script a supporto della preparazione di corpora di addestramento per il software Annif

<p align="center">
  <img src="https://github.com/logo94/AnnifTK/blob/main/data/AnnifTK_screen.png" />
</p>

## Requisiti ##
Per l'utilizzo degli scripts è necessario aver scaricato `Python 3.8+` sul proprio dispositivo, per installare Python seguire le istruzioni riportate al seguente [link](https://www.python.org/downloads/).

Una volta eseguito il download è possibile verificare le versioni di `Python` e `pip` tramite i comandi:

```
python --version
```
```
pip --version
```

## Installazione ##
Per scaricare l'applicazione localmente premere il tasto verde 'Code' in alto a destra e scegliere il sistema di download preferito, nel caso non si conoscano le opzioni elencate, premere sul tasto 'Download ZIP':

<p align="center">
  <img src="https://github.com/logo94/catabot/blob/main/img/catabot-download.png" />
</p>

Una volta scaricato il file, decomprimerlo ed entrare nella cartella risultante

## Ambiente virtuale ##
Per non compromettere l'installazione di Python e le relative librerie è consigliabile creare un ambiente virtuale; per la sua creazione, una volta dentro la cartella dell'applicazione, procedere come segue:

Aprire il terminale all'interno della cartella (premere il tasto destro del mouse all'interno di uno spazio vuoto della cartella e selezionare l'opzione Apri nel Terminale)

Creare l'ambiente virtuale, quindi digitare:
```
python -m venv pyenv
```
oppure, in caso di errore:
```
python3 -m venv pyenv
```

### Linux
Per attivare l'ambiente virtuale con un sistema operativo Linux digitare:
```
source pyenv/bin/activate
```
### Windows
L'attivazione dell'ambiente virtuale su sistema operativo Windows richiede i privilegi di Amministratore di sistema, è quindi necessario aprire il Terminale o Windows PowerShell come amministratore. Una volta eseguita la procedura sopra riportata digitare:
```
pyenv\Scripts\activate
```

>Nel caso in cui non ci sia la possibilità di ottenere i privilegi di amministratore questo passaggio può essere saltato in modo che sia utilizzato l'ambiente virtuale Python di sistema.

## Librerie ##
Per il suo funzionamento Catabot utilizza una serie di librerie esterne, per il corretto funzionamento dell'applicazione è necessario procedere con il download di tutti i pacchetti necessari, ovvero:

```
pip install -r requirements.txt
```
### Windows
Per l'installazione delle librerie è necessario disporre dei perivilegi di amministratore di sistema, in alternativa è possibile avviare l'installazione senza privilegi specifici attraverso il comando:
```
pip install -r requirements.txt --user
```
> Eventuali messaggi di Warning durante l'installazione potranno essere ignorati



## Utilizzo ##
Una volta scaricato il repository e scaricate le librerie necessarie, per avviare l'applicazione sarà sufficiente eseguire il comando:
```
python anniftk.py [options]
```
oppure:
```
python3 anniftk.py [options]
```

### Comandi ###
