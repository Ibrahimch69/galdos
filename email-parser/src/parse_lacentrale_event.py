import json
import re
from lxml import etree


def parse_lacentrale_event(event):
    event = json.loads(event)
    print(event)
        #j'utilise re.search pour touve tout texte compris entre les caractères '<' et '>',
    from_match = re.search(r'<([^>]+)>', event['from'])
    if from_match:
        from_email = from_match.group(1)
    else:
        from_email = event['from']

    to_match = re.search(r'<([^>]+)>', event['to'])
    if to_match:
        to_email = to_match.group(1)
    else:
        to_email = event['to']

    subject_match = re.search(r"E(\d+) - ([^\r\n]+)", event['subject'])
    if subject_match:
        ad_id, ad_title = subject_match.groups()
    else:
        ad_id, ad_title = None, None

    parsed_event = {
        "channel": "lacentrale",
        "from_email": from_email,
        "to_email": to_email,
        "workspace_name": ad_title,
        "workspace_id": ad_id,
        "brand": "SEAT",  
        "model": "LEON",  
        "message": event['text'],
        "firstname": "jean-baptiste",  
        "lastname": "roi", 
        "customer_email": from_email,  
        "subject": event['subject'],
        "contact_info": [
            {
                "type": "email",
                "value": from_email
            }
        ]
    }

    return parsed_event
