from sqlalchemy import *
from lib.metadata import engine, User_Info_table, Groups_table, Group_Members_table, Group_Money_table
import json

def new_group(details):
    conn=engine.connect()
                                                  
    ins_q = Groups_table.insert(values= dict(user_id=details['user_id'],
                                              group_name=details['group_name'],))
    result=conn.execute(ins_q)
    conn.close()
    if(result.inserted_primary_key[0] if result.is_insert else id_):
        return result.inserted_primary_key[0]
    else:
        return 0

def new_group_member(details):
    conn=engine.connect()
                                                  
    ins_q = Group_Members_table.insert(values= dict(group_id=details['group_id'],
                                              user_phno=details['user_phone'],))
    result=conn.execute(ins_q)
    conn.close()
    if(result.inserted_primary_key[0] if result.is_insert else id_):
        return result.inserted_primary_key[0]
    else:
        return 0

def new_expense(details):
    conn=engine.connect()
                                                  
    ins_q = Group_Money_table.insert(values= dict(group_id=details['group_id'],
                                                   money_amount=details['amount'],
                                                   money_desc=details['desc'],
                                                   user__phno=details['user_phone'],
    result=conn.execute(ins_q)
    conn.close()
    if(result.inserted_primary_key[0] if result.is_insert else id_):
        return result.inserted_primary_key[0]
    else:
        return 0


if __name__ == '__main__':
    print new_group(json.loads(json.dumps({"user_id":"1", "group_name":"test"})))
