import os
import pandas as pd

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")
productId = input("Enter product id: ")

opinions = pd.read_json(f"opinions/{productId}.json")
print(opinions)