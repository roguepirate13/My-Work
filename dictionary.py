pass_per = {}


def read_data():
    n = int(input("Enter Total number of semesters = "))
    for i in range(n):
        print("Enter Semester name and Percentage sepa"
              "rated by Space]")
        text = input().split()
        pass_per[text[0]] = text[-1]


def display_data():
    s_pass_per = pd.Series(pass_per)
    print(type(s_pass_per))
    print("Displaying dictionary using pandas Series:\n", s_pass_per)

    print("The dictionary output:\n", pass_per)


read_data()
display_data()
