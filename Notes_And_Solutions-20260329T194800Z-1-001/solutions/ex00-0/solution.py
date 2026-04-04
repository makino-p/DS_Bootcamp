import sys
import ast

data_types = ["int", "float", "bool", "str"]
data = sys.argv[1]

if len(sys.argv) <= 1:
   raise  print("Error not enough arguments!")
elif len(sys.argv) >= 2:
    unknown_type = eval(data)
    known_type = type(unknown_type).__name__
    if known_type in data_types:
        print(known_type, unknown_type)
    else:
        print(f"String: {data}")


   
   