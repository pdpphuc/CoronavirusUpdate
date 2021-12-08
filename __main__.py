import requests
from win10toast import ToastNotifier
import json

def coronavirus_update():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = r.json()
    text = f'Cases: {data["cases"]:,}\nDeaths: {data["deaths"]:,}\nRecovered: {data["recovered"]:,}'

    t = ToastNotifier()
    t.show_toast('Covid 19 Update', text, icon_path="covid19-icon.ico", duration=20)

coronavirus_update()