# def do_operation(a, b, operation):
#     result = operation(a, b)
#     print(f"result = {result}")
#
#
# do_operation(5, 4, lambda a, b: a + b)  # result = 9
# do_operation(5, 4, lambda a, b: a * b)  # result = 20
import json

data = {"name": "John", "age": 30, "city": "New York"}

# Without indentation
print(json.dumps(data))

# With indentation
print(json.dumps(data, indent=2))