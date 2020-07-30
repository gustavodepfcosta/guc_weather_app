
import functions as fc

fc.title_printer(" ---- GuC Weather | source: AccuWeather ----")

print("Definindo a sua localização aproximada...")

lat_long = fc.getting_user_location()

latitude, longitude = lat_long[0], lat_long[1]

location_key = fc.getting_location_key(latitude, longitude)

while True:
    print("Você gostaria de saber sua previsão do tempo para 1 dia ou para 5? (1) ou (5)")
    forecast_getter = input("Ou gostaria de fazer uma busca pelo nome da cidade? (2) - ")

    try:
        forecast_getter = int(forecast_getter)

        if forecast_getter != 1 and forecast_getter != 5 and forecast_getter != 2:
            print("Você deve entrar com o número 1, 2 ou 5!")
            continue

        else:
            break

    except KeyError:
        print("Você deve entrar com o número 1, 2 ou 5!")

if forecast_getter == 1:
    weather_1 = fc.getting_user_weather_1(location_key)
    fc.printing_weather_1(weather_1)

elif forecast_getter == 5:
    _5_days_weather = fc.getting_user_weather_5days(location_key)
    fc.printing_weather_5(_5_days_weather)

elif forecast_getter == 2:
    search_location_key = fc.search_engine()

    while True:
        search_for_how_many_days = input("Você gostaria de saber a previsão do tempo de um dia ou de cinco? (1) ou (5)")

        try:
            search_for_how_many_days = int(search_for_how_many_days)

            if search_for_how_many_days != 1 and search_for_how_many_days != 5:
                print("Você deve entrar com o número 1 ou 5!")
                continue

            else:
                break

        except KeyError:
            print("Você deve entrar com o número 1 ou 5!")

    if search_for_how_many_days == 1:
        weather_1 = fc.getting_user_weather_1(search_location_key)
        fc.printing_weather_1(weather_1)
    
    elif forecast_getter == 5:
        _5_days_weather = fc.getting_user_weather_5days(search_location_key)
        fc.printing_weather_5(_5_days_weather)


