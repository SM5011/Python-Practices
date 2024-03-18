# Answer to question no. 3.2

def create_element_cubes_dict(list1):

  element_cubes_dict = {}
  for element in list1:
    element_cubes_dict[element] = element**3
  return element_cubes_dict

list1 = [11, 13, 17, 19, 23]

element_cubes_dict = create_element_cubes_dict(list1)
print("Result Dictionary:", element_cubes_dict)
