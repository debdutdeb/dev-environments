from abc import ABC, abstractmethod


class Store(ABC):

    @abstractmethod
    def new_environment(self):
        pass

    @abstractmethod
    def remove_environment(self):
        pass

    @abstractmethod
    def find_environment(self):
        pass

    @abstractmethod
    def update_environment(self):
        pass
