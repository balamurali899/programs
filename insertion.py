class Node:
  def __init__(self,data):
    self.data=data
    self.nextt=None
class SLL:
  def __init__(self):
    self.head=None
  def printList(self):
    temp=self.head
    while temp!=None:
      print(temp.data,"==>",end='')
      temp=temp.nextt
      
obj=SLL()
ch=0
while ch!=4:
  print("linked list implementation\n","1.insertion 2.deletion 3.print list 4.exit")
  ch=int(input()) 
  if ch==1:
    print('enter the value of the Node')
    data=input()
    temp=Node(data)
    temp.next=obj.head
    obj.head=temp
    
  elif ch==3:
    obj.printList()           .
