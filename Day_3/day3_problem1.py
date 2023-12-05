def read_data(file = "data.txt"):
  data=[]
  with open(file,'r') as f:
    data = list(f.read().split('\n'))
  return data


def calculate_gamma_epsilon(data=read_data()):
  gamma_str =""
  epsilon_str = ""
  length = len(data[0])
  for i in range(length):
    zeros_count = 0
    ones_count = 0
    for item in data:
      if item[i] == "0":
        zeros_count += 1
      elif item[i] == "1":
        ones_count += 1 
    if zeros_count > ones_count:
      gamma_str += "0"
      epsilon_str += "1"
    else:
      gamma_str += "1"
      epsilon_str += "0"
  gamma = int(gamma_str,2)
  epsilon = int(epsilon_str,2)
  return (gamma,epsilon)
    

def main():
  gamma,epsilon = calculate_gamma_epsilon()
  print(gamma*epsilon)

if __name__ == "__main__":
  main()  