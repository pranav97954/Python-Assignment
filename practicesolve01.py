from abc import ABC ,abstractmethod
class person(ABC):
    @abstractmethod
    def setid(self,id):
        pass
class student(person):
    def setid(self,id):
        self.id=id
        print(self.id)
a=student()
a.setid(123)
