class Account:
  def __init__(self,ano,owner,balance):
    self.ano = ano
    self.owner = owner
    self.__balance = balance
  
  def deposit(self, amount):
    if self.__balance + amount >= 10000000:
      print('천만원 이상은 갖고 있을 수 없습니다.')
      return
    self.__balance += amount
    print(f'계좌에 {self.__balance}원 남았습니다.')
  
  def withdraw(self, amount):
    if self.__balance < amount:
      print('잔액이 부족합니다.')
      return
    self.__balance -= amount
    print(f'계좌에 {self.__balance}원 남았습니다.')
  
  def __str__(self):
    return f'계좌번호 : {self.ano}, name : {self.owner}, 잔액 : {self.__balance:9,d}'