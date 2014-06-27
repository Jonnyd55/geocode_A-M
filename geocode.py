import csv
import requests

'''
This script will read a .csv file and geocode the address using Texas A&M's geocoding service (FREE!!!).
It requires the fantastic Requests package.
You will need an API key from A&M, available here --> http://geoservices.tamu.edu/Services/Geocode/WebService/
You are only allowed 2500 API hits. After that you need to sign up for a partnership, or purchase credits.

Your address should look like this:
address, city, state
150 main street, norfolk, va
'''

#Name your file here
read_file = 'addresses.csv'

with open(read_file, 'rb') as address_data:
	add_reader = csv.reader(address_data, delimiter=",")
	data = []
	
	def stringify(item):
		item_list = item.split(' ')
		stringified = '%20'.join(item_list)
		return stringified
		
	def geocode(add, city, state):
		api_key = 'ENTER YOUR KEY HERE'
		
		starter_url = 'http://geoservices.tamu.edu/Services/Geocode/WebService/GeocoderWebServiceHttpNonParsed_V04_01.aspx?streetAddress='
		
		tail_url = '&city='+ stringify(city) +'%20&state='+ state +'&apikey='+ api_key +'&format=csv&census=true&censusYear=2000|2010&notStore=false&version=4.01'
		
		api_hit = starter_url + stringify(add) + tail_url
		
		return str(api_hit)
	
	iter = 0
	for row in add_reader:
		#row[0] = address, row[1] = city, row[2] = state. We're going to take everything from the row and just append the lat and long to it.
		data_row = row		
		r = requests.get(geocode(row[0], row[1], row[2]))
		response = r.text.split(',')
		#This is the lat in the reponse
		data_row.append(response[3])
		#This is the long
		data_row.append(response[4])
		#Census Tract
		data_row.append(str(response[31]))
		#Census County FIPS
		data_row.append(response[32])
		data.append(data_row)
		iter += 1
		print "Geocoded row", iter
		

with open('geocodes.csv', 'wb') as final_file:
		orgwriter = csv.writer(final_file)
		#Name your headers here
		header_row = ['DATE','ITEM', 'ADDRESS', 'CITY','STATE','LAT', 'LONG', 'CENSUS_TRACT', 'CESNSUS_COUNTY_FIPS']
		orgwriter.writerow(header_row)
		for codes in data:
			orgwriter.writerow(codes)

