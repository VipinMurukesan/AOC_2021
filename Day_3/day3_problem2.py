import itertools

def read_data(file = "data.txt"):
  data=[]
  with open(file,'r') as f:
    data = list(f.read().split('\n'))
  return data

# updates mask with zero_indices
# example mask is [0 1 0 1 1] , zero_indices is [ 0 2] 
# # update_mask will set the non-zero values of mask to zeros as per zero_indices
# returns [0 0 0 1 0] , considers the ones and sets them to zeros  
def update_mask(mask,zero_indices):
  counter = 0  
  for index,value in enumerate(mask):
    if len(zero_indices) > 0:
      if value == 0:
        continue
      else:
        if counter == zero_indices[0]:
          mask[index] = 0
          zero_indices.pop(0) 
        counter += 1 
  return mask      



def get_scrubber_ratings(data=read_data()):
    gamma_str =""
    epsilon_str = ""
    length = len(data[0])

    scrubber_mask = [1 for item in data]

    for i in range(length):
      if sum(scrubber_mask) == 1:
        return(list(itertools.compress(data,scrubber_mask))[0]) 
      zeros_count = 0
      ones_count = 0
      zero_indices = []
      one_indices = []
      for index,item in enumerate(itertools.compress(data,scrubber_mask)):
        if item[i] == "0":
          zeros_count += 1
          zero_indices.append(index)
        elif item[i] == "1":
          ones_count += 1 
          one_indices.append(index)
      if ones_count >=zeros_count :
          scrubber_mask = update_mask(scrubber_mask,one_indices)          
      else:
        scrubber_mask = update_mask(scrubber_mask,zero_indices)
       

    return(list(itertools.compress(data,scrubber_mask))[0])  
    


def get_generator_ratings(data=read_data()):
    gamma_str =""
    epsilon_str = ""
    length = len(data[0])

    generator_mask = [1 for item in data]

    for i in range(length):
      if sum(generator_mask) == 1:
        return(list(itertools.compress(data,generator_mask))[0])
      zeros_count = 0
      ones_count = 0
      zero_indices = []
      one_indices = []
      for index,item in enumerate(itertools.compress(data,generator_mask)):
        if item[i] == "0":
          zeros_count += 1
          zero_indices.append(index)
        elif item[i] == "1":
          ones_count += 1 
          one_indices.append(index)
      if ones_count >=zeros_count :
          generator_mask = update_mask(generator_mask,zero_indices)
      else:
        generator_mask = update_mask(generator_mask,one_indices)

    return(list(itertools.compress(data,generator_mask))[0])  
    

def main():
  generator_rating = int(get_generator_ratings(),2)
  scrubber_rating = int(get_scrubber_ratings(),2)
  print(generator_rating*scrubber_rating)

if __name__ == "__main__":
  main()