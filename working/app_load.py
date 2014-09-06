from sqlalchemy import *
from lib.metadata import engine, User_Info_table, Groups_table, Group_Members_table, Group_Money_table
import json

def load_groups(details):
    conn=engine.connect()
    sel_q = select([Groups_table.c.group_name,
                    Groups_table.c.group_id,]).where(Groups_table.c.user_id == details['user_id'])
    result=conn.execute(sel_q)
    rows=result.fetchall()
    ret_data = [dict(i) for i in rows]

    sel_q = select([Group_Members_table.c.group_id,
                    Groups_table.c.group_name,]).where(and_(
                        Groups_table.c.group_id == Group_Members_table.c.group_id,
                        Group_Members_table.c.user_phno==details['user_phone']))
    result=conn.execute(sel_q)
    rows=result.fetchall()
    ret_data.extend([dict(i) for i in rows])
    
    conn.close()
    return ret_data

def load_groupdata(details):
    conn=engine.connect()
    sel_q = select([Group_Money_table.c.user_phno,
                    Group_Money_table.c.money_desc,
                    Group_Money_table.c.money_amount,]).where(Group_Money_table.c.group_id == details['group_id'])
    result=conn.execute(sel_q)
    rows=result.fetchall()
    ret_data = [dict(i) for i in rows]
##UNTESTED    
    conn.close()
    return ret_data


if __name__ == '__main__':
    print load_groupdata(json.loads(json.dumps({'group_id':'1', 'user_phone':'1234'})))
