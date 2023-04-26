import requests
 
 
def handle_no_ban():
    print('No bans detected')
 
 
def handle_ban(body_json):
    ban_count = len(body_json['bans'])
    can_appeal = body_json['canAppeal']
    ban_info = body_json['bans']
    print('Ban count: ' + str(ban_count))
    print('Can appeal: ' + str(can_appeal))
    print('Ban info: ' + str(ban_info))
 
 
if __name__ == '__main__':
    SSO_TOKEN = '' # SET SSO TOKEN HERE
 
    response = requests.get('https://prod-psapi.infra-ext.activision.com/api/bans/appeal', cookies={'ACT_SSO_COOKIE': SSO_TOKEN})
 
    if response.status_code != 200:
        raise Exception('Non-200 status returned: ' + str(response.status_code))
 
    body = response.json()
    ban_count = len(body['bans'])
    if (ban_count == 0):
        handle_ban(body)
    else:
        handle_no_ban()
