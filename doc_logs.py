

from flask_restful import Resource, Api, request
from model import conn
class doc_logss(Resource):
    """This contain apis to carry out activity with all doc_logss"""

    def get(self):
        """Retrive list of all the doc_logs"""

        doc_logss = conn.execute("SELECT * FROM doc_logs ORDER BY doc_name DESC").fetchall()
        return doc_logss



    
class doc_logs(Resource):
    """It include all the apis carrying out the activity with the single doc_logs"""


    def get(self,id):
        """get the details of the docktor by the doc_logs id"""

        doc_logs = conn.execute("SELECT * FROM doc_logs WHERE doc_id=?",(id,)).fetchall()
        return doc_logs

    
