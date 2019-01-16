from json import JSONDecodeError, loads
from requests import get, exceptions

def http_request(url):
	try:
		request = get(url)
	except RequestException as e:
		print("Error fetching: " + str(e))
		return None

	if(request.status_code == 200):
		try:
			json_data = loads(request.text)
			json_data = json_data
		except JSONDecodeError as e:
			print("Error decoding: " + str(e))
			return None
	return json_data