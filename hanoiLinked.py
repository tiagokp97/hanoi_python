class Node:

    
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize 
                          # next as null
   
# Queue class
class LinkedList:
    length = 0
    # Init Class
    def __init__(self): 
        self.head = None
        self.tail = None

    def isEmpty(self):
        if self.head == None:
            return True
    
    def size(self):
        return self.length
    
    def gameStart(self, data):
        for i in range(data, 0, -1):
            column_1.push(i, 0)
    
    def push(self,data,pos=-1):

        if pos > self.length:
            print("Cannot insert in %d. length == %d" % (pos,self.length))
            return

        #First element
        if self.isEmpty():
            node = Node(data)
            self.head = node 
            self.tail = node

        #Insert at Tail
        elif(pos == -1): 
            node = Node(data)
            self.tail.next = node
            self.tail = node

        #Insert at Head
        elif(pos == 0):
            node = Node(data)
            node.next = self.head
            self.head = node

        #Insert at any position    
        elif pos <= self.length: #Sanity check 
            it = self.head
            i = 1 
            while(i<pos):
                it = it.next
                i+=1
                
            temp = it.next
            node = Node(data)
            node.next = temp
            it.next = node

                        
        self.length += 1

        return
    
    def pop(self,pos=0):

        #Last postion index
        if pos == -1:
            pos = self.length-1
        
        if self.isEmpty():
            print("Nothing to remove")

        #Insert at Head
        elif pos==0:             
            node = self.head
            self.head = self.head.next
            del node

        else:
            it = self.head
            i = 1 

            while(i<pos):                
                it = it.next
                i+=1

            node = it.next
            it.next=it.next.next
            del node

            if pos == self.length -1:
                self.tail = it
                self.tail.next = None
                
        self.length -= 1

    def display(column1, column2, column3, blocks):
        max_length = max(column1.size(), column2.size(), column3.size())
        if max_length == 0:
            print("Sem discos")
            return

        col1_data = []
        col2_data = []
        col3_data = []

        it1 = column1.head
        it2 = column2.head
        it3 = column3.head

        for _ in range(blocks):
            col1_data.append(None if it1 is None else it1.data)
            col2_data.append(None if it2 is None else it2.data)
            col3_data.append(None if it3 is None else it3.data)

            if it1: it1 = it1.next
            if it2: it2 = it2.next
            if it3: it3 = it3.next

        print(f"Coluna 1\tColuna 2\tColuna 3")

        sorted = sort_arrays(col1_data, col2_data, col3_data, blocks)

        for i in range(blocks):
                print(f"{sorted[0][i]}\t\t{sorted[1][i]}\t\t{sorted[2][i]}")
            
    def print(self):
        if self.isEmpty():
            print("Empty Stack")
            return
        
        it = self.head
        
        while(it != None):
            print (it.data)
            it = it.next


    def moveBlockFrom(self,data):
            head = data.head.data

            #First element
            if self.isEmpty():
                node = Node(head)
                self.head = node 
                self.tail = node
                self.length += 1
                data.pop()

            #Insert at Head
            else:
                if self.head.data > head:
                    node = Node(head)
                    node.next = self.head
                    self.head = node
                    self.length += 1
                    data.pop()
                    return

                else:
                    print('Não é possível adicionar um bloco com maior que o que já tem')
                    print(f' Essa coluna tem um bloco com valor {head}, tentou colocar o blocor {self.head.data}')       

def get_user_input(message):
    print(message)
    return input()     

def get_column(column_number):
    if column_number == "um":
        return 'column_1'
    elif column_number == "dois":
        return 'column_2'
    elif column_number == "tres":
        return 'column_3'
    elif column_number == "quatro":
        return 'column_4'
    elif column_number == "cinco":
        return 'column_5'
    else:
        raise ValueError("Invalid column number")         

          
def get_blocs(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 2 <= value <= 13:
                return value
            else:
                get_user_input("Por favor, escolha um número de 3 a 13.")
        except ValueError:
            get_user_input("Entrada inválida. Digite um número válido.")

def sort_arrays(array1, array2, array3, blocks):
    new_array1 = []
    new_array2 = []
    new_array3 = []
    for i in range(blocks):
        if array1[i] is None:
            new_array1.insert(0, array1[i])
        else:
            new_array1.append(array1[i])
        if array2[i] is None:
            new_array2.insert(0, array2[i])
        else:
            new_array2.append(array2[i])
        if array3[i] is None:
            new_array3.insert(0, array3[i])
        else:
            new_array3.append(array3[i])
    return new_array1, new_array2, new_array3

      
        

column_1 = LinkedList()
column_2 = LinkedList()
column_3 = LinkedList()
# Criação dinâmica de colunas
# columnNumber = get_user_input("Quantas colunas você deseja? 3, 5 ou 7?")
# for i in range(2, int(columnNumber) + 1):
#     column_name = f"column_{i}"
#     columns[column_name] = LinkedList()

blockNumber = get_blocs("Com quantos discos você quer jogar? escolha um número de 3 a 13. \n")
column_1.gameStart(blockNumber)

columns = {}

columns['column_1'] = column_1
columns['column_2'] = column_2
columns['column_3'] = column_3


while True:
    column_from = get_user_input("Quer retirar o bloco de qual coluna? um, dois ou tres?")
    column_to = get_user_input("Em qual coluna você quer adicionar? dois ou tres?")

    coluna1 = columns[get_column(column_from)]
    coluna2 = columns[get_column(column_to)]
    coluna2.moveBlockFrom(coluna1)
    column_1.display(column_2, column_3, int(blockNumber))


    if column_3.size() == blockNumber:
        print("Parabéns! Você completou o jogo!")
        break


