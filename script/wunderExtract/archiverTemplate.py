# api info https://docs.google.com/document/d/1w8jbqfAk0tfZS5P7hYnar1JiitM0gQZB-clxDfG3aD0/edit  on Wunderground

import datetime
import requests

start = datetime.datetime.strptime("2019-08-02", "%Y-%m-%d")
end = datetime.datetime.strptime("2020-04-30", "%Y-%m-%d")

date_array = \
    (start + datetime.timedelta(days=x) for x in range(0, (end-start).days))

for date_object in date_array:
    date = date_object.strftime("%Y%m%d")
    url = "https://api.weather.com/v2/pws/history/all"
    payload = {'stationId': 'INSERT_STATIONID', 'format': 'json', 'units': 'm', 'date': date, 'apiKey': 'INSERT_KEY'}
    resp = requests.get(url, params=payload)
    print(resp.status_code, " --- ", date)
    file = open('%s.json' % date, "w+")
    file.write(resp.text)
    file.close()
