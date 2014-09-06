from sqlalchemy import schema, types, create_engine
from dbconfig import DB_URI

metadata = schema.MetaData()

User_Info_table = schema.Table('User_Info', metadata, 
                               schema.Column('user_id', types.Integer, primary_key=True),
                               schema.Column('user_phno', types.Unicode(20), default=u'', unique=True),
)

Groups_table = schema.Table('Groups', metadata, 
                               schema.Column('group_id', types.Integer, primary_key=True),
                               schema.Column('group_name', types.Unicode(255), default=u''),
                               schema.Column('user_id', types.Integer),
)
 
Group_Members_table = schema.Table('Group_Members', metadata, 
                               schema.Column('group_id', types.Integer, primary_key=True),
                               schema.Column('user_phno', types.Unicode(20), default=u''),
)

Group_Money_table = schema.Table('Group_Money', metadata, 
                               schema.Column('group_id', types.Integer, primary_key=True),
                               schema.Column('user_phno', types.Unicode(20), default=u''),
                               schema.Column('money_desc', types.Unicode(255), default=u''),
                               schema.Column('money_amount', types.Unicode(20), default=u''),
)

engine=create_engine(DB_URI, echo=False)

metadata.bind=engine

if(__name__=='__main__'):
    metadata.create_all(checkfirst=True)
