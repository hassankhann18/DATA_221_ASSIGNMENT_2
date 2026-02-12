# NAME: HASSAN ADNAN
# UCID: 30217418
# QUESTION 6

import pandas as pd

def main():
    df = pd.read_csv("crime.csv")

    df["risk"] = "LowCrime"
    df.loc[df["ViolentCrimesPerPop"] >= 0.50, "risk"] = "HighCrime"

    average_unemployment = df.groupby("risk")["PctUnemployed"].mean()

    print("Average Unemployment Rate using Risk Group: ")
    print("HighCrime ->", average_unemployment["HighCrime"])
    print("LowCrime ->", average_unemployment["LowCrime"])

if __name__ == "__main__":
    main()


