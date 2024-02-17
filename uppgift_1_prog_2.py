from datetime import datetime, time
import time
avsluta = False
while True:
	nu = datetime.now()
	tid = nu.hour
	if tid <= 6 or tid >= 23:
		avsluta = True
#resten av funktionen eller applikationen här

	if avsluta == True:
		print("dags att sova")
		quit()

	print("ok att vara vaken")
	time.sleep(5)