import abc

class Generator(abc.ABC):
    @abc.abstractmethod
    def gen(self) -> list: pass
