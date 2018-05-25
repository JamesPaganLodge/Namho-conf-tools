import pandas as pd

eventsHeaders = ['code','desc']

bookings = pd.read_csv('bookings.csv', sep=',', header=None)
events = pd.read_csv('events.csv', sep=',', names = eventsHeaders)

d = dict(events[['code','desc']].values)

bookings.replace(d, inplace=True)

# outputs the replaced file
bookings.to_csv('booking2.csv')

df = pd.DataFrame(bookings)

for i, row in df.iterrows():
    ref = df.loc[[i],[0]].to_string(index=False)
    name = df.loc[[i],[2,1]].to_string(index=False)
    print('Reference: {}'.format(ref), 'Name: {}'.format(name))

for row in df.itertuples():
    print('Reference: {}'.format(row.0), 'Name: {} {}'.format(row.2, row.1))