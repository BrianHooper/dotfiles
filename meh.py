from python_wget import http_request

url = "https://api.meh.com/1/current.json?apikey="
api_key = "x6t3Y1wHAj45JQUhb!3aHqsK6bJntM6h"

json_data = http_request(url + api_key)

try:
	title = json_data["deal"]["title"]
	available = not json_data["deal"]["launches"][0]["soldOutAt"]
	price = str(json_data["deal"]["items"][0]["price"])
except KeyError as e:
	print("Error accessing " + str(e))
	exit(1)

if available:
	print("$" + price + ": " + title)
else:
	print("Sold out: $" + price + ": " + title)