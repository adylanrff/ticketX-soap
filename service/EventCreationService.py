from spyne.decorator import rpc 
from spyne.model.complex import Iterable
from spyne.model.primitive import Unicode, Boolean, Integer
from spyne.service import ServiceBase
from datetime import datetime
from model import Event, Section

import requests

class EventCreationService(ServiceBase):
  @rpc(Event, Iterable(Section), _returns=Boolean)
  def CreateEvent(ctx,event,section_list):
    url = ctx.udc.ticket_url;

    # if (event.start_at < event.end_at):
    #   return False
      
    create_event_payload = {
      'event_name': event.name, 
      'partner_id':event.partner_id, 
      'start_at': event.start_at, 
      'end_at': event.end_at, 
      'description': event.description, 
      'location': event.location
    }

    print("Event: " , create_event_payload)
    create_event_resp = requests.post(url+'/event', json = create_event_payload)
    
    if (create_event_resp.ok):
      # Tolong request nya ngereturn id yang abis diinsert ya
      create_event_json = create_event_resp.json()
      event_id = create_event_json["id"]
      create_ticket_payload = {"event_id": event_id, "section_list": []}
      
      for section in section_list:
        create_ticket_payload["section_list"].append(
          {
            'name': section.name, 
            'capacity': section.capacity, 
            'price': section.price, 
            'has_seat': section.has_seat
          })

      print("Section list: " , create_ticket_payload)

      create_ticket_resp = requests.post(url+'/section', json = create_ticket_payload)
      if (create_ticket_request.ok):
        return True
      else:
        return False
        
    else:
      return False

    


