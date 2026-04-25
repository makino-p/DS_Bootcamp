import sys
import ast


file_path = sys.argv[1]
data_types_dict = {}

if len(sys.argv) <= 1:
   raise Exception("Not enough arguments!")
else:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for data in lines:
        try:
           data = ast.literal_eval(data)
           data_type = type(data).__name__ 
           data_types_dict[data_type] = data_types_dict.get(data_type, 0) +  1
        except:
            data_types_dict['string'] = data_types_dict.get('string', 0) + 1 
    print(data_types_dict)
      