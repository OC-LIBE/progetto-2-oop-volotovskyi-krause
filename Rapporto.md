# 08.01.2025
Abbiamo deciso di programmare il gioco BlackJack.


# 15.01.2025
Abbiamo deciso di dividere il lavoro in modo che uno fa le funzioni e l'altro fa la grafica.
Per la grafica vogliamo fare in modo che le carte del giocatore e della banca sono in mezzo allo schermo.
Abbiamo provato a fare una funzione per distribuire le carte.

# 17.01.2025
Sono state aggiunte diverse funzioni('Hit', calcolare punti, etc.) che pero non funzionano come dovrebbero perché le carte continuano a mischiarsi. Ho provato a cambiare
le funzioni nel Deck ma quello ha pure peggiorato la situazione. Alla fine sono arrivato alla conclusione che il deck deve essere in qualche
salvato in qualche modo. Per ora sto cercando le soluzioni.

# 22.01.2025
Con l'aiuto del metodo session_state siamo riusciti a salvare il mazzo. Rimane comunque il problema che le carte vengono prese saltando una.

# 27.01.2025
Sono riuscito a mettere apposto la funzione 'Hit' che aggiunge nel mazzo le carte ogni volta che si schiaccia il buttone. Ci ho anche provato 
a fare la classe del Dealer che eredita la classe Player. Per ora non funziona come vogliamo ma le basi ci sono

# 28.01.2025
Sono riuscito a riparare la classe Dealer cosi che il mazzo non va in conflitto con quello del Player. Ho anche aggiunto la funzione
'take card' che riempie il mazzo del Dealer delle carte se non ce ne sono abbastanza. Per ora non funziona come dovrebbe. Il lavoro è in progresso.

# 29.01.2025
Abbiamo finito la funzione "stand" che aggiunge le carte mancanti carta al dealer quando il giocatore ha finito di prendere le sue carte.
Abbiamo anche fatto la classe Game e la funzione result che è responsabile dei risultati del gioco quando si devono confrontare gli score
degli giocatori. Abbiamo anche aggiunto il metodo 'New Game' che pulisce il cache e fa ripartire il gioco.

# 05.02.2025
Ho aggiunto il codice che gira la seconda carta del dealer e dopo aver cliccato 'Stand' la rigira. In sviluppo è anche la separazione del codice in due parti: back e front. È anche stata aggiunta la carta 0C che non esiste nel gioco ma reale ma qui rappresenta la parte dietro della carta che viene usata per girare la seconda carta del dealer.

# 12.02.2025 - 13.02.2025
Alla fine abbiamo deciso di non separare il codice in 2 parti perchè non ci dava tanti vantaggi. Abbiamo aggiunto anche la funzione che ci permette di fare il background del sito. Ho anche aggiunto la nuova classe User che controlla i soldi che vince il giocatore. In questo momento puo funzionare ma non ha tanto senso perché ogni volta che viene pulito il cache il balance ritorna al valore iniziale.

# 19.02.2025
Ho aggiunto 3 nuovi file: login, sign_up e navigation, cosi creando un sistema login. Ora il programma partisce dal file login. Dopo che l'utente entra nel nostro sistema riesce a giocare, per ora senza le puntate. Se l'utente non ha un account puo semplicemente crearselo tramite pagina sign_up. I dati forniti vengono caricati nel file accounts che contiene i dizionari con i dati degli utenti. Per ora il username non viene collegato al gioco e il sistema sign out non funziona come dovrebbe ma questi problemi verrano risolti.

# 26.02.2025

Abbiamo aggioranto il sistema login. Ora l'uetnte riceve al suo username anche un valore iniziale di 2000$ che viene salvato nel file balance come il dizionario. Abbiamo applicato questo sistema al gioco e funziona, solo che il balance viene sempre aggiornato quando si pulisce il session stateю

# 12.03.2025

Abbiamo risolto il problema con il balance che si aggiornava facendo username rimanere nel session state. Adesso il gioco è completamente funzionante.

# 01.04.2025

Ho fixato i bug con il sistema log out e ho anche pulito il codice.

# 02.04.2025

Ho cambiato un po' la user interface.