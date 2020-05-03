from alertsys import checkcond
import time
import json


def select_thresh():
    """This is a function to set thresholds of parameters
    These would be used by the notification system to compare
    with the sensor values and send an email.
    Returns:
        {(int,int,str)} -- (threshold 1, thereshold 2,user's email)
    """

    # load data from the parameters.txt file
    with open('parameters.txt', 'r') as f:
        data = f.read()
    data = data.replace('\'', '\"')
    json_dict = json.loads(data)

    # extract data from the json
    category1 = json_dict['category1']
    category2 = json_dict['category2']
    email = json_dict['email']

    # set default values for category1 and category2, in case they have not been set
    if category1 == "":
        category1 = 'Car'
    if category2 == "":
        category2 = 'Summer'

    '''
    # for debuging
    print(category1)
    print(category2)
    print(email)
    '''

    # threshold selection criterion
    if category1 == "Car":

        if category2 == "Summer":
            # Temperature in celsius
            thresh_engineTemp = 107
            # Pressure in psi
            thresh_tirePressure = 28
        elif category2 == "Winter":
            thresh_engineTemp = 102
            thresh_tirePressure = 31

    elif category2 == "Truck":

        if category2 == "Summer":
            thresh_engineTemp = 115
            thresh_tirePressure = 31

        elif category2 == "Winter":
            thresh_engineTemp = 110
            thresh_tirePressure = 34

    thresh_tireDistanceKm = 60000
    thresh_oilTimehrs = 5000

    return (thresh_engineTemp, thresh_tirePressure, thresh_oilTimehrs, thresh_tireDistanceKm, email)

# intialize flag as false indicating no maintainance or replacement is required
f = False

# an infite loop which will continue running until maintainance or replacement is required
while True:
    print('waiting for update')
    if not f:
        (t1, t2, t3, t4, email) = select_thresh()
        f = checkcond(f, t1, t2, t3, t4, email)
    else:
        break
    time.sleep(5)
