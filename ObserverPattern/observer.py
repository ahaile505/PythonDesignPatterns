from abc import ABCMeta, abstractmethod


class ISubject(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def subscribe(observer):
        pass
    
    @staticmethod
    @abstractmethod
    def unsubscribe(observer):
        pass
    
    @staticmethod
    @abstractmethod
    def notify(observer):
        pass


class IObserver(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def notify(observable, *args, **Kwargs):
        pass


class Observer(IObserver):

    def __init__(self, observable):
        observable.subscribe(self)

    def notify(self, observable, *args, **kwargs):
        print("Observer received", args, kwargs)


class Subject(ISubject):

    def __init__(self):
        self._observers = set()

    def subscribe(self, observer):
        self._observers.add(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)



def main():

    SUBJECT = Subject()

    OBSERVERA = Observer(SUBJECT)

    OBSERVERB = Observer(SUBJECT)

    SUBJECT.notify("Hello Observers")

    SUBJECT.unsubscribe(OBSERVERB)
    
    SUBJECT.notify("Hello Observers")



if __name__ == '__main__':
    main()












