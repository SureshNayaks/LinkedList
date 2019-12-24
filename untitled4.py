class Node():
    def __init__(self,value):
        self.info=value         # self.data=data
        self.link=None          # self.next=next
class Linkedlists():
    def __init__(self):
        self.start=None         # self.head=head
        
    #this function travells all over the Nodes and the references and displays the list
    
    def display(self):
        
        if self.start is None:
            return ("the list is empty")
        else:
            print("the list is : ")
            p=self.start
            while p is not None:
                print(p.info," ",end='')
                p=p.link
            print()
    
    # this function counts all the Nodes and return the number nodes present in the  [array] actually not an array    
    def Counting(self):
        p=self.start
        n=0
        while p is not None:
            p=p.link
            n+=1
        print('Number of Nodes in the list %d'%(n))
    
    # this function will return True if the el
    def search(self,x):
        p=self.start
        position=1
        while p is not None:
            if p.info==x:
                print(x,"the element is found :",position)
                return True
            position+=1
            p=p.link

        else:
            print(x,"the element is not found")
            return False
        
    def Last_node_ref(self):
        p=self.start
        while p.link is not None:
            p=p.link
            
    def sec_Last_node_ref(self):
        p=self.start
        while p.link.link is not None:
            p=p.link
    def x_node_ref(self,x):
        p=self.start
        while p is not None:
            if p.info==x:
                break
            p=p.link
    def x_nodes_predecs_ref(self,x):
        p=self.start
        while p.link is not None:
            if p.link.info==x:
                break
            p=p.link
    def k_node_ref(self,k):
        p=self.start
        i=1
        while p  and k<i is not None:
            i+=1
            p=p.link
        return i
            
    def insert_in_the_beginning_of_List(self,data):
        temp=Node(data)
        temp.link=self.start
        self.start=temp
        
    def insert_in_the_empty_list(self,data):
        temp=Node(data)
        self.start=temp
    def insert_at_end(self,data):
        temp=Node(data)
        
        if self.start is None:
            self.start=temp
            return
        
        p=self.start    
        while p.link is not None:
            p=p.link
        p.link=temp
    def create_list(self):
        n=int(input("enter the number of nodes inserting:"))
        if n==0:
            print(" zero elements are present in the list")
            
        for i in range(n):
            data=int(input("enter the element to add the list:"))
            self.insert_at_end(data)
    



    # here is the code for the all types of nodes
        
    def insert_after(self,data,x):
        temp=Node(data)
        p=self.start
        while p is not None:
            if p.info==x:
                break
            p=p.link
        if p is None:
            return("%d is not present in the list"%(x))
            
        else:
            temp.link=p.link
            p.link=temp
    def insert_before(self,data,x):
        temp=Node(data)
        
        if self.start is None:
            print("the list is empty")
            return
        if x==self.start.info:
            temp.link=self.start
            self.start=temp
            return
        p=self.start   
        while p.link is not None:
            if p.link.info==x:
                break
            p=p.link
        else:
            temp.link=p.link
            p.link=temp
        
    def insert_at_k(self,data,k):
        temp=Node(data)
        if k==1:
            temp.link=self.start
            self.start=temp
            return
        '''if self.Counting()==0:
            self.insert_in_the_empty_list()'''
        
        i=1
        p=self.start
        while i<k-1 and p is not None:
            p=p.link
            i+=1
            #continue
        if p is None:
            print("k exceeded the range")
            return
        
        else:
            temp.link=p.link
            p.link=temp
            
            
    #here is the code for the all the deletion of nodes

    def delete_at_beginning(self):
        
        if self.start is None:
            print("there are no elements present in the list:")
            return
        
        else:
            self.start=self.start.link
            return
    
    def delete_at_end(self):
        if self.start is None:
            print("there are no elements present in the list:")
            return
        else:
            p=self.start
            
            while p.link is not None:
                p=p.link
                break
            p.link=None
    def delete_at_k(self,k):
        i=1
        
        if self.start is None :
            print("list is empty")
            return
        
        p=self.start
        while i<k-1 and p.link is not None:
            p=p.link
            k+=1
            break
        p.link=p.link.link
        
        
    def delete(self,x):
        if self.start is None:
            print("list is empty")
            return
        p=self.start
        if self.start.link==None:
            self.start=None
            return
        while p is not None  and p.link is not None:
            if p.link.info==x:
                p.link=p.link.link
                break
            
     #this function is defined for reversing the list


    def reverse(self):
        p=self.start
        while p is not None:
            p=p.link
            break
        self.start=p
        
        
            
    #now here comes sorting
    #1) merge sort
    
    
    
        
            
            
        
            
            
        
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                