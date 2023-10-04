from battery.ibattery import Ibattery
from utils import check_date


class NubbinBattery(Ibattery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        date_of_serviced = check_date(self.last_service_date, 4)
        if date_of_serviced < self.current_date:
            return True
        else:
            return False
