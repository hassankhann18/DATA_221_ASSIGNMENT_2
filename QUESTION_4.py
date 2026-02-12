# NAME: HASSAN ADNAN
# UCID: 30217418
# QUESTION 4

import pandas as pd

def main():

    df = pd.read_csv("student.csv")

    filtered = df [
        (df["studytime"] >= 3) &
        (df["internet"] == 1) &
        (df["absences"] <= 5)
    ]

    filtered.to_csv("high_engagement.csv", index=False)  # Saving filtered data

    number_students = len(filtered)
    print("The number of students is : ", number_students)

    average_grade = filtered["grade"].mean()
    print("The average grade is : ", average_grade)

if __name__ == "__main__":
    main()






