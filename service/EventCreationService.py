from spyne.decorator import rpc 
from spyne.model.complex import Iterable
from spyne.model.primitive import Unicode, Boolean, Integer
from spyne.service import ServiceBase
from datetime import datetime
import requests

class EventCreationService(ServiceBase):
  @rpc(Unicode, Unicode, Unicode, Integer, _returns=Unicode)
  def CreateEvent(ctx,name,date, description, ticket_amount):
    url = ctx.ticket_url;
    date_object = datetime.strptime(date, '%b %d %Y %I:%M%p')
    if (date_object < datetime.now()):
      return False
    
    create_event_payload = {'EventName': name, 'DateTime': date, 'Description': description}
    create_event_resp = requests.post(url+'/event', json = payload)
    
    if (create_event_resp.ok):
      # Tolong request nya ngereturn id yang abis diinsert ya
      create_event_json = create_event_resp.json()
      create_ticket_payload = {'EventId' : create_event_json["id"], 'Amount': ticket_amount}
      create_ticket_request = requests.post(url+'/ticket', json = payload)

      if (create_ticket_request.ok):
        return True
      else:
        return False
        
    else:
      return False

    


