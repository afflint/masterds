### Master in Data Science, Economics, Business and Finance - AA 2023-24

## Progetti finali del corso di Programmazione in Python

### Proff. Marco Calautti e Alfio Ferrara

### 1. La risposta giusta

Lo scopo del progetto è creare automaticamente quiz a scelta multipla relativi ai film, sfruttando i dati di [IMDb](https://www.imdb.com/). Ogni quiz deve essere composto da una domanda e quattro possibili risposte, di cui solo una corretta. Il programma che genera i quiz deve inoltre implementare un criterio per generare le possibili risposte proporzionale alla difficoltà del quiz desiderato. Il programma deve inoltre consentire ad un giocatore umano di rispondere al quiz e deve misurare la sua prestazione con un punteggio complessivo che tenga conto della difficoltà di ogni singola domanda.
I dati IMDb possono essere acquisiti tramite API specifiche (come [Cinemagoer](https://cinemagoer.github.io)) o set di dati esistenti, come [IMDb Dataset](https://www.kaggle.com/datasets/ashirwadsangwan /imdb-dataset).

### 2. Board Games

Il sito web [BoardGameGeek (BGG)](https://boardgamegeek.com/) fornisce vari dati e statistiche sull'entusiasmante hobby dei giochi da tavolo. Gli utenti di BGG commentano i giochi e opzionalmente assegnano loro un punteggio di gradimento compreso tra 0 e 10.

Lo scopo del progetto è acquisire i voti assegnati ai giochi tramite le [API del sito](https://boardgamegeek.com/wiki/page/BGG_XML_API2) e produrre una classifica dei giochi in ordine di gradimento degli utenti. È bene precisare che per ottenere un ranking adeguato è necessario considerare non solo i voti, ma anche il fatto che a giochi diversi possono essere associati numeri molto diversi di commenti e quindi di voti da parte dei singoli utenti. Per una discussione su questo punto vedere, ad esempio, [How Not To Sort By Average Rating](https://www.evanmiller.org/how-not-to-sort-by-average-rating.html).

Il progetto dovrebbe proporre la propria strategia per l'ordinamento dei giochi, discutendone anche l'adeguatezza in relazione alla classifica ufficiale BGG, disponibile [online](https://boardgamegeek.com/browse/boardgame).

Il progetto dovrà inoltre produrre dei grafici che confrontino la classifica proposta con quella ottenuta unicamente attraverso la valutazione media di ogni partita, mostrando la diversa distribuzione dei punteggi e le differenze riscontrate.

### 3. Che tempo fa

Il [set di dati](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data?select=GlobalLandTemperaturesByMajorCity.csv) riporta la temperatura registrata nelle principali città del mondo a partire dal 1750. Utilizzando questo dati, il progetto dovrà fornire un’efficace visualizzazione grafica del cambiamento delle temperature nel tempo, evidenziando le città in cui sono state registrate le maggiori escursioni termiche durante i diversi periodi storici. Per la visualizzazione dei dati su una mappa, vedere [geopandas](https://geopandas.org/).

Il programma suggerirà inoltre, a seconda del periodo considerato, il percorso migliore da seguire per un viaggiatore che intende spostarsi da Pechino a Los Angeles spostandosi passo dopo passo verso la città più calda tra le 3 a lui più vicine.

### 4. Che animale è?

Il [set di dati](https://www.kaggle.com/uciml/zoo-animal-classification) fornisce dati su diverse specie animali per classificarle in 7 classi diverse, vale a dire mammiferi, uccelli, rettili, pesci, anfibi, insetti e invertebrati.
Seguendo un approccio non supervisionato, ovvero senza osservare la classe di ciascuna specie animale, il progetto dovrebbe mirare a confrontare le diverse specie e raggrupparle utilizzando diversi algoritmi di clustering.

Confrontando il risultato di ciascun algoritmo, mostra quale algoritmo di clustering approssima meglio le classi fornite dal set di dati.

È quindi necessario non solo definire una metodologia per confrontare i risultati del clustering con la classificazione prevista, ma anche descrivere brevemente le caratteristiche distintive di ciascun cluster di specie prodotto dall'algoritmo in esame.

### 5. Il giro del mondo in 80 giorni

Consideriamo il [dataset](http://island.ricerca.di.unimi.it/~alfio/shared/worldcities.xlsx) che descrive alcune delle principali città del mondo. Supponiamo che sia sempre possibile viaggiare da ciascuna città alle 3 città più vicine e che tale viaggio richieda 2 ore per la città più vicina, 4 ore per la seconda città più vicina e 8 ore per la terza città più vicina. Inoltre, il viaggio dura altre 2 ore se la città di destinazione si trova in un Paese diverso da quello di partenza e altre 2 ore se la città di destinazione ha più di 200.000 abitanti.

Partendo da Londra e viaggiando sempre verso est, è possibile fare il giro del mondo tornando a Londra in 80 giorni? Quanto tempo richiede almeno?

