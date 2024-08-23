import datetime
import streamlit as st

'''
# TaxiFareModel front
'''

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


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

    '''

    2. Let's build a dictionary containing the parameters for our API...

    3. Let's call our API using the `requests` package...

    4. Let's retrieve the prediction from the **JSON** returned by the API...

    ## Finally, we can display the prediction to the user
    '''
