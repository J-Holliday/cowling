from datetime import datetime
import subprocess

#SCRIPT_PATH = '/home/pi/ascetic/BME280/Python27/bme280_sample.py'
SCRIPT_PATH = '/home/iida/ascetic/cowling/dummy_bme280_sample.py'
LOG_PATH = '/home/iida/ascetic/cowling/temp_log'
DST_PATH = '/home/iida/ascetic/cowling/temperature_log'

subprocess.call('python {} > {}'.format(SCRIPT_PATH, LOG_PATH), shell=True)
time = datetime.now().strftime('%Y%m%d%H%M%S')
subprocess.call('sudo mv {} {}/temp{}'.format(LOG_PATH, DST_PATH, time), shell=True)

print('temperature_logger.py is executed at {}'.format(
      datetime.now().strftime('%Y/%m/%d - %H:%M:%S')))
