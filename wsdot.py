from python_wget import http_request

url = "http://www.wsdot.com/Traffic/api/MountainPassConditions/MountainPassConditionsREST.svc/GetMountainPassConditionsAsJson?AccessCode="
api_key = "f48c740d-c9ea-47f4-9bd4-b1e220cda26b"

json_data = http_request(url + api_key)
json_data = json_data[11]


try:
	eastbound_restrictions = json_data["RestrictionOne"]["RestrictionText"]
	westbound_restrictions = json_data["RestrictionTwo"]["RestrictionText"]
	condition = json_data["RoadCondition"]
	weather = json_data["WeatherCondition"]
except KeyError as e:
	print("Error accessing " + str(e))
	exit(1)

print("Condition: " + condition)
print("Weather: " + weather)
print("Westbound: " + westbound_restrictions)
print("EastBound: " + eastbound_restrictions)