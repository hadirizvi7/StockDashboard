import requests
from config_files.config import RAPID_API_KEY, RAPID_API_HOST

def data_pull(ticker):
    url = "https://yahoo-finance127.p.rapidapi.com/price/{}".format(ticker)
    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": RAPID_API_HOST
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        output = response.json()
        if 'message' in response.json():
            output['valid'] = False
        else:
            output['valid'] = True
        return output
    else:
        #_dict = response.json()
        #_dict['valid'] = False
        #return _dict
        return {'valid': False}
    
