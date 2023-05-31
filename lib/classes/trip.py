
class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        visitor.national_parks(national_park)
        visitor.trips(self)
        
        national_park.visitors(visitor)
        national_park.trips(self)

        Trip.all.append(self)


    def visitor(self, visitor=None):
        from classes.visitor import Visitor
        if visitor and isinstance(visitor, Visitor):
            self.visitor = visitor
        else:
            raise Exception
        return self.visitor
    
    def national_park(self, national_park=None):
        from classes.national_park import NationalPark
        if national_park and isinstance(national_park, NationalPark):
            self.national_park = national_park
        else:
            raise Exception
        return self.national_park