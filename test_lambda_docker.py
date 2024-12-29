import requests
import json


site = {'site': {'having_ip_address': -1,
 'url_length': -1,
 'shortining_service': 1,
 'having_at_symbol': 1,
 'double_slash_redirecting': 1,
 'prefix_suffix': -1,
 'having_sub_domain': 1,
 'sslfinal_state': -1,
 'domain_registeration_length': 1,
 'favicon': 1,
 'port': 1,
 'https_token': 1,
 'request_url': -1,
 'url_of_anchor': -1,
 'links_in_tags': 0,
 'sfh': 1,
 'submitting_to_email': 1,
 'abnormal_url': 1,
 'redirect': 0,
 'on_mouseover': 1,
 'rightclick': 1,
 'popupwidnow': 1,
 'iframe': 1,
 'age_of_domain': -1,
 'dnsrecord': 1,
 'web_traffic': -1,
 'page_rank': -1,
 'google_index': 1,
 'links_pointing_to_page': 1,
 'statistical_report': 1}}
site = json.dumps(site)

url = 'http://localhost:9696/2015-03-31/functions/function/invocations'
response = requests.post(url, json=site)
result = response.json()

print(json.dumps(result, indent=2))
