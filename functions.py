
import requests
import json
import time
import datetime


def title_printer(title):
    print('=' * 80)
    print(f"{title:^80}")
    print('=' * 80)


def getting_user_location():
    """Uses the GeoPlugin API Service to get the longitude and latitude from the user so that we can use it com the AccuWeather API to get the user's weather information. It uses no parameters"""

    geoplugin_request = requests.get("http://www.geoplugin.net/json.gp")

    if geoplugin_request.status_code != 200:
        print("It was not possible to obtain your current location. Please, try again later!")
        exit()
    
    else:
        geo_plugin_response = geoplugin_request.json()
        latitude = geo_plugin_response['geoplugin_latitude']
        longitude = geo_plugin_response['geoplugin_longitude']

        user_location_info = tuple([latitude, longitude])

        return user_location_info


def getting_location_key(latitude, longitude):
    """Uses the provided latitude and longitude to get the location key that'll be used in the forecast request"""

    API_Key = "zIGuOeUd0aE4O621Gj1KGDc6JiZ3PAGb"
    http_request = f"http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={API_Key}&q={latitude}%2C%20{longitude}&language=pt-br"

    location_key_request = requests.get(http_request)

    if location_key_request.status_code != 200:
        print("It was not possible to retrive your location key. Please, try again later!!")
        exit()

    else:
        location_key_response = location_key_request.json()

    location_key = location_key_response['Key']
    
    # EXTRACTING LOCATION INFORMATION --
    country = location_key_response['Country']['LocalizedName']
    state = location_key_response['AdministrativeArea']['ID']
    city = location_key_response['ParentCity']['LocalizedName']
    neighbourhood = location_key_response['LocalizedName']

    # PRINTING LOCATION INFORMATION --
    title_printer(" ---- LOCALIZAÇÃO ----")
    time.sleep(0.5)

    print("Country", end="")
    print(f"{country:.>73}")
    time.sleep(0.5)

    print("State", end="")
    print(f"{state:.>75}")
    time.sleep(0.5)

    print("City", end="")
    print(f"{city:.>76}")
    time.sleep(0.5)

    print("Region", end="")
    print(f"{neighbourhood:.>74}")
    time.sleep(0.5)

    return location_key


def getting_user_weather_1(location_key):
    """Uses the provided location key information to retrieve from AccuWeather the weather forecast for 1 day"""

    API_Key = "zIGuOeUd0aE4O621Gj1KGDc6JiZ3PAGb"
    http_request = f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{location_key}?apikey={API_Key}&language=pt-br&metric=true"

    accu_request = requests.get(http_request)

    if accu_request.status_code != 200:
        print("It was not possible to stablish connection with the metherological server. Please, try again later!")
        exit()

    else:
        accu_response = accu_request.json()

    return accu_response


def printing_weather_1(accu_response):
    """Extractcs the json information provided by the server and prints it nicely"""

    min_temperature = f"{accu_response['DailyForecasts'][0]['Temperature']['Minimum']['Value']} ºC"
    max_temperature = f"{accu_response['DailyForecasts'][0]['Temperature']['Maximum']['Value']} ºC"
    weather_forecast = accu_response['Headline']['Text']
    for_what_time = accu_response['Headline']['EffectiveDate']
    source = ' -- AccuWeather API Service'

    #PRINTING WEATHER INFORMATION --
    title_printer(" ---- WEATHER SOON ---- ")

    print("MINIMAL TEMPERATURE", end="")
    print(f"{min_temperature:.>62}")
    time.sleep(0.5)

    print("MAXIMUM TEMPERATURE", end="")
    print(f"{max_temperature:.>62}")
    time.sleep(0.5)

    print("")
    print("WEATHER CONDITIONS:")
    print(for_what_time)
    print("")
    time.sleep(0.5)

    print(weather_forecast)
    print(source)
    print("= " * 40)
    time.sleep(0.5)


def getting_user_weather_5days(location_key):
    """Uses the provided location key information to retrieve from AccuWeather the weather forecast for 5 days"""

    API_Key = "zIGuOeUd0aE4O621Gj1KGDc6JiZ3PAGb"
    http_request = f"http://dataservice.accuweather.com/forecasts/v1/daily/5day/{location_key}?apikey={API_Key}&language=pt-br&metric=true"

    accu_request_5 = requests.get(http_request)

    if accu_request_5.status_code != 200:
        print("It was not possible to stablish connection with the metherological server. Please, try again later!")
        exit()

    else:
        accu_response_5 = accu_request_5.json()

    return accu_response_5


def printing_weather_5(accu_response_5):
    """Extractcs the json information provided by the server and prints it nicely"""

    title_printer(" ---- 5 DAYS FORECAST ---- ")

    for daily_weather_info in accu_response_5['DailyForecasts']:
        print(daily_weather_info['Date'])

        print("MINIMAL TEMPERATURE", end="")
        print(f"{daily_weather_info['Temperature']['Minimum']['Value']:.>59}", "ºC")
        time.sleep(0.5)

        print("MAXIMUM TEMPERATURE", end="")
        print(f"{daily_weather_info['Temperature']['Maximum']['Value']:.>59}", "ºC")

        print(daily_weather_info['Day']['IconPhrase'])
        print(" -- " * 20)
        time.sleep(0.5)
    
    print("=" * 80)


def search_engine(city_name):
    """returns the location key of the typed city name"""

    API_Key = "zIGuOeUd0aE4O621Gj1KGDc6JiZ3PAGb"
    http_request = f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={API_Key}&q={city_name}&language=pt-br"

    search_request = requests.get(http_request)

    if search_request.status_code != 200:
        print(f"It was not possible to retrive information about {city_name}")

    else:
        search_response = search_request.json()
        print(f"Obtaining information about the weather in {city_name}")

    return search_response[0]['Key']
