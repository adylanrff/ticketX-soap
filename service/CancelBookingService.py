from spyne.decorator import rpc 
from spyne.model.complex import Array
from spyne.model.primitive import Boolean, Integer
from spyne.service import ServiceBase
from datetime import datetime
import requests

class CancelBookingService(ServiceBase):
  @rpc(Integer,_returns=Boolean)
  def CancelTicket(ctx,invoice_id):
    url = ctx.ticket_url;
    payload = {'status': 'canceled'}
    cancel_booking_resp = requests.put(url+'/invoice/'+invoice_id, data = payload)
    if (cancel_booking_resp.ok):
      return True
    else:
      return False

    


