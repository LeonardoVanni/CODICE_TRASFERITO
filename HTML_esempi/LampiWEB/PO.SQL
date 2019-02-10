SELECT StatoLED, FileImmagine FROM LED WHERE Selettore == 1 

UPDATE LED SET Selettore = 0

UPDATE nome_tabella SET Selettore = 1 WHERE StatoLED = 1