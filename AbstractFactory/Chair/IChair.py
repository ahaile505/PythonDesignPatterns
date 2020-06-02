from abc import ABCMeta, abstractstaticmethod


class IChair(metaclass = ABCMeta):

    @abstractstaticmethod
    def dimensions():
        pass