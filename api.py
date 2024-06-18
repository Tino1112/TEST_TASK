import requests


def send_data(date, hour, minute, name, surname, sex):
    url = "http://bazihero.com/api/algo/firststep"
    payload = {
        "date": date,
        "hour": hour,
        "minute": minute,
        "name": name,
        "surname": surname,
        "sex": sex
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    if response.text:
        try:
            return response.json()
        except ValueError:
            # Print the response text to debug the issue
            print("Response content is not valid JSON:", response.text)
            return {"error": "Invalid JSON response"}
    else:
        # Handle the case where the response body is empty
        print("Response content is empty")
        return {"error": "Empty response"}

