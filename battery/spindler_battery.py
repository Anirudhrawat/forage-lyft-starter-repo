from battery.ibattery import Ibattery
from utils import check_date


class SpindlerBattery(Ibattery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        date_of_service = check_date(self.last_service_date, 2)
        if date_of_service < self.current_date:
            return True
        else:
            return False
