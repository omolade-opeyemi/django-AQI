from django.shortcuts import render
def home(request):
	import json
	import requests

	api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=D5132E8C-0F77-4A30-AAFB-083833F44E1C")
	# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=D5132E8C-0F77-4A30-AAFB-083833F44E1C

	try:
		api= json.loads(api_request.content)
	except Exception as e:
		api = "Error..."


	return render(request, 'home.html', {'api' : api })

def about(request):
	return render(request, 'about.html', {})
