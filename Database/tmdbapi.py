import requests, json

def api_request(url):
    try:
        headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMTgyOWNiYjcyZDc0N2E0N2NjMGJjZmYxYWQ1MjdlNiIsInN1YiI6IjY1Yzc3MTdlY2U2YzRjMDE3Y2I5MWQzOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.jb-Jk9ni5U4Nnl3VPBWmXsDKNUcUSujZxN2bzXrTynk"
            }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = json.loads(response.text)
            return data
    
    except requests.exceptions.RequestException as e:
        print("API request failed:", e)
        