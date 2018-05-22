#题目1：请定义关于 airplanes（飞机）和flights（航班）的两个类，以下给出了类Airplane的一部分，包括描述性的文档字符串。
class Airplane:
    """ 关于特定飞机的信息，包括型号、序列号、座位数量和行驶里程。"""
##    model = ''
##    serial = ''
##    seats = 0
##    miles = 0.0
#(1) 完成Airplane类的初始化函数__init__。
    def __init__(self, plane_model, serial_num, num_seats, miles_travelled):
        """ 初始化函数，调用形式为 (Airplane, str, str, int, float)，用来记录飞机的型号（model）、序列号（serial）、座位数（seats ）和行驶里程（miles）。 """
        self.model = plane_model
        self.serial = serial_num
        self.seats = num_seats
        self.miles = miles_travelled
#(2) 这里给出了类Airplane中的log_trip（记录行程）方法的函数头、类型和描述，请你完成该方法的定义。并请增加一个例子用于创建一个Airplane对象，记录一趟行程为1000英里的行程。
    def log_trip(self, num_miles):
        """调用形式为(Airplane, float) -> NoneType
        前提条件是参数 num_miles > 0.0
        本方法用于记录飞机新近一趟行程的长度。
        具体创建与使用方式如下：
        >>> airplane = Airplane(‘Boeing 747’, ‘19643’, 366, 45267.7)
        >>> airplane.log_trip(1000.0)
        >>> airplane.miles
        46267.7
        """
        self.miles += num_miles
        
#(3) 请为类Airplane增加一个__eq__方法，用来判断给定的两个Airplane对象是否相等，判断的依据是如果两个Airplane对象的序列号相等，我们就认为这两个对象是相等的，即__eq__返回True。
    def __eq__(self, other):
        """ (Airplane, Airplane) -> bool
        判断这架飞机和另外一架是否相同.
        >>> a1 = Airplane(‘Boeing 747’, ‘19643’, 366, 45267.7)
        >>> a2 = Airplane(‘Boeing 747’, ‘19643’, 366, 45267.7)
        >>> a3 = Airplane(‘Boeing 747’, ‘20536’, 366, 45267.7)
        >>> a1 == a2
        True
        >>> a1 == a3
        False
        """
        if int(self.serial) == int(other.serial):
            return True
        else:
            return False
        
class Flight(Airplane):
    """关于特定航班的信息. """
##    passenger_cnt = 0
#(4) 完成类Flight中的__init__方法,并另外定义一个conversion方法。
    def __init__(self,plane):
        """ (Flight, Airplane) -> NoneType(即返回值为空)
        创建一个航班,其中指明特定飞机上的乘客为空列表.例如,
        >>> a = Airplane(‘Boeing 747’, ‘19643’, 366, 45267.7)
        >>> f = Flight(a)
        >>> f.conversion()
        Airplane(‘Boeing 747’, ‘19643’, 366, 45267.7)
        >>> f.passengers
        []
        """
        Airplane.__init__(self,plane.model, plane.serial,plane.seats, plane.miles)
        self.passengers = []
    def conversion(self, plane):
        """ 返回类Airplane的对象的字符串表示形式,如 
        'Airplane(Boeing 747, 19643, 366, 45267.7)' ."""
        return  'Airplane('+'%s'%plane.model+','+'%s'%plane.serial+','+'%s'%plane.seats+','+'%s'%plane.miles+')'

#(5) 完成类Flight的add方法。
    def add(self, passenger):
        """ (Flight, str) -> bool
        如果本架航班上仍然有空位，则将乘客加入到航班的乘客列表中；如果添加了乘客，则返回True，否则为False.
        >>> a = Airplane(‘Cessna 150E’, ‘9378’, 1, 824.8)
        >>> f = Flight(a)
        >>> f.add(‘Myrto’)
        True
        >>> f.add(‘Jen’)
        False
        """
        if len(self.passengers) < self.seats:
            self.passengers.append(passenger)
            return True
        else:
            return False

#(6) 完成类Flight的change_planes方法。
    def change_planes(self, other_airplane):
        """ (Flight, Airplane) -> bool
        如果另外一架飞机能够容纳本架飞机的所有乘客，那么使用另外一架飞机。无论我们是否将乘客换到另外一架飞机上，均返回目前本架飞机上的空余座位数目。
        >>> a1 = Airplane(‘Boeing 747’, ‘19643’, 366, 45267.7)
        >>> f = Flight(a1)
        >>> f.add(‘Myrto’)
        True
        >>> f.add(‘Jen’)
        True
        >>> a2 = Airplane(‘Bombardier Dash 8’, ‘11234’, 39, 6444.6)
        >>> f.change_planes(a2)
        366
        >>> a3 = Airplane(‘Cessna 150E’, ‘9378’, 1, 824.8)
        >>> f.change_planes(a3)
        364
        """
        if other_airplane.seats >= len(self.passengers):
            return self.seats
        else:
            return self.seats-len(self.passengers)



if __name__ == "__main__":	
    airplane = Airplane('Boeing 747', '19643', 366, 45267.7)
    print(airplane.log_trip(1000.0))
    print(airplane.miles)
    
    a1 = Airplane('Boeing 747','19643', 366, 45267.7)
    a2 = Airplane('Boeing 747','19643', 366, 45267.7)
    a3 = Airplane('Boeing 747','20536', 366, 45267.7)
    print(a1.__eq__(a2))
    
    a = Airplane('Boeing 747','19643', 366, 45267.7)
    f = Flight(a)
    print(f.conversion(a))
    
    Airplane('Boeing 747','19643', 366, 45267.7)
    print(f.passengers)

##    print(a1.__dict__)
    a = Airplane('Cessna 150E', '9378', 1, 824.8)
    f = Flight(a)
    print(f.add('Myrto'))
    print(f.add('Jen'))

    a1 = Airplane('Boeing 747', '19643', 366, 45267.7)
    f = Flight(a1)
    f.add('Myrto')
    f.add('Jen')
    a2 = Airplane('Bombardier Dash 8', '11234', 39, 6444.6)
    print(f.change_planes(a2))
    a3 = Airplane('Cessna 150E', '9378', 1, 824.8)
    print(f.change_planes(a3))

          
