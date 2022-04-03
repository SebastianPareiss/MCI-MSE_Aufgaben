# %% Import der nötigen Pakete
import numpy as np
import matplotlib.pyplot as plt

# Schleife um jede Person einspeichern zu können
# (auslesen und ploten)


# %% Öffnen der Datei und konvertieren zu numpy-Array

#for(i = 1; i <= 3; i++) Schreibweise in Python nicht bekannt 

#Schleife 3 mal durchlaufen weil 3 Daten gegeben sind 
for i in range (3):

 #Daten bei durchlauf um 1 erhöhen bis bei range(3) angekommen
 #string in python str
  
    d = str(i+1)

#+d+ um den string anzuwenden und die Diagramme der 3 verschiedenen Daten zu erhalten
    file_name =  'input_data/power_data_'+d+'.txt'  # Eleganter ist das verwenden von 'os' um die Namen nicht zu hard-coden (siehe letzte Übung)
    power_data_watts = open(file_name).read().split("\n")
    x = np.array(power_data_watts)

#Plot erstellen
    plt.title("Line graph")  # Hier kann der Name der Plots auch in der Schleife verändert werden
    plt.plot(x, color="red")
    plt.show()


# Bewertung: Solide Lösung die funktioniert! Kommentare in Zeilen 22 und 27 bitte nächstes mal beachten. 

# %%

# %%
