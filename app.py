'''
This module implements the TaxiFareModel front
'''

import json
import datetime
import requests
import streamlit as st


URL = 'https://taxifare-502551074520.europe-west1.run.app/predict'


st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

## Add some controllers in order to ask the user to select the parameters for
# their ride
#
# Let's ask for:
#   - date and time
#   - pickup longitude
#   - pickup latitude
#   - dropoff longitude
#   - dropoff latitude
#   - passenger count

# Get date
pickup_date = st.date_input("Pickup date", value=datetime.date.today())

# Get time
pickup_time = st.time_input('Pickup time', value=datetime.datetime.now())

# Get pickup latitude
pickup_latitude = st.number_input('Insert pickup latitude', value=40.783282)

# Get pickup longitude
pickup_longitude = st.number_input('Insert pickup longitude', value=-73.950655)

# Get dropoff latitude
dropoff_latitude = st.number_input('Insert dropoff latitude', value=40.769802)

# Get dropoff latitude
dropoff_longitude = st.number_input('Insert dropoff longitude', value=-73.984365)

# Get passenger count
passenger_count = st.selectbox(
    'Number of passengers',
    list(range(1, 9))
)


## Once the parameters are set, call the API to retrieve a prediction
if st.button('Predict fare'):

    # Fuild a dictionary containing the parameters for our API
    params = dict(
        pickup_datetime=' '.join(
            [str(pickup_date), str(pickup_time)]),  # e.g., 2014-07-06 19:18:00
        pickup_longitude=pickup_longitude,
        pickup_latitude=pickup_latitude,
        dropoff_longitude=dropoff_longitude,
        dropoff_latitude=dropoff_latitude,
        passenger_count=passenger_count)

    # Call the API
    try:
        response = requests.get(URL, params=params, timeout=30)

        if response.status_code == 200:

            # Retrieve the prediction from the JSON response returned by the API
            prediction = json.loads(response.content)

            ## Finally, we can display the prediction to the user
            fare = round(prediction['fare'], 2)
            st.text(f"Predicted fare: {fare}$")

        else:
            st.text('Could not predict a fare :(')
    except requests.ReadTimeout:
        st.text('Could not predict a fare: service is unresponsive :(')
