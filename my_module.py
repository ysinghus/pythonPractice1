def hello():
    print("Hello from my_module!")
    
if __name__ == "__main__":
    print("my_module is being run directly")
    hello()
else:
    print(f"my_module has been imported. Current __name__ is: ",__name__)