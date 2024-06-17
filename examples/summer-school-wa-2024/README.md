Elenco comandi:


1. Analisi preliminaer e selezione sito

Visualizzazione file HTML

```
Tasto destro --> Ispeziona
```
oppure
```
CTRL + U
```


2. Raccolta link

Download Catabot: https://github.com/logo94/Catabot?tab=readme-ov-file#installazione 

Attivazione ambiente virtuale


Linux
```
source pyenv/bin/activate
```

Windows
```
pyenv\Scripts\activate
```

Selezione TAB `Links`
Selezione TAB `URL progressivo`

Inizio URL --> https://aibnotizie.aib.it/page/
Da         --> 1
A          --> 45
Fine URL   --> /

Checkbox `Pagina singola`
Checkbox `Tutti i link`

Selezione `Salva CSV`


3. Raccolta metadati descrittivi

Selezione TAB `HTML`

URL pagina di prova --> https://aibnotizie.aib.it/archivi-in-biblioteca-lofferta-formativa-in-presenza-di-aib-lombardia-ospitata-in-un-luogo-di-fascino/ 

Title | h1 | class | entry-title
Date | time
Description | div | class | entry-content
Subject | div | class | tags

Selezione `Test`

Selezione `Carica CSV`

Selezione `Salva CSV`


6. Conversione corpus di addestramento e vocabolario

Download AnnifTK: https://github.com/logo94/AnnifTK/wiki#download 

Attivazione ambiente virtuale

```
python3 anniftk.py -i -v
```


7. Creazione file projects.cfg

[xxx] - identificativo univoco del progetto  
name - nome del singolo progetto
language - lingua del progetto (ISO 639-2)
backend - algoritmo
analyzer - tokenizzatore
vocab - ID vocabolario di riferimento
cluster_balanced - tipologia blanciamento cluster (parametro già ottimizzato)
cluster_k - numero di cluster (parametro già ottimizzato)
max_depth - profondità cluster (parametro già ottimizzato)

Il file `projects.cfg` va collocato all'interno della cartella in cui è stato scaricato, e in cui viene lanciato, Annif


8. Addestramento algoritmi

Attivazione ambiente virtuale

```
pip install annif
```
```
pip install annif[omikuji]
```

Per verificare il corretto caricamento del progetto digitare:
```
annif list-projects
```

Caricamento vocabolario:
```
annif load-vocab aibnotizie data/aibnotizie_voc_it.csv
```

Training algoritmi
```
annif train sswa-multi data/corpus/
```

> In caso di primo scaricamento verrà richiesto di scaricare punkt, per procedere con l'installazione digitare:


```
python3
```

```
> import punkt
```
```
punkt.download('punkt')
```


9. Esposizione API Annif

```
annif run
```

Aprire il browser e digitare l'URL: `127.0.0.1:5000`
