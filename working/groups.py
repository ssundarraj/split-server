from sqlalchemy import *
from lib.metadata import engine, Groups_table, Group_Members_table, Group_Money_table
import json

def new_group(details):
    conn=engine.connect()
                                                  
    ins_q = Groups_table.insert(values= dict(group_name=details['user_phno'],
                                              group_name=details['group_name'],))
    result=conn.execute(ins_q)
    conn.close()
    if(result.inserted_primary_key[0] if result.is_insert else id_):
        return result.inserted_primary_key[0]
    else:
        return 0

def add_to_group(details):
    conn=engine.connect()
                                                  
    ins_q = Groups_Members_table.insert(values= dict(group_name=details['group_id'],
                                              user_phno=details['user_phone'],))
    result=conn.execute(ins_q)
    conn.close()
    if(result.inserted_primary_key[0] if result.is_insert else id_):
        return result.inserted_primary_key[0]
    else:
        return 0


if __name__ == '__main__':
    print new_user_phno(json.dumps({"user_phone":"+919600063014"}))
