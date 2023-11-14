

def data_State():
    money=0
    hungry=False
    drink=False
    snack=False

    def _init_(self,money,hungry,drink,snack):
        self.money = money

        
class State:
    def __init__(self,data):
        self.data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self,new_data):
        self._data = new_data

    def process_data(self):
        #処理
        pass