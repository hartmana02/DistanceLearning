import matplotlib.pyplot as plt
import pandas as pd

countries = ["US", "Spain", "Italy", "United Kingdom", "France", "Russia", "Iceland", "China", "India", "Korea, South"]
days = []
for x in range(104):
    days.append(x)

df = pd.read_csv("covid19_data.csv", header=0)

unique_countries = df["Country"].unique()

for c in unique_countries:
    if c in countries: 
        confirmed_cases = df[df["Country"] == c]["Confirmed"]

        plt.plot(days, confirmed_cases, label=c, linestyle="dashed")

plt.ylabel("Confirmed Cases (Logarithmic Scale)")
plt.yscale("log")
plt.xlabel("Days Since January 22nd, 2020")
plt.title("Confirmed Cases of Covid-19 by Country")
plt.legend()
plt.show()