value = 13
if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")
    
available_sizes = ["small", "medium", "large"]
if (requested_size := input("Enter your chai cup size")) in available_sizes:
    print(f"Serving {requested_size} chai")
else:
    print(f"Size is unavailable - {requested_chai}")

 