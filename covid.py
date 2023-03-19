import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    new_cases = {}
    for row in reader:
        state = row["state"]
        cases = int(row["cases"])
        if state not in new_cases:
            new_cases[state] = [cases]
        else:
            new_cases[state].append(cases - new_cases[state][-1])
        if len(new_cases[state]) > 14:
            new_cases[state].pop(0)  #removing the first array element.
    return new_cases


# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    for state in states:
      try: 
            cases_last_week = sum(new_cases[state][:7])
            cases_this_week = sum(new_cases[state][7:])
            avg_last_week = cases_last_week / 7
            avg_this_week = cases_this_week / 7
            print(f"{state}: {avg_this_week:.2f} (vs. {avg_last_week:.2f} last week)")
      except ZeroDivisionError:
            avg_last_week = 0
            avg_this_week = 0
            
if __name__ == "__main__":
      main()
