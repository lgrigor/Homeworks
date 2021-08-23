# Exercise 1: Below are the two lists convert it into the dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Expected output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

x = dict(zip(keys, values))

print("Exercise 1, output:", x)

# Exercise 2: Create a new dictionary with the following keys from a below dictionary

# Given dictionary: sampleDict = {
#        "name": "Kelly",
#        "age":25,
#        "salary": 8000,
#        "city": "New york"
# }
# Keys: "name", "salary"

# Expected output: {'name': 'Kelly', 'salary': 8000}

sampleDict = {
       "name": "Kelly",
       "age":25,
       "salary": 8000,
       "city": "New york"
}

x = {"name": sampleDict["name"], "salary": sampleDict["salary"]}

print("Exercise 2, output:", x)

# Exercise 3*: Access the value of key ‘history’ from the below dict

sampleDict = {
    "class":{
        "student":{
            "name":"Mike",
            "marks":{
                "physics":70,
                "history":80
            }
        }
    }
}

# Expected output: 80

x = sampleDict["class"]["student"]["marks"]["history"]

print("Exercise 3, output:", x)

# Exercise 4*: Change Brad’s salary to 8500 from a given Python dictionary

sampleDict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}

# Expected output: sampleDict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 8500}
# }

sampleDict["emp3"]["salary"] = 8500

print("Exercise 4, output:", sampleDict)
