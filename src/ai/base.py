from abc import ABC, abstractmethod

class AIEngine(ABC):
    @abstractmethod
    def ask(self, question: str) -> str:
        pass
