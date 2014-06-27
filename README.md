Geocode script
=========

This is a script written to geocode address using the Texas A&M geocoding service. 
You will need:
  - An [API key] [1] from the university.
  - The python package [Requests].
  - A .csv of addresses that you want to geocode.

The structure of your .csv file is key. You __Must have__ the following three cells in your data:
  - Address
  - City
  - State

The script reads your file, builds a URL to pass to the A&M geocode API, and returns the lat/long coordinates, census tract and County FIPS number according to the 2010 cesnsus. 

The __addresses.csv__ file provided is a good template to follow. You can add as many cells to the right of the **state** data point. The script will always append the Latitude and Longitude to the very end of the row.

**NOTE** I've had some misses from this API. In particular, it doesn't handle numbered streets very well. You can check the accuracy of your addresses at the A&M [interactive geocode] [2] site.

License
----

MIT


[1]:http://geoservices.tamu.edu/Services/Geocode/WebService/
[2]:https://geoservices.tamu.edu/Services/Geocode/Interactive/
[Requests]:http://docs.python-requests.org/en/latest/