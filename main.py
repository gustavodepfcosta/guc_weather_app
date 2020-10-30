
import functions as fc


def main():
    fc.title_printer(" ---- GuC Weather | source: AccuWeather ----")

    print("Obtaining your current location...")

    lat_long = fc.getting_user_location()

    latitude, longitude = lat_long[0], lat_long[1]

    location_key = fc.getting_location_key(latitude, longitude)

    while True:
        print(" -- " * 20)
        print("Would you like to know the forecast info for 1 or 5 days? (1) ou (5)")
        forecast_getter = input("Or would you like to make a search by city name? (2) - ")

        try:
            forecast_getter = int(forecast_getter)

            if forecast_getter != 1 and forecast_getter != 2 and forecast_getter != 5:
                print("You must type in the numbers 1, 2 or 5!")
                continue

            else:
                break

        except KeyError:
            print("You must type in the numbers 1, 2 or 5!")

    if forecast_getter == 1:
        weather_1 = fc.getting_user_weather_1(location_key)
        fc.printing_weather_1(weather_1)

    elif forecast_getter == 2:
        city_name = input("What's the city name? ").title()

        search_location_info = fc.search_engine(city_name)

        fc.searched_city_info_printer(search_location_info)

        while True:
            print(" -- " * 20)
            search_for_how_many_days = input("Would you like to know the forecast info for 1 or 5 days? (1) ou (5) ")

            try:
                search_for_how_many_days = int(search_for_how_many_days)

                if search_for_how_many_days != 1 and search_for_how_many_days != 5:
                    print("You must type in the numbers 1 or 5!")
                    continue

                else:
                    break

            except KeyError:
                print("You must type in the numbers 1 or 5!")

        if search_for_how_many_days == 1:
            weather_1 = fc.getting_user_weather_1(search_location_info['Key'])
            fc.printing_weather_1(weather_1)
        
        elif search_for_how_many_days == 5:
            _5_days_weather = fc.getting_user_weather_5days(search_location_info['Key'])
            fc.printing_weather_5(_5_days_weather)
            fc.searched_city_info_printer(_5_days_weather)
            print(_5_days_weather)

    elif forecast_getter == 5:
        _5_days_weather = fc.getting_user_weather_5days(location_key)
        fc.printing_weather_5(_5_days_weather)


if __name__ == '__main__':
    main()