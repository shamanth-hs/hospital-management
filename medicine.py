

from flask_restful import Resource, Api, request
from model import conn
class medicines(Resource):
    """This contain apis to carry out activity with all medicines"""

    def get(self):
        """Retrive list of all the medicine"""

        medicines = conn.execute("SELECT * FROM medicine ORDER BY med_id DESC").fetchall()
        return medicines



    def post(self):
        """Add the new medicine"""

        medicineInput = request.get_json(force=True)
        #med_id=medicineInput['med_id']
        medicine_name = medicineInput['medicine_name']
        desease = medicineInput['desease']
        pat_name = medicineInput['pat_name']
        medicineInput['med_id']=conn.execute('''INSERT INTO medicine(medicine_name,desease,pat_name)
            VALUES(?,?,?)''', (medicine_name,desease,pat_name)).lastrowid
        conn.commit()
        return medicineInput

class medicine(Resource):
    """It include all the apis carrying out the activity with the single medicine"""


    def get(self,id):
        """get the details of the docktor by the medicine id"""

        medicine = conn.execute("SELECT * FROM medicine WHERE med_id=?",(id,)).fetchall()
        return medicine

    def delete(self, id):
        """Delete the medicine by its id"""

        conn.execute("DELETE FROM medicine WHERE med_id=?", (id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,id):
        """Update the medicine by its id"""

        medicineInput = request.get_json(force=True)
        medicine_name = medicineInput['medicine_name']
        desease = medicineInput['desease']
        pat_name = medicineInput['pat_name']
        conn.execute(
            "UPDATE medicine SET medicine_name=?,desease=?,pat_name=? WHERE med_id=?",
            (medicine_name,desease,pat_name, id))
        conn.commit()
        return medicineInput
