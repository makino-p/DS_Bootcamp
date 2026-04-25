import sys
import ast

class TypeMatrix:

    def __init__(self, data):
        self.data = data


    def type_grid(self):
        new_data = []
        for lists in self.data:
            new_data.append(lists)
        
        for row in new_data:
            for index, item in enumerate(row):
                if isinstance(item, str):
                            try:
                                parsed = ast.literal_eval(item)
                                item_type = type(parsed).__name__
                            except:
                                item_type = "str"
                else:
                            item_type = type(item).__name__

                row[index] = item_type
     
    
    def most_common_type():
        pass    


data = [
    ["Яблоко", 5, 1.2],
    ["Банан", 10, 0.5],  
    ["Апельсин", 3, 2.0]      
]


matrix = TypeMatrix(data)

print(matrix.type_grid())

