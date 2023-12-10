
from random import randrange
from collections import defaultdict


display_map ={0:{'a','b','e','c','f','g'},
              1:{'c','f'},
              2:{'a','c','d','e','g'},
              3:{'a','c','d','f','g'},
              4:{'b','d','c','f'},
              5:{'a','b','d','f','g'},
              6:{'a','b','d','e','f','g'},
              7:{'a','c','f'},
              8:{'a','b','c','d','e','f','g'},
              9:{'a','b','c','d','f','g'}}



def read_data(file = "data.txt",sep="\n"):
  data=[]
  with open(file,'r') as f:
    data = list(f.read().split(sep))
  return data


def compare_str(str1,str2):
  set1 = set(str1)
  set2 = set(str2)
  diff = set1 - set2
  return diff


#generate rules using default map 
# result for digit = 0 
# {0: [(1, 0), (7, 0), (0, 8)], 4: [(0, 1)], 1: [(4, 0), (8, 0)], 3: [(0, 4), (0, 7)]}) 
# stored as length of result and the order of the set subtraction 
def generate_rules(digit,default_digits=(1,4,7,8)):


  rules = defaultdict(list)

  for default_digit in default_digits:
    key1,key2 = default_digit,digit
    result = compare_str(display_map[key1],display_map[key2])
    rules[len(result)].append((key1,key2))
    key1,key2 = digit,default_digit
    result = compare_str(display_map[key1],display_map[key2])
    rules[len(result)].append((key1,key2))
  # print("rules",digit,rules)
  return rules;


def verify_rules(digit,code,rules,fixed_encode):
  if len(code) != len(display_map[digit]):
    return False
  for count,rule_list in rules.items():
    for rule in rule_list:
      pos1,pos2=rule
      if pos1 == digit:
        str1= code
        str2= list(fixed_encode[pos2])[0]
      if pos2 == digit:
        str1= list(fixed_encode[pos1])[0]
        str2= code

      if count != len(compare_str(str1,str2)):        
        # print("Test failed",count,rule,str1,str2)
        return False
      else:
        # print("Test passed",count,rule,str1,str2)
        pass

  return True    


def get_fixed_length_encodes(encodes,display_map):
  decodes = {}
  #codes for  digits 1, 4, 7, and 8
  for key in (1,4,7,8):
    decodes[key] = set(item for item in encodes if len(item)==len(display_map[key]))
  return(decodes)

def decipher_display(data = read_data() ):
  encodes = [item.split('|')[0].split() for item in data ]
  displays = [item.split('|')[1].split() for item in data ]
  fixed_encodes=[]
  for item in encodes:
    fixed_encodes.append(get_fixed_length_encodes(item,display_map))

  count  = 0
  for index,display in enumerate(displays):
    fixed_encode = fixed_encodes[index]
    # print(fixed_encode,display)
    decoded_number = ''
    for code in display:
      for digit in range(10):
        rules= generate_rules(digit)      
        if verify_rules(digit,code,rules,fixed_encode):
          decoded_number += str(digit)
      # print("Next display")    
    count+= int(decoded_number) 
  print(count)        




def main():
  decipher_display()

if __name__ == "__main__":
  main()