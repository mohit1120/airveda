*Tech Stack Used*

1. Python
2. Djando 
3. Rest framework
4. db.sqlite3


*Running server at localhost*

To add device
https://localhost:8000/deviceadd

To fetch uid and name of a device using uid
https://localhost:8000/deviceone/{device-uid}

To fetch uid and name of all the created devices
https://localhost:8000/devicelist

To delete a device using device Id
https://localhost:8000/deviceremove/{device-uid}




To insert temperature reading of a device
http://localhost:8000/api/temperatureadd

//To fetch device Recorded temperature
http://localhost:8000/api/temperaturelist/{device-uid}/?startDate={date}&endDate={date}



To insert Humidity Reading of a device
http://localhost:8000/api/humidityadd

//To fetch device Recorded humidity
http://localhost:8000/api/temperaturelist/{device-uid}/?startDate={date}&endDate={date}
