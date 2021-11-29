q=[]
size=int(input("Enter the size of Queue:"))
def Enqueue():
    if len(q)==size: print("\nQ is Full")
    else:
        e1=input("\nEnter the element:")
        q.append(e1)
        print("suc enq",e1)
def dequeue():
    if len(q)!=size: print("Q is Empty")
    else: print("\nsuc deq",q.pop())
def display():
    if len(q)!=size: print("Q is Empty")
    else: print(q)
def main():
    while True :
        print("\n1.Enq\n2.Deq\n3.Display\n4.Exit\nChoice :",end=" ")
        ch=int(input())
        if ch==1: Enqueue()
        elif ch==2: dequeue()
        elif ch==3: display()
        elif ch==4:
            print ("P E")
            break
        else: print("W C")
main()
