
# initilizing Node class

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        
class LinkedList:
    def __init__(self) :
        self.head = None

    def addBegin(self,value):
        if self.head is None:
            self.head = Node(value)





def main():
    input_condition = eval(input("Enter a value : "))
    input_value = eval(input("Enter a value :"))
    if input == 1:
        lst = LinkedList()
        lst.head = Node(input_value)

    
if __name__ == "__main__":
    main()
    print()

    
