def read_data(file = "data.txt",sep="\n"):
  data=[]
  with open(file,'r') as f:
    data = list(f.read().split(sep))
  return data


def get_unique_length_displays(data=read_data()):

  displays = [item.split('|')[1] for item in data ]

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

  #how many times do digits 1, 4, 7, or 8 appear
  expected_counts =[ len(value) for key,value in display_map.items() if key in (1,4,7,8)]

  # print(expected_counts)

  count = 0
  for display in displays:
     count += len([ item for item in display.split() if len(item) in expected_counts])

  print(f"Digits 1, 4, 7, or 8 appear {count} times in the input file")    


def main():
  get_unique_length_displays()

if __name__ == "__main__":
  main()