

class Jar:
    def __init__(self, capacity=12):
      self._capacity = capacity

    def __str__(self):
      return str(self.capacity)

    def deposit(self, n):
      self._capacity += n

    def withdraw(self, n):
      if self.capacity < n:
         print("Not enough in jar")
      else:
         self._capacity -= n

    @property
    def capacity(self):
      return self._capacity

    @property
    def size(self):
      return len(self.capacity)
    
def main():
      jar = Jar()
      print(str(jar.capacity))
      jar.deposit(5)
      print(str(jar))
      jar.withdraw(2)
      print(str(jar))
      jar.withdraw(20)
      print(str(jar))

if __name__ == "__main__":
  main()