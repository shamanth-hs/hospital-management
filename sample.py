

from flask_restful import Resource, Api, request
from model import conn


#billInput = request.get_json(force=True)
pat_name = 'pat'
        #bill_date = bill['bill_date']
amount=25000
conn.execute('''INSERT INTO bill(pat_name,amount)
    VALUES(?,?)''', (pat_name,amount)).lastrowid
conn.commit()




