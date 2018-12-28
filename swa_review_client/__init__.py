import requests
from string import Template


def fetch(confirmationNumber, fName, lName):
    url = 'https://www.southwest.com/api/air-checkin/v1/air-checkin/page/air/check-in/review'

    template = Template('''{
        "confirmationNumber":"$confirmationNumber",
        "passengerFirstName":"$fName",
        "passengerLastName":"$lName",
        "application":"air-check-in",
        "site":"southwest"
        }''')

    data = template.substitute({'confirmationNumber': confirmationNumber, 'fName': fName, 'lName': lName})
    headers = {"Content-Type": "application/json", "x-api-key": "l7xx944d175ea25f4b9c903a583ea82a1c4c"}
    response = requests.post(url, data=data, headers=headers)
    print('status {0}', response.status_code)
    print(response.json())
