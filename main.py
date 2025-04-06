import json

# Read input
# name = input()
# year = int(input())
# creator = input()
# is_oop = input().lower() == 'true'
# versions = input().split(',')

# Create the dictionary
# python_info = {
#     "name": name,
#     "year": year,
#     "creator": creator,
#     "is_oop": is_oop,
#     "versions": versions
# }

# new_json = json.dumps(python_info)
# print(new_json)
#
# # 3. Use json.dump() to write the dictionary to a file named "python_info.json"
# with open("python_info.json", "w") as file:
#     json.dump(python_info, file)
#
# # 4. Use json.load() to read the contents of "python_info.json"
# with open("python_info.json", "r") as file:
#     loaded_object = json.load(file)
#
# print(loaded_object)
input_str = input()
ind = int(input())
form = input().lower() == 'true'
# form = json.loads(form.lower())
input_obj = json.loads(input_str)
def format_json(obj, ind, sep1):
    if sep1 == False:
        return json.dumps(obj, indent=ind, separators=(', ', ': '), sort_keys=True)
    else:
        return json.dumps(obj,  separators=(',', ':'), sort_keys=False)

result = format_json(input_obj, ind, form)

# Print the result
print(result)