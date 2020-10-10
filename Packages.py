import datetime


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
        self._status = 'At Hub'
        self._deliveredAt = datetime.timedelta()

    def package_key(self):
        return self._packageKey

    def package_address(self):
        return self._packageAddress

    def package_city(self):
        return self._packageCity

    def package_state(self):
        return self._packageState

    def package_zip_code(self):
        return self._packageZipCode

    def package_delivery_time(self):
        return self._packageDeliveryTime

    def package_weight(self):
        return self._packageWeight

    def package_notes(self):
        return self._packageNotes

    def full_address(self):
        return self._packageAddress + " " + self._packageCity + " " + self._packageState

    def status(self):
        return self._status

    # This is useful for testing purposes
    def __repr__(self):
        template = "'{0._packageKey}', '{0._packageAddress}', '{0._packageCity}', " \
                   "'{0._packageState}', '{0._packageZipCode}', '{0._packageDeliveryTime}', " \
                   "'{0._packageWeight}', '{0._packageNotes}'"
        return template.format(self)
