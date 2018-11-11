from spyne.decorator import rpc 
from spyne.model.complex import Iterable
from spyne.model.primitive import Unicode, Boolean, Integer
from spyne.service import ServiceBase
from datetime import datetime
import requests

class BookEventService(ServiceBase):
  @rpc(Integer, Integer, Iterable(Integer), _returns=Integer)
  def BookEvent(ctx,user_id,event_id, section_id_list):
    ticket_url = ctx.ticket_url
    payment_url = ctx.payment_url
    get_event_resp = requests.get(ticket_url+'/event/'+event_id)
    if (get_event_resp.ok):
      event_json = get_event_resp.json()
      create_order_payload = {'user_id' : user_id, 'event_id': event_id, 'section_id_list': section_id_list}
      create_order_resp = requests.post(ticket_url+'/order', json=payload)
      if (create_order_resp.ok):
        order_json = create_order_resp.json()
        create_invoice_payload = {'order_id': order_json["id"], 'price': order_json["total_price"]}
        create_invoice_resp = requests.post(payment_url+'/invoice', json=create_invoice_payload)
        if (create_invoice_resp.ok):
          invoice_json = create_invoice_resp.json()
          return invoice_json["id"]

      else:
        return -1

    else:
      return -1
  
  @rpc(Integer, _returns=Boolean)
  def ConfirmPayment(ctx,order_id):
    ticket_url = ctx.ticket_url
    payload = {'status': "paid"}
    update_event_resp = requests.put(ticket_url+'/event/'+order_id, json=payload)
    if (update_event_resp.ok):
      return True
    else :
      return False




    

    


