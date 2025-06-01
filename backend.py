import requests

API_KEY = "6cf2caea0fd2ad648e16444778ec26aa"
SECOND = "14a52a0f9c1c243b9af5b1d0592911af"

def get_data(place, days = None):

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * days 
    filtered_data = filtered_data[:nr_values]
    
    return filtered_data 

if __name__ == "__main__":

    print(get_data(place = "Tokyo", days = 5))

