# 1) measuring elapsed time
print("Measuring elapsed time:")
import time
start = time.time()
value = 0
for x in range(1000000):
    value += 1
end = time.time()
print('The loop ran for', end - start, 'seconds', '\n')

# 2) printing current time - local and UTC
print('Printing current date time:')
import datetime
print('Current datetime:', datetime.datetime.now())
print('UTC datetime:', datetime.datetime.utcnow())
print()

# 3) parsing date time from string
print('Parsing date time from string:')
date_time_str = '2022-03-26 00:01:02.123'
dt = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
print('Parsed date time is:', dt, '\n')

# 4) date time arithmetics 
print('Date time arithmetics:')
adjusted_dt = dt + datetime.timedelta(days=2, hours=1, minutes=-1, seconds=-1)
print('Adjusted date time is:', adjusted_dt, '\n')
