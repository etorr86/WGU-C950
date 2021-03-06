import datetime
from Utils import TruckStatus


# package class, it acts as a model to use for the packages.
class Packages:
    def __init__(self,
                 package_key=None,
                 package_address=None,
                 package_city=None,
                 package_state=None,
                 package_zip_code=None,
                 package_delivery_time=None,
                 package_weight=None,
                 package_notes=None):
        self._packageKey = package_key
        self._packageAddress = package_address
        self._packageCity = package_city
        self._packageState = package_state
        self._packageZipCode = package_zip_code
        self._packageDeliveryTime = package_delivery_time
        self._packageWeight = package_weight
        self._packageNotes = package_notes
        self._status = TruckStatus.atHub
        self._truck = None
        self._deliveredAt = datetime.timedelta()

    def package_key(self):
        return self._packageKey

    def package_address(self):
        return self._packageAddress

    def set_package_addr(self, addr):
        self._packageAddress = addr

    def package_city(self):
        return self._packageCity

    def set_package_city(self, city):
        self._packageCity = city

    def package_state(self):
        return self._packageState

    def set_package_state(self, state):
        self._packageState = state

    def package_zip_code(self):
        return self._packageZipCode

    def set_package_zip(self, zipCode):
        self._packageZipCode = zipCode

    def package_delivery_time(self):
        return self._packageDeliveryTime

    def package_weight(self):
        return self._packageWeight

    def package_notes(self):
        return self._packageNotes

    def full_address(self):
        return self._packageAddress + " " + self._packageCity + " " + self._packageState + " " + self._packageZipCode

    def status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def delivered_at(self):
        return self._deliveredAt

    def set_truck_id(self, truckid):
        self._truck = truckid

    def get_truck_id(self):
        return self._truck

    def set_package_delivery_time(self, time):
        self._deliveredAt = time
        return self._deliveredAt

    # This is useful for testing purposes
    def __repr__(self):
        template = "'{0._packageKey}', '{0._packageAddress}', '{0._packageCity}', " \
                   "'{0._packageState}', '{0._packageZipCode}', '{0._packageDeliveryTime}', " \
                   "'{0._packageWeight}', '{0._packageNotes}'"
        return template.format(self)
