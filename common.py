

from flask_restful import Resource, Api, request
from model import conn


class Common(Resource):
    """This contain common api ie noe related to the specific module"""

    def get(self):
        """Retrive the patient,doctor and appointment count for the dashboard page"""

        getPatientCount=conn.execute("SELECT COUNT(*) AS patient FROM patient").fetchone()
        getDoctorCount = conn.execute("SELECT COUNT(*) AS doctor FROM doctor").fetchone()
        getAppointmentCount = conn.execute("SELECT COUNT(*) AS appointment FROM appointment").fetchone()
        getMedicineCount=conn.execute("select count(*) as medicine from medicine").fetchone()
        getbillCount=conn.execute("select count(*) as bill from bill").fetchone()
        getPatientCount.update(getDoctorCount)
        getPatientCount.update(getAppointmentCount)
        getPatientCount.update(getMedicineCount)
        getPatientCount.update(getbillCount)
        return getPatientCount
