from iservice import Iservice


class Service(Iservice):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    
    def needs_service(self):
        return self.engine.needs_service() or self.battery.need_Service()
