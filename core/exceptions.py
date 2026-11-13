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

class InventortyException(GameException, ABC):
    @abstractmethod
    def show_message(self):
        pass

class InventoryFullException(InventortyException):
    def show_message(self):
        print("Инвентарь переполнен!")

class ItemNotFoundException(InventortyException):
    def show_message(self):
        print("Предмет не найден!")

class ItemNotEquippableException(InventortyException):
    def show_message(self):
        print("Данный предмет нельзя экировать этим классом")

class EquipmentSlotOccupiedException(InventortyException):
    def show_message(self):
        print("Слот уже занят")

class ItemDurabilityZeroException(InventortyException):
    def show_message(self):
        print("Предмет сломан")

class StackLimitException(InventortyException):
    def show_message(self):
        print("Превышен лимит стака")

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

class CombatException(GameException, ABC):
    @abstractmethod
    def show_message(self):
        pass

class AttackNotReadyException(CombatException):
    def show_message(self):
        print("Атака на перезарядке!")

class OutOfAmmoException(CombatException):
    def show_message(self):
        print("Нет боеприпасов!")

class InvalidTargetException(CombatException):
    def show_message(self):
        print("Цель мертва/вне зоны")

class AbilityNotLearnedException(CombatException):
    def show_message(self):
        print("Способность не изучена!")

class AbilityOnCooldownException(CombatException):
    def show_message(self):
        print("Способность на перезарядке!")

class StatusEffectException(CombatException):
    def show_message(self):
        print("Ошибка эффектов")

class BuffConflictException(CombatException):
    def show_message(self):
        print("Конфликт баффов")

class CriticalHitException(CombatException):
    def show_message(self):
        print("Нанесён критический урон!")

