

from flask_restful import Resource, Api, request
from model import conn




class bills(Resource):
    """It contain all the api carryign the activity with aand specific bill"""

    def get(self):
        """Api to retive all the bill from the database"""

        bills = conn.execute("SELECT * FROM bill  ORDER BY bill_date DESC").fetchall()
        return bills



    def post(self):
        """api to add the bill in the database"""

        billInput = request.get_json(force=True)
        pat_name=billInput['pat_name']
        amount = billInput['amount']
        bill_date = billInput['bill_date']
        billInput['bill_id']=conn.execute('''INSERT INTO bill(pat_name,amount)
            VALUES(?,?)''', (pat_name,amount)).lastrowid
        conn.commit()
        return billInput

class bill(Resource):
    """It contains all apis doing activity with the single bill entity"""

    def get(self,id):
        """api to retrive details of the bill by it id"""

        bill = conn.execute("SELECT * FROM bill WHERE bill_id=?",(id,)).fetchall()
        return bill

    def delete(self,id):
        """api to delete the patiend by its id"""

        conn.execute("DELETE FROM bill WHERE bill_id=?",(id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,id):
        """api to update the bill by it id"""

        billInput = request.get_json(force=True)
        pat_name=billInput['pat_name']
        amount = billInput['amount']
        bill_date = billInput['bill_date']
        #bill_id = billInput['bill_id']
        #pat_address = billInput['pat_address']
        conn.execute("UPDATE bill SET pat_name=?,amount=? WHERE bill_id=?",
                     (pat_name,amount,id))
        conn.commit()
        return billInput
