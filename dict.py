hours = {"python": 4, "gaming": 2, "gym": 0.5}
hours["ml learning"] = 6

for i,k in hours.items():
    print("you spent", k, "hours on", i )
print(hours)
print(hours.keys())
print(sum(hours.values()))