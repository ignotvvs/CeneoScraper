import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")
productId = input("Enter product id: ")

opinions = pd.read_json(f"opinions/{productId}.json")
opinions["stars"] = opinions["stars"].map(lambda x: float(x.split("/")[0].replace(",",".")))

opinions_count = len(opinions)
pros_count = opinions["pros"].map(bool).sum()
cons_count = opinions["cons"].map(bool).sum()
average_score = opinions["stars"].mean().round(2)

recommendation = opinions["recommendation"].value_counts(dropna=False).sort_index().reindex(["Nie polecam","Polecam", None],fill_value = 0)
recommendation.plot.pie(
    label="",
    autopct =  lambda p: '{:.1f}%'.format(round(p)) if p > 0 else '',
    colors = ["crimson", "forestgreen", "grey"],
    labels = ["Nie polecam", "Polecam", "Nie mam zdania"]
)
plt.title("Rekomendacje")
plt.savefig(f"plots/{productId}_recommendations.png")
plt.close()

stars = opinions["stars"].value_counts().sort_index().reindex(list(np.arange(0,5.5,0.5)),fill_value = 0)
stars.plot.bar(
    color = "pink"
)
plt.title("Oceny produktu")
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
plt.grid(True, axis="y")
plt.xticks(rotation=0)
plt.savefig(f"plots/{productId}_stars.png")
plt.close()