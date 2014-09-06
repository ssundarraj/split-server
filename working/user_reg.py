from sqlalchemy import *
from lib.metadata import engine, User_Info_table
import json

def new_user_phno(details):
    conn=engine.connect()
                                                  
    #check if phno is unique
    sel_q = select([User_Info_table]).where(User_Info_table.c.user_phno == details['user_phone'])
    sel_result=conn.execute(sel_q)
    if len(sel_result.fetchall()):
        conn.close()
        return 0; #returns 0 if phno is not unique
    ins_q = User_Info_table.insert(values= dict(user_phno=details['user_phone']))
    result=conn.execute(ins_q)
    conn.close()
    if(result.inserted_primary_key[0] if result.is_insert else id_):
        return result.inserted_primary_key[0]
    else:
        return 0

if __name__ == '__main__':
    print new_user_phno(json.loads(json.dumps({"user_phone":"+919609063014"})))
