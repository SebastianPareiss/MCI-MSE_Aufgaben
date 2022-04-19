#%% UC 2.0

import os
from this import s
import pandas as pd
import neurokit2 as nk
import json
import numpy as np
import matplotlib.pyplot as plt

#%% UC 2.1 Einlesen der Daten

#gemäß neuer Angabe (04.04) wurden Funktionen erstellt, mit doc-strings markiert und kommentiert.
#es wurden weitere Funktionen hinzugefügt, allerdings kommt es vereinzelt zu Fehlermeldungen, da lokale Werte der einzelnen Funktionen nicht weiter gegeben werden
#es wurden die fehlerhaften Funktionen trotzdem mit doc-strings versehen, um absicht der Funktionen zu zeigen

folder_current = os.path.dirname(__file__) 
folder_input_data = os.path.join(folder_current, 'input_data')


def get_peaks(ekg):

    '''Funktion zum Finden der peaks und berechnen der average_HR und Speichern von Daten als Liste 
    
        parameters: 
            ekg_data(data_frame): values from the ecg-test

        returns:
            average_HR_10s(str): heart rate moving average

    '''
    #Find peaks 

    #Peaks aus Datensatz ermitteln, anschließend als Variable speichern
    peaks, info = nk.ecg_peaks(ekg, sampling_rate=1000)

    #Anzahl der Herzschläge 
    number_of_heartbeats = peaks["ECG_R_Peaks"].sum()

    #Testdauer in Minuten
    duration_test_min = ekg_data.size/1000/60

    #Durchschnittliche Herzfrequenz 
    average_hr_test = number_of_heartbeats / duration_test_min

    peaks['average_HR_10s'] = peaks.rolling(window=10000).mean()*60*1000

    #Rückgabe der Herzfrequenz 
    return peaks['average_HR_10s']


def plot_peaks (plotdata):

    ''' Funktion zum ploten der vorverarbeiteten Daten 

        parameters: 
            average_HR_10s(str): moving average 

        output: Data plot

    '''

    plotdata.plot()

    plt.show()


## Anlegen einer Zeitreihe dery Herzfrequenz aus den EKG-Daten

iterator = 1 #weiteres Aufzählen um alle subjects zeigen zu können 

for file in os.listdir(folder_input_data):
    
    #"Kontrolle" ob .csv-file
    if file.endswith(".csv"):  
        file_name = os.path.join(folder_input_data, file)
        subject_id = file_name.split(".")[0][-1]
        new_ecg_data = pd.read_csv(file_name)
        
        print(new_ecg_data) #zur Zwischenüberprüfung 

        #iterator um auf alle Subjects zugreifen zu können (als string)
        ekg_data = pd.DataFrame()
        ekg_data["ECG"] = new_ecg_data["Subject_"+ str(iterator)]

        average_hr = get_peaks(ekg_data["ECG"])

        #ploten der average_hr
        plot_peaks(average_hr)
        
        iterator += 1


#%% UC 2.2 Vorverarbeiten der Daten


## Use-Case 2.2 in Use-Case 2.1 zusammengelegt 

#%% UC 2.3 Analysieren der Daten auf Abbruch-Kriterium

termination = False


## Vergleich der Maximalen Herzfrequenz mit Alter des Patienten

def load_json(file):

    '''JSON Datei wird geöffnet => Rückgabe als dictionary  
    
    parameters: 
        file(json): json data

    returns:
        subject_data(str): data of subject (test person)
    '''

    folder_input_data = os.path.join(folder_current, 'input_data')
    file_name = folder_input_data = os.path.join(folder_input_data, file)
    f = open(file_name)
    # returns JSON object as
    # a dictionary
    subject_data = json.load(f)

    return subject_data

subject_data = load_json("subject_3.json")

