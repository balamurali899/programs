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
  def insertAtBeg(self,data):
      temp=Node(data)
      temp.nextt=self.head 
      self.head=temp
  def DelAtBeg(self):
      temp=self.head
      self.head=self.head.nextt
      temp.nextt=None   
         
     
obj=SLL()
ch=0
while ch!=4:
  print("linked list implementation\n","1.insertion 2.deletion 3.printlist 4.exit")
  ch=int(input()) 
  if ch==1:
    print('enter the value of the Node')
    data=input()
    obj.insertAtBeg(data)
    obj.printList()
  elif ch==2:
    obj.DelAtBeg()
    obj.printList()  
  elif ch==3:
    obj.printList()           
