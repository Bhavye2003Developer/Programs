class Employee:
    __name = None
    __Roll = None
    def __init__(self,name,roll) -> None:
        self.__name = name
        self.__Roll = roll
    def show_info(self) -> None:
        print(f"Your name : {self.__name}")
        print(f"Your Roll number : {self.__Roll}")