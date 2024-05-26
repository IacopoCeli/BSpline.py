 /$$$$$$$   /$$$$$$            /$$ /$$                    
| $$__  $$ /$$__  $$          | $$|__/                    
| $$  \ $$| $$  \__/  /$$$$$$ | $$ /$$ /$$$$$$$   /$$$$$$ 
| $$$$$$$ |  $$$$$$  /$$__  $$| $$| $$| $$__  $$ /$$__  $$
| $$__  $$ \____  $$| $$  \ $$| $$| $$| $$  \ $$| $$$$$$$$
| $$  \ $$ /$$  \ $$| $$  | $$| $$| $$| $$  | $$| $$_____/
| $$$$$$$/|  $$$$$$/| $$$$$$$/| $$| $$| $$  | $$|  $$$$$$$
|_______/  \______/ | $$____/ |__/|__/|__/  |__/ \_______/
                    | $$                                  
                    | $$                                  
                    |__/          

Il programma lavoro solo in due dimensioni e accetta in input:
  1. file .txt contenente i punti di controllo specificati per riga con cordinata x separata da coordinata y da un tab.
  2. file .txt contenente i knots.
Ritorna in output un file .txt contenente la curva ricostruita con le informazioni in input secondo l'algoritmo BSpline implementato nella libreria tinyspline.

Il programma è stato sviluppato per ottenere, senza dover necessariamente utilizzare Autocad, un insieme di punti che rappresentano delle figure piane da un file in formato DXF che contiene curve BSpline o Polyline. Il programma, oltre a ricostruire la figura, ne discretizza ogni punto secondo specifiche richieste in input. Tale esigenza si è resa necessaria poichè, le macchine a controllo numerico che tagliano fisicamente il pezzo, hanno delle specifiche tolleranze (dovute per esempio alla dimensione dell'utensile) che non consentono una distanza tra due punti troppo ravvicinata.
