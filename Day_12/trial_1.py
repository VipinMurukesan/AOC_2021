import os
from dataclasses import dataclass
from enum import StrEnum, auto
from collections import defaultdict, namedtuple

def read_data(file = "data.txt",sep="\n"):
  data=[]
  with open(file,'r') as f:
    data = list(f.read().split(sep))
  return data

class NodeType(StrEnum):
    SingleVisit = auto()
    MultiVisit = auto()


Node = namedtuple("Node","name node_type")


# @dataclass
# class Node:
#     name: str
#     node_type: NodeType


# @dataclass
# class Connection:
#   node1: Node
#   node2: Node

class Map():
  def __init__(self,input=read_data()):
    self.nodes = []
    self.connections = defaultdict(list)
    for item in input:
      node1_name,node2_name = item.split('-')
      node1_type = NodeType.SingleVisit if str.islower(node1_name) else NodeType.MultiVisit
      node2_type = NodeType.SingleVisit if str.islower(node2_name) else NodeType.MultiVisit
      node1= Node(node1_name,node1_type)
      node2= Node(node2_name,node2_type)
      self.nodes.extend([node1,node2])
      if node2.name != 'start':
        self.connections[node1].append(node2)
      if node1.name != 'end':
        self.connections[node2].append(node1)

  def __str__(self):
    return str(self.nodes)    
      
  def generate_paths(self,startNode,endNode,pathDict,currentPath =[]):
    
    currentPath.append(startNode.name)

    print(os.linesep)
    print(f"StartNode {startNode.name} -> EndNode {endNode.name}")
    print(f"Options from {startNode.name} are {[path.name for path in pathDict[startNode]]}")
    
    for node in pathDict[startNode]:
      if node != endNode and node.name != 'start':
        print(f"New StartNode {node.name}")
        if node.node_type == NodeType.SingleVisit:
          pathDict[startNode].remove(node)
          print(f" {node.name} Node removed from path of {startNode.name}")
        print(os.linesep)  
        self.generate_paths(node,endNode,pathDict,currentPath)
    if endNode in pathDict[startNode]:
      currentPath.append(endNode.name)
      return currentPath    


  def getPaths_start_to_endNodes(self):
    startNode = [node for node in self.nodes if node.name == "start" ][0]
    endNode = [node for node in self.nodes if node.name == "end" ][0] 
    pathDict = self.connections.copy()    
    path = self.generate_paths(startNode,endNode,pathDict) 
    
      








def main():
  map = Map()
  # print(map)
  map.getPaths_start_to_endNodes()



if __name__ == "__main__":
  main()


