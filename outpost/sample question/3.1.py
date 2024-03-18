# Answer to question no. 3.1

def find_common_elements(list1, list2):
  common_elements = []
  for element in list1:
    if element in list2:
      common_elements.append(element)
  return common_elements

list1 = [11, 13, 17, 19, 23]
list2 = [3, 6, 9, 12, 15]

common_elements = find_common_elements(list1, list2)
print("Common Elements:", common_elements)  
