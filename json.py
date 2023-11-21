# import the json library for handling JSON data
import json

# create a dictionary with various data types
data = {
    "name": "John Doe",
    "age": 50,
    "city": "San Diego",
    "interest": ["stock trading", "video games", "running"],
    "is_student": True
}

# use the 'with' statement to open and write to a file named data.json
with open("data.json", "w") as json_file:
    # utilize the dump method from the json library to save the data with an indentation of 4 spaces
    json.dump(data, json_file, indent=4)

print("data has been written to data.json")

# open the data.json file to read its contents
with open("data.json", "r") as json_file:
    # load the content into an object named loaded_data
    loaded_data = json.load(json_file)

print("successfully read data.json")
# print the content of the data.json file
print(loaded_data)

# modify the loaded_data object: change age to 51 and add an interest in reading
loaded_data["age"] = 51
loaded_data["interest"].append("eating food")

# write the modified data back to the data.json file
with open("data.json", "w") as json_file:
    # use the dump method again to update the file with the modified data
    json.dump(loaded_data, json_file, indent=4)

# confirm that the file has been updated
print("Modified data written to data.json")
