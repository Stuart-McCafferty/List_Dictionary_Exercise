users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
# 2. Get Erik's hometown
# 3. Get the list of Erik's lottery numbers
# 4. Get the species of Avril's pet Monty
# 5. Get the smallest of Erik's lottery numbers
# 6. Return an list of Avril's lottery numbers that are even
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
# 8. Change Erik's hometown to Edinburgh
# 9. Add a pet dog to Erik called "fluffy"
# 10. Add another person to the users dictionary

#Question 1 -5
print(users["Jonathan"]["twitter"])
print(users["Erik"]["home_town"])
print(users["Erik"]["lottery_numbers"])
print(users["Avril"]["pets"][0]["species"])
listSorted = (users["Erik"]["lottery_numbers"])
listSorted.sort()
print(listSorted[0])

#Question 6
avrilLottery = users["Avril"]["lottery_numbers"]
avrilEvenNumbers = []
for lottery_number in avrilLottery:
  if lottery_number % 2 == 0:
    avrilEvenNumbers.append(lottery_number)
print(avrilEvenNumbers)

#Question 7-9
users["Erik"]["lottery_numbers"] += [7]
print(users["Erik"]["lottery_numbers"])

users["Erik"]["home_town"] = "Edinburgh"
print(users["Erik"]["home_town"])

users["Erik"]["pets"] += [{"name": "fluffy", "species": "dog"}]
print(users["Erik"]["pets"])

#Question 10
users["Stuart"] = {
  "twitter": "stew_mcc",
  "lottery_numbers": [12, 14, 33, 38, 9, 25],
  "home_town": "Glasgow",
  "pets": [
      {
        "name": "ben",
        "species": "human"
      }
    ]
  }

print(users["Stuart"])