import csv
import os

def collect_user_info():
    user_data = []

    ##Erstellen der Variable und Abfrage der Eingabe
    username = input("Enter your username\n")
    
    #Eingabe des Usernames
    try:   
        # Convert it into string
        username = str(username)
        print("Input is a string. Username = ", username)
    except ValueError:
        print("Please enter a username with letters")
    user_data.append(username)

    #Eingabe des Alters
    age = input("Enter your age\n")

    try:
        # Convert it into integer
        age = int(age)
        print("Input is an integer number. Number = ", age, "Jahre")
    except ValueError:
        print("not an integer")
    user_data.append(age)

    #Eingabe der Größe
    height = input("Enter your height\n")

    try:
        # Convert it into integer
        height= float(height)
        print("Input is a float number. Number = ", height, "m")
    except ValueError:
        print("not a float")
    user_data.append(height)

#Eingabe des Gewichts
    weight = input("Enter your weight\n")

    try:
        # Convert it into integer
        weight= float(weight)
        print("Input is a float number. Number = ", weight, "Kg")
    except ValueError:
        print("not a float")
    user_data.append(weight)

#Berechnung des BMI
    bmi = round(weight / (height*height), 1)
    print("Your Body Mass Index is: ", str(bmi))
    user_data.append(bmi)

#Ausgabe der BMI-Werte
    if bmi < 18.5:
        bmi_result = "underweight"
        #print("Untergewicht")
    elif bmi >= 18.5 and bmi <= 24.9:
        bmi_result = "normalweight"
        #print("Normalgewicht")
    elif bmi >= 25.0 and bmi <=29.9:
        bmi_result = "overweight"
        #print("Übergewicht")
    else:
        bmi_result = "strong overweight"
        #print("starkes Übergewicht")
    user_data.append(bmi_result)

    return user_data

def save_to_csv(file_path, data):
    # Überprüfen, ob die Datei existiert
    file_exists = os.path.isfile(file_path)
    
    # Datei im Append-Modus öffnen
    with open(file_path, mode='a') as file:
        writer = csv.writer(file)
        
        # Wenn die Datei neu ist, schreiben Sie die Kopfzeile
        if not file_exists:
            writer.writerow(["username","age", "hight", "weight","bmi", "results"])
        
        # Daten in die CSV-Datei schreiben
        writer.writerow(data)

def main():
    # Benutzerdaten sammeln
    user_data = collect_user_info()
    
    # Daten in einer CSV-Datei speichern
    save_to_csv('user_data.csv', user_data)
    print("Daten wurden in 'user_data.csv' gespeichert.")

if __name__ == "__main__":
    main()