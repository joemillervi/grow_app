#series of batches to keep data current in db
import yaml
import sqlite3
import time

from hardware_interfaces.camera import take_image_and_write_file

conn = sqlite3.connect('/home/pi/growdatabase.db')

def write_temp_to_db(
	time,
	temp,
	humid,
):
    c = conn.cursor()
    c.execute('INSERT INTO temps VALUES (0, {time}, {temp}, {humid})'.format(time=time, temp=temp, humid=humid))
    conn.commit()
   

def fetch_most_recent_temp_from_fs():
    # read yaml file of data
    # if there is not match for timestamp write to db
	with open("./data/temp_and_humid.yaml", 'r') as stream:
		recent_temp = yaml.load(stream)
        print recent_temp
        return recent_temp

def date_exists_in_db(timestamp):
    c = conn.cursor()
    c.execute('SELECT * FROM temps WHERE time={timestamp}'.format(timestamp=timestamp))
    match_in_db = c.fetchone()
    print match_in_db
    return bool(match_in_db)

# Loop
print 'Entering Loop'
while True:
    # Save temp to DB every 7 min
    take_image_and_write_file()
    print 'Took Image'
    current_tmp = fetch_most_recent_temp_from_fs()
    data = current_tmp['data']
    if date_exists_in_db(data['time']):
        print 'ERROR This time has already been logged'
    else:
		write_temp_to_db(data['time'], data['temp'], data['humidity'])
		print 'Wrote temp to db: {data}'.format(data=data)
    time.sleep(420)
