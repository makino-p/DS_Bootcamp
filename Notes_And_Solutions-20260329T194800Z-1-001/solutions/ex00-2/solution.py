import sys
import ast
class TypeMatrix:

    def __init__(self, data):
        self.data = data


    def type_grid(self):
        new_data = []
        index_counter = 0
        for lists in self.data:
            new_data.append(lists)
    
        for changed_lists in new_data:
            
            for list_elements in changed_lists:
                try:

                    changed_lists[index_counter] = type(ast.literal_eval(list_elements)).__name__ 
            
                except:
                    changed_lists[index_counter] = "string"
            index_counter = index_counter + 1


        return new_data  
                    
    
    def most_common_type():
        pass    


data = [
    ["Яблоко", 5, 1.2],
    ["Банан", 10, 0.5],  
    ["Апельсин", 3, 2.0]      
]


object = TypeMatrix(data)

print(object.type_grid())

