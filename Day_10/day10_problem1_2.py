from collections import deque


def read_data(file = "data.txt",sep="\n"):
  data=[]
  with open(file,'r') as f:
    data = list(f.read().split(sep))
  return data

class PatternValidator():
  
  matchPattern = {"(":")","[":"]","{":"}","<":">"}
  
  def __init__(self,pattern):    
    self.isValid = False
    self.stack = deque()
    self.validate(pattern)

  def validate(self,pattern):    
    for item in pattern:
      if len(self.stack) == 0 or self.matchPattern.get(self.stack[-1],None) != item:
        self.stack.append(item)
      else:
        self.stack.pop()
    if len(self.stack) != 0:
      self.isValid = False
    else:
      self.isValid = True

def calculate_corrupt_points(input=read_data("data.txt")):
  invalid_pattern_map = {")":3,"]":57,"}":1197,">": 25137}
  points = 0
  for item in input:
    validator = PatternValidator(item)
    for symbol in validator.stack:
      if symbol in invalid_pattern_map:
        points += invalid_pattern_map[symbol]
        break
  return points     

def calculate_incomplete_points(input=read_data("data.txt")):
  incomplete_pattern_map = {")":1,"]":2,"}":3,">": 4}
  matchPattern = {"(":")","[":"]","{":"}","<":">"}  
  pattern_points = []
  for item in input:
    validator = PatternValidator(item)
    points = 0
    isCorrupt = False
    while len(validator.stack) != 0:
      closing_symbol = matchPattern.get(validator.stack.pop(),None)
      if closing_symbol:
        points = (points*5)+incomplete_pattern_map[closing_symbol]
      else:
        isCorrupt = True        
        break
    if (not isCorrupt):
      pattern_points.append(points)   
  return sorted(pattern_points)[len(pattern_points)//2]      


def main():
  print("Total Corrupt Points",calculate_corrupt_points())
  print("Total Incomplete Points",calculate_incomplete_points())

if __name__ == "__main__":
  main()