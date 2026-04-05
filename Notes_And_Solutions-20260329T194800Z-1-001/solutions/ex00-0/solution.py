import sys
import ast

data_types = ["int", "float", "bool", "str"]
data = sys.argv[1]

try:
   data_type = type(ast.literal_eval(data)).__name__
   print(f"{data_type}: {data}")

except:
   print(f"string: {data}")

   
   