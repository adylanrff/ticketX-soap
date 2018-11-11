from suds.client import Client

test_client = Client('http://localhost:8000/?wsdl')
results = test_client.service.test("Dave",5)
for result in results[0]:
  print result