# error.py

def crash():
    print("Crashing now...")
    return 1 / 0  # ZeroDivisionError

crash()
