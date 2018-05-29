import pandas as pd

eventsHeaders = ['code','desc']

bookings = pd.read_csv('bookings.csv', sep=',', header=None)
events = pd.read_csv('events.csv', sep=',', names = eventsHeaders)

d = dict(events[['code','desc']].values)

bookings.replace(d, inplace=True)

# outputs the replaced file
bookings.to_csv('booking2.csv')
