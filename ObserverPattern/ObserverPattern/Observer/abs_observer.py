from abc import ABCMeta, abstractmethod


class AbsObserver(metaclass=ABCMeta):

    def update(self, value):
        pass
