"""x = "vineel"

def globalvi():
  print("my name is " + x)

globalvi()"""
def globalvi():
  global x
  x =str(input("write anything\n"))

globalvi()

print("Python is " + x)