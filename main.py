import requests
from tkinter import *
import tkinter as ttk
from PIL import Image, ImageTk

root = Tk()

img = Image.open("./images/logoMeteo.png")
img.thumbnail((150, 150))


logo = ImageTk.PhotoImage(img)  # keep this reference
logo_label = ttk.Label(root, image=logo, bg="#348dd1")
logo_label.pack(pady=20)

villeLabel = ttk.Label(root, text="Entrez une ville :", bg="#348dd1")
villeLabel.config(font=("Helvetica", 12, "bold"))
villeLabel.pack()

ville = ttk.Entry(root, bg="#26699c", relief="solid", width=25, font=("Helvetica", 12))
ville.bind("<Return>", lambda event: getTemp(ville.get()))
ville.pack()

affichage = ttk.Label(root, text="", bg="#348dd1")


def getLongitudeLatitude(ville):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": ville,
        "count": 1,
        "language": "fr",
        "format": "json"
    }
    reponse = requests.get(url, params=params)
    donnees = reponse.json()
    if not "results"in donnees or len(donnees["results"]) == 0:
        affichage.config(text=f"{ville} n'existe pas..", fg="#741b1b", font=("Helvetica", 12, "bold"))
        affichage.pack(pady=(30, 0))
        print(f"ERREUR : {ville} n'existe pas..")
        return

    latitude = donnees["results"][0]["latitude"]
    longitude = donnees["results"][0]["longitude"]

    return (latitude, longitude)

def getTemp(ville):
    url_meteo = "https://api.open-meteo.com/v1/forecast"
    res = getLongitudeLatitude(ville)
    if res is None:
        return
    latitude, longitude = res
    paramsMeteo = {
    "latitude": latitude,
    "longitude" : longitude,
    "current": "temperature_2m"
    }

    reponseMeteo = requests.get(url_meteo, params=paramsMeteo)
    meteo = reponseMeteo.json()

    affichage.config(text=f"La température à {ville} est de {meteo["current"]["temperature_2m"]}°C", fg="black", font=("Helvetica", 12, "bold"))
    affichage.pack(pady=(30, 0))
    print("Température :", meteo["current"]["temperature_2m"], "°C")




root.title("Météo")
root.geometry("450x750")
root.minsize(450, 750)
root.maxsize(450, 750)
root.config(background="#348dd1")
root.mainloop()