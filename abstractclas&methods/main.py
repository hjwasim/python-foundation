from abc import abstractmethod, ABC

'''
    Every car should have a company name. 
    To implement this kind of logic, we use abstract methods and class
    
    1)Every abstract class should be the child of ABC class,
    2)Abstract methods should contain @abstractmethod decorator.
      @abstractmethod
      def fun(self):
        pass - keyword must.
    3)Child class of Abstract class, must provide the implementation of abstract 
        methods.
        otherwise, it will throw error.
'''


class Car(ABC):

    @abstractmethod
    def companyName(self):
        pass


class BMW(Car):
    def companyName(self):
        print("COMPANY NAME IS BMW")


class Ferrari(Car):
    def companyName(self):
        print("COMPANY NAME IS Ferrari")


b = BMW()
b.companyName()

f = Ferrari()
f.companyName()
