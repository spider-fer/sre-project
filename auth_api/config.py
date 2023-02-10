import pymysql

def getconnection():
    return pymysql.connect(
    host= 'sre-bootcamp-selection-challenge.cabf3yhjqvmq.us-east-1.rds.amazonaws.com', 
    port = 3306,
    user = 'secret', 
    password = 'jOdznoyH6swQB9sTGdLUeeSrtejWkcw',
    db = 'bootcamp_tht',  
)

SECRET_KEY = 'my2w7wjd7yXF64FIADfJxNs1oupTGAuW'