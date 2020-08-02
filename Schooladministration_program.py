class student:
    def __init__(self , name , rollno , mark1 , mark2) :
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2

    def accept(self , name , rollno , mark1 , mark2):
    obj = student(name , rollno , mark1 , mark2)
    ls.append(obj)

    def display(self, obj) :
            print("name : ", obj.name)
            print("rollno : ",obj.name)
            print("mark1 : ",obj.mark1)
            print("mark2 : ",obj.mark2)
            print("/n")

    def search(self, rn):
        for i in range(ls.__len__()) :
            if(ls[i] . rollno == rn)
                return i

    def delete(self, rn):
        i = obj.search(rn)
        del ls[i]

    def update(self , rn, no):
        i = obj.search(rn)
        roll = no
        ls[i].rollno = roll:

    ls = []

    obj = student('',0 , 0 , 0)

    print("\n Operations used,")
    print("\n1.accept the student details/ \n2.display the student details/ \n3.search the student details/ \n4.delete the student details/ \n5.update the student details / \n6.exit")

    ch = int(input("Enter choice:"))
    if(ch == 1):

    obj.accept("A" , 1, 100, 100)
    obj.accept("B" , 2, 90, 90)
    obj.accept("C" , 3, 80, 80)

   elif(ch == 2):
   print("\n")
   print("\nList of Students\n")
   for i in range(ls.__len__()):
       obj.display(ls[i])

   elif(ch == 3):
   print("\n student found,")
   s = obj.search(2)
       obj.display(ls[s])

   elif(ch == 4):
   obj.delete(2)
   print(ls.__len__())
   print("List after deletion")
   for i in range(ls.__len__()):
       obj.display(ls[i])

   elif(ch == 5):
   obj.update(3,2)
   print(ls.__len())
   print("List after updation")
   for i in range(ls.__len__()):
       obj.display(ls[i])

    else:
    print("Thank You !")
