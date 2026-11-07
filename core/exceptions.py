from abc import ABC , abstractmethod

class GameException(Exception, ABC):
    pass

class GameOverException(GameException, ABC):
    @abstractmethod
    def show_message(self):
        pass

class WinException(GameOverException):
    def show_message(self):
        print("Победа!")

class LoseExceprion(GameOverException):
    def show_message(self):
        print("Поражение")

class TimeLimitException(GameOverException):
    def show_message(self):
        print("Время истекло!")

class InventoryFullError(GameException):
    pass

class NotEnoughManaError(GameException):
    pass

class TargetError(GameException):
    pass

class ChoiceError(GameException):
    pass

class ScriptException(Exception, ABC):
    @abstractmethod
    def show_message(self):
        pass

class OverflowLimitError(ScriptException):
    def show_message(self):
        print("Указанный параметр превышает заданую границу")
        
class NegativeValueError(ScriptException):
    def show_message(self):
        print("Значение должно быть больше или равно нуля")
