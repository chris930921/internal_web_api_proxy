from django.http import HttpResponse
import json
import subprocess

def Index(request):
	raw = request.body
	url = request.GET.get('url')
	command = ""
	if 'HTTP_X_AUTH_TOKEN' in request.META:
		command += "curl -s '"+url						+"'"
		command += " -X "+request.method
		command += " -H 'Content-Type:"+request.META['CONTENT_TYPE']		+"'"
		command += " -H 'Accept:"+request.META['HTTP_ACCEPT']			+"'"
		command += " -H 'X-Auth-Token:"+request.META['HTTP_X_AUTH_TOKEN']	+"'"
	else:
		command += "curl -s '"+url						+"'"
		command += " -X "+request.method
		command += " -H 'Content-Type:"+request.META['CONTENT_TYPE']		+"'"
		command += " -H 'Accept:"+request.META['HTTP_ACCEPT']			+"'"
		command += " -d '"+raw							+"'"

	result = subprocess.check_output(command, shell=True)
	response = HttpResponse(result, content_type="application/json")
	response['Access-Control-Allow-Origin'] = '*'
	response['Access-Control-Allow-Headers'] = 'Content-Type,Accept,X-Auth-Token'
	return response
