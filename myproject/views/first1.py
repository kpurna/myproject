from django.http import Http404, HttpResponse, HttpResponseBadRequest
import json
from django.conf import settings

from myproject.db import query
def users12(request):
	id = request.REQUEST.get('id','')
	age = request.REQUEST.get('age','')
	
	if id != '':
		sql = "SELECT * from arc WHERE id= %s"
		param_for_user_details=[id]        
   
	elif age != '':
		sql = "SELECT * from arc WHERE age= %s"
		param_for_user_details=[age]
	else:
		sql = "SELECT * from arc"
		param_for_user_details=[]
	results = query(sql,*param_for_user_details)     
	final_test_map = []  
	metadata_totalcount=0 
    #result is constructed in the expected format
	for result in results:
		metadata_totalcount=metadata_totalcount+1
		response_map = {}
		response_map['id']=result['id']
		response_map['age']=result['age']                                                                                       
		final_test_map.append(response_map)       
	metadata = {"total_count":metadata_totalcount}
	response = {"metadata":metadata,'data_test':final_test_map} 
	data = json.dumps(response, encoding="ISO-8859-1")    
	http_response = HttpResponse(data,content_type="application/json")
	return http_response
	
def users123(request):
	id = request.REQUEST.get('id','')
	age = request.REQUEST.get('age','')
	
	if id != '':
		sql = "SELECT * from number WHERE id= %s"
		param_for_user_details=[id]        
   
	elif age != '':
		sql = "SELECT * from number WHERE age= %s"
		param_for_user_details=[age]
	else:
		sql = "SELECT * from number"
		param_for_user_details=[]
	results = query(sql,*param_for_user_details)     
	final_test_map = []  
	metadata_totalcount=0 
    #result is constructed in the expected format
	for result in results:
		metadata_totalcount=metadata_totalcount+1
		response_map = {}
		response_map['id']=result['id']
		response_map['age']=result['age']                                                                                       
		final_test_map.append(response_map)       
	metadata = {"total_count":metadata_totalcount}
	response = {"metadata":metadata,'data_test':final_test_map} 
	data = json.dumps(response, encoding="ISO-8859-1")    
	http_response = HttpResponse(data,content_type="application/json")
	return http_response
	
def users999(request):
	id = request.REQUEST.get('id','')
	location = request.REQUEST.get('location','')
	aadhar = request.REQUEST.get('aadhar','')
	voterid = request.REQUEST.get('voterid','')
	
	if id != '':
		sql = "select a.id,a.age,d.location,d.aadhar,d.voteridfrom arc a join details d on a.id = d.id"
		param_for_user_details=[id]        
   
	elif location != '':
		sql = "SELECT * from details WHERE location= %s"
		param_for_user_details=[location]
		
	elif aadhar != '':
		sql = "SELECT * from details WHERE aadhar= %s"
		param_for_user_details=[aadhar]
		
	elif voterid != '':
		sql = "SELECT * from details WHERE voterid= %s"
		param_for_user_details=[voterid]
		
	else:
		sql = "SELECT * from details"
		param_for_user_details=[]
	results = query(sql,*param_for_user_details)     
	final_test_map = []  
	metadata_totalcount=0 
    #result is constructed in the expected format
	for result in results:
		metadata_totalcount=metadata_totalcount+1
		response_map = {}
		response_map['id']=result['id']
		response_map['location']=result['location']
		response_map['aadhar']=result['aadhar']
		response_map['voterid']=result['voterid']
		final_test_map.append(response_map)       
	metadata = {"total_count":metadata_totalcount}
	response = {"metadata":metadata,'data_test':final_test_map} 
	data = json.dumps(response, encoding="ISO-8859-1")    
	http_response = HttpResponse(data,content_type="application/json")
	return http_response