def check_termination(subject_birth_year):

    '''Daten auf Abbruchkriterium (termination) geprüft  
    
        parameters: 
            file(json): json data

        returns:
            maximum_hr(str): maximum heart rate 
            subject_max_hr(str): maximum heart rate allowed 
    '''

    maximum_hr = peaks['average_HR_10s'].max()
    subject_max_hr = 220 - (2022 - subject_birth_year)

    if maximum_hr > subject_max_hr*0.90:
        termination = True

    return maximum_hr, subject_max_hr
    subject_max_hr, maximum_hr = check_termination(subject_data["birth_year"])

#%% UC 2.4 Erstellen einer Zusammenfassung

def summary_prints():

    '''Erstellen einer Funktion die prints als summary (Zusammenfassung) abspeichert
    
    '''

    print("Summary for Subject " + str(subject_data["subject_id"]))
    print("Year of birth:  " + str(subject_data["birth_year"]))
    print("Test level power in W:  " + str(subject_data["test_power_w"]))
    print(" \n")
    print("Maximum HR was: " + str(peaks['average_HR_10s'].max())) #entspricht maximum_hr => als peaks in Funktion mitgeben
    print("Was test terminated because exceeding HR " + str(termination))


#Versuch einer Alternativen summary, nicht funktionsfähig

#summary={"Summary for Subject " + str(subject_data["subject_id"]), 
         # "Year of birth:  " + str(subject_data["birth_year"], 
          #"Test level power in W:  " + str(subject_data["test_power_w"], 
          #"Maximum HR was: " + str(maximum_hr)),
          #"Was test terminated because exceeding HR " + str(termination))       
        #}

summary_prints()

#%% UC 2.5 Visualisierung der Daten

## Öffnen der Leistungsdaten

# Opening JSON file
def open_power_data(file):

    '''Öffnen der Leistungsdaten 
    
        parameters: 
            file(json): json data

        returns:
            power_data_watts(str): watt-data of subjects
            '''

    folder_input_data = os.path.join(folder_current, 'input_data')
    file_name =  os.path.join(folder_input_data, file)
    power_data_watts = open(file_name).read().split("\n")
    power_data_watts.pop(-1)
    len(power_data_watts)

    return power_data_watts


# %%
## Erstellung eines Plots

#peaks['average_HR_10s'].plot()

def plot_data():
    peaks_downsampled = peaks[peaks.index % 1000 == 0]  
    peaks_downsampled = peaks_downsampled.reset_index(drop=True)
    peaks_downsampled = peaks_downsampled.drop(["ECG_R_Peaks"],axis=1)
    peaks_downsampled["Power (Watt)"] = pd.to_numeric(open(file_name).read().split("\n"))
    peaks_downsampled.plot()

    peaks_downsampled = plot_data()


#%% UC 2.6 Manuelle Eingabe eines Abbruchkritierums

## Abfrage an Nutzer:in, ob Abgebrochen werden soll

def manual_termination():

    '''
    Funktion die es ermöglicht den Test manuell abzubrechen
    '''

    manual_termination = False
    manual_termination = input("Is this test invalid? (leave blank if valid): ")

    if manual_termination != False:
        termination = True

    return manual_termination 

#%% UC 2.7 Speichern der Daten


# Speichern der Daten
subject_max_hr = 220 - (2022 - subject_birth_year)
power_data_watts = open(file_name).read().split("\n")


data = {"User ID": subject_data["subject_id"], "Reason for test termation": manual_termination, "Average Heart Rate": average_hr_test, "Maximum Heart Rate": subject_max_hr, "Test Length (s)": len(power_data_watts), "Test Power (W)": subject_data["test_power_w"], "Average Power": peaks_downsampled["Power (Watt)"].mean()}

def save_data():

    '''
    Daten werden als JSON-Datei im results-Ordner gespeichert 
    '''
    #save data into json data format

    json_data_to_save = json.dumps(data)

    folder_current = os.path.dirname(__file__) 
    folder_input_data = os.path.join(folder_current, 'result_data')
    results_file = os.path.join(folder_input_data, 'data.json')

    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(json_data_to_save, f, ensure_ascii=False, indent=4)


    return save_data()
# %%

# %%

# %%

# %%

# %%