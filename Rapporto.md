# 08.01.2025
Abbiamo deciso di programmare il gioco BlackJack e di farlo in modo che più giocatori possano giocare allo stesso tempo.


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
