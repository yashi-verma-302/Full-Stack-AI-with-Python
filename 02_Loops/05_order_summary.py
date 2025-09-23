names = ["abc", "xyz", "who"]
bills = [50, 70, 130]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")