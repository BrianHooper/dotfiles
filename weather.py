from python_wget import http_request
from datetime import datetime


def print_forecast(city):
    url = "http://api.openweathermap.org/data/2.5/forecast?q=" + city + ",US&mode=json&units=imperial&APPID="
    api_key = "933f835cb1b6ada5fc2c27396d93d5b6"
    json_data = http_request(url + api_key)

    try:
        city = json_data["city"]["name"]
        forecast = json_data["list"]
    except KeyError as e:
        print("Error accessing " + str(e))
        exit(1)

    current_date = datetime.now()
    forecast_date = current_date.replace(day=current_date.day + 1, hour=12, minute=0, second=0, microsecond=0)

    print(city + ": ")
    for forecast_element in forecast:
        datetime_object = datetime.strptime(forecast_element["dt_txt"], '%Y-%m-%d %H:%M:%S')
        if datetime_object.date() == forecast_date.date():
            forecast_date = forecast_date.replace(day=forecast_date.day + 1)
            try:
                temperature = int(forecast_element["main"]["temp"])
                print("\t" + str(datetime_object.strftime("%A")) + ": " +
                      str(temperature) + "°, " +
                      str(forecast_element["weather"][0]["description"]))
            except KeyError:
                continue


print_forecast("Seattle")
print_forecast("Ellensburg")
