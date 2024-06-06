import json
import requests

api_key = "f55313c5-7a02-40d1-ab0b-54e14fc32b8e"


def test(lon, lat):
    api_key = '1a6e0098-df91-403a-b905-47e75fb2095b'

    # Параметры запроса
    url = 'https://geocode-maps.yandex.ru/1.x/'
    data = {
        'apikey': api_key,
        'geocode': f'{lon},{lat}',
        'lang': 'ru_RU',
        'format': 'json'
    }

    response = requests.get(url, params=data)

    return response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["name"]


if __name__ == "__main__":
    res = {}
    
    with open("..\\data\\points_position.json", "r") as f:
        data = json.load(f)

    for k, v in data.items():
        try:
            ans = test(v["lon"], v["lat"])

            print(k, ans)

            r = input("y/n: ")

            if "y" in r:
                res[k] = ans
            else:
                break
        except:
            break

    with open("..\\data\\points_name.json", "w", encoding="utf-8",) as f:
        json.dump(res, f)
