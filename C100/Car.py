# C100--- python classes

class Car(object):
    """
      blueprint for car
    """

    def __init__(self, modelInput, colorInput, companyInput, speed_limitInput):
        self.color = colorInput
        self.company = companyInput
        self.speed_limit = speed_limitInput
        self.model = modelInput

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelarate(self):
        print("accelarating...")
        "accelarator functionality here"

    def change_gear(self, gear_type):
        print("gear changed")
        " gear related functionality here"


audi = Car("A6", "red", "audi", 80)

print(audi.start())
