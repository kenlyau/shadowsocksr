import time
import logging

def getKeys(key_list):
	return key_list
	#return key_list + ['plan'] # append the column name 'plan'

def isTurnOn(row, cfg):
        return row['vip'] >= cfg['vip'] and ( row['expire_time'] == 0 or row['expire_time'] > time.time())
	#return True
	#return row['plan'] == 'B' # then judge here
