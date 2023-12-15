import os
import copy
from dataclasses import dataclass
from enum import StrEnum, auto
from collections import defaultdict, namedtuple

def read_data(file = "data.txt",sep="\n"):
  data=[]
  with open(file,'r') as f:
    data = list(f.read().split(sep))
  return data



class Map():
  def __init__(self,input=read_data()):
    self.nodes = []
    self.connections = defaultdict(list)
    for item in input:
      node1_name,node2_name = item.split('-')
      self.nodes.extend([node1_name,node2_name])

      if node2_name == "start" or node1_name == "end":
        node1_name,node2_name = node2_name,node1_name
      

      self.connections[node1_name].append(node2_name)  
      if node1_name != 'start' and node2_name != 'end':
        self.connections[node2_name].append(node1_name)
    #   print(self.connections)  



  def __str__(self):
    return str(self.nodes)    
      
  
  def generate_paths(self,startNode,endNode,pathDict,validPaths,currentPath =[]):
    
    # print(f"{startNode} -> {endNode}")
    # print(pathDict)
    # print(currentPath)

    currentPath.append(startNode)
    if startNode == endNode:
        validPaths.append(currentPath)
        return
        # print("Path: ",currentPath)

    # print(os.linesep)
    

    for node in pathDict[startNode]:
      if str.islower(node) and node in currentPath:
        continue
      newPathDict = pathDict
      newCurrentPath = currentPath.copy()
      if str.islower(startNode):
        newPathDict = copy.deepcopy(pathDict)
        if startNode in newPathDict[node]:
          newPathDict[node].remove(startNode)
      self.generate_paths(node,endNode,newPathDict,validPaths,newCurrentPath)
      
   


  def getPaths_start_to_endNodes(self):
    startNode = "start"
    endNode = "end" 
    pathDict = copy.deepcopy(self.connections)
    validPaths = []
    self.generate_paths(startNode,endNode,pathDict,validPaths) 
    # print(validPaths) 
    print(f"Total number of valid paths: {len(validPaths)}")
      



def main():
  map = Map()
  # print(map)
  map.getPaths_start_to_endNodes()



if __name__ == "__main__":
  main()


