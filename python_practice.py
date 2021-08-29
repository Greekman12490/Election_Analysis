print("Hello World")

counties = ["Arapahoe","Denver","Jefferson"]

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

if counties[1] == "Denver":
    print(counties[1])

if "El Paso" in counties:
    print("El Paso is in the list of counties. ")
else:
    print("El Paso is not in the list of counties. ")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties. ")
else:
    print("Arapahoe or El Paso are not in the list of counties. ")

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county, voters in counties_dict.items():
    print(county, voters)

for county, voters in counties_dict.items():
    counties_dict_info = (f'{county} county has {voters:,} registered voters')
    print(counties_dict_info)

temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC. ")
else:
    print("Open the windows. ")

#What is the score?
score = int(input("What is your test score? "))

#Determine grade

if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes. ")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes_candidate = int(input("What is the total number of votes in the election? "))
message_to_candidate = (f"You received {candidate_votes:,} number of votes. "
                        f"The total number of votes in the election was {total_votes_candidate:,}. "
                        f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes. ")

print(message_to_candidate)
                

