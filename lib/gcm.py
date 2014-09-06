import requests
import json

def send_gcm(action, params, rid):
    try:
        url = 'https://android.googleapis.com/gcm/send'
        authkey="AIzaSyAdMgoeDcpmSi4IG7ncdFr1cHK8u-xX_-4"
        rid_list=[rid]

        headers = {'content-type': 'application/json', 'Authorization':"key="+ authkey}
        payload={"registration_ids":rid_list, "data" : {"action":action, "params":json.dumps(params),},}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        if(r.status_code != requests.codes.ok or 1):
            print r.json()
            try:
                if(r.json()['success']==len(rid_list)):
                    return 1
                else:
                    return 0
            except:
                return 0;
        else:
            return 0
    except:
        return -1

if __name__=='__main__':
    print send_gcm("lol", "something", 'APA91bGuqEQnJ6BJX_SbHTBm5u_GnLebHGjNAFUxixUG460-l0axMmJ39WHSM4v5CFUNOgSBcd-0vE6SpO8z2ZQ5OQE23yXVq1uY9fJ2B0_qM1FsGfSbg0icrsvfxw_l2Ts_6jOvn1yuP6roGKecDDnmRHtVkxUUog')
