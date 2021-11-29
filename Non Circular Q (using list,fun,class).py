class queue:
    def __init__ (me): me._list=[]
    def empty (me): return me._list==[]
    def enqueue (me,data):
        me._list.append(data)
        print(f"{data} is succ added\n")
    def display (me): print(f"{me._list}")
    def dequeue (me): print (me._list.pop(0), "suc deq\n")
def main():
    q=queue()
    while True:
        ch=input("1.Enq\n2.Deq\n3.Display\n4.Exit\nChoice : ")
        if ch=="1": q.enqueue(input("Enter data : "))
        elif ch=="2":
            if q.empty():print("Queue is Empty\n")
            else:q.dequeue()
        elif ch=="3":
            if q.empty():print("Queue is Empty\n")
            else : q.display()
        elif ch=="4":
            print("Please Exit")
            break
        else: print("Wrong Choice")
main()