import json
import re
from lxml import etree

def parse_leboncoin_event(event):

    msg = email.message_from_string(event)
    # je recupere les info qui corsponde dans le jso et je l'ai stock dans des variables
    subject = msg["subject"]
    to_email = msg["to"]
    from_email = msg["from"]

    # je recupere le corp du message et je dois recupere les info qui m'interesse 
    text = ""

    result = {
        "channel": "leboncoin",
        "from_email": from_email,
        "to_email": to_email,
        "workspace_name": "abc",
        "workspace_id": "ab77535e-6fe7-4b44-82bb-64c6f82ef5a4",
        "brand": "Mazda",
        "model": "CX-3 2.0L Skyactiv-G 120 4x2 Signature",
        # "firstname": ,
        # "lastname": ,
        # "customer_phone_number": ,
        # "links": {
        #     "lead": 
        # },
        "subject": subject,
        "contact_info": [
            {
                "type": "email",
                # "value": 
            },
            {
                "type": "phone_number",
                # "value": customer_phone_number
            }
        ]
    }

    return result
