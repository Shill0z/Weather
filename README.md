# 🌤️ Weather Application

## **Overview**

A weather application developed in Python using **Tkinter** and the **Open-Meteo API**.

It allows users to search for a city and retrieve its current temperature through a simple graphical interface.

## **Features**

- **City search:** Search for a city by entering its name.
- **GPS coordinates:** Automatically retrieve the latitude and longitude of the selected city.
- **Current temperature:** Display the current temperature in Celsius.
- **Error handling:** Display an error message when the requested city cannot be found.
- **Graphical interface:** Simple interface built with Tkinter, including a custom logo.

## **Technologies Used**

- **Python**
- **Tkinter:** Graphical user interface.
- **Requests:** HTTP requests to retrieve weather data.
- **Pillow (PIL):** Image loading and resizing.
- **Open-Meteo API:** Weather data and geocoding.

## **Installation**

Install the required Python libraries:

```bash
pip install requests pillow
```

## **Running the Application**

Run the main Python file:

```bash
python main.py
```

## **Project Structure**

```text
Meteo/
│
├── images/
│   └── logoMeteo.png
│
├── main.py
└── README.md
```

## **APIs Used**

- **Geocoding API:** Converts city names into GPS coordinates.
- **Weather Forecast API:** Retrieves current weather information.

Documentation: [Open-Meteo](https://open-meteo.com/en/docs)
