x = 0
while x <= 5:
    print(x)
    x = x + 1


count = 7

while count < 1:

    print("Hello World")

for county in counties:
    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)


