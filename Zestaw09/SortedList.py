# Marlena Gryt
# Python 2022/2023
# Zd 9.4
# Lista powiazana podwojnie - posortowana

class Node:
    """Klasa reprezentująca węzeł listy dwukierunkowej."""
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class SortedList:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    # Dodanie elementu 
    def insert(self, node): 
        # jesli lista jest pusta
        if self.is_empty():
            self.tail = self.head = node
        # jesli element dodac mozemy na pierwsze miejsce  
        elif self.head.data <= node.data:
            node.next = self.head
            node.next.prev = node
            self.head = node
        else:
            current = self.head
            while (current.next is not None) and (current.next.data > node.data):
                current = current.next
            node.next = current.next
            if current.next is not None:
                node.next.prev = node
            current.next = node
            node.prev = current
            # zmiana tail jesli element zostal dodany na koniec
            if node.next is None:
                self.tail = node
        self.length += 1


    # Usuniecie i zwrocenie Node z najwiekszym kluczem (head)
    def remove(self): 
        if self.is_empty():
            raise ValueError("pusta lista")
        # 1 element w liscie
        if self.head is self.tail:
            temp = self.head
            self.head = None    # czyszczenie
            self.tail = None 
            temp.next = None
        else:
            temp = self.head
            self.head = self.head.next 
            temp.next = None    # czyszczenie
        self.length -= 1
        return temp


    # Scalanie dwoch list posortowanych
    def merge(self, other): 
        
        if self.is_empty():
            return other
        if other.is_empty():
            return self

        L = SortedList()

        # ustalenie poczatku listy
        if self.head.data <= other.head.data:
            L.tail = other.head
            other.head = other.head.next
        else:
            L.tail = self.head
            self.head = self.head.next
        L.head = L.tail
        L.length += 1
        
        while self.head is not None and other.head is not None:
            if self.head.data <= other.head.data:
                L.tail.next = other.head
                other.head.prev = L.tail
                other.head = other.head.next
            else:
                L.tail.next = self.head
                self.head.prev = L.tail
                self.head = self.head.next
            L.tail = L.tail.next
            L.length += 1

        # jesli jedna z list została niepusta 
        while self.head is not None:
            L.tail.next = self.head
            self.head.prev = L.tail
            self.head = self.head.next
            L.tail = L.tail.next
            L.length += 1
        while other.head is not None:
            L.tail.next = other.head
            other.head.prev = L.tail
            other.head = other.head.next
            L.tail = L.tail.next
            L.length += 1
        return L

    def clear(self):    # czyszczenie listy
        while not self.is_empty():
            self.remove()
            self.length -= 1


    # zwraca liste samych kluczy od head do tail (na potrzeby testow)
    def data_list(self):
        list = []
        current = self.head
        while current is not None:
            list.append(current.data)
            current = current.next
        return list  

    # zwraca liste samych kluczy od tail do head (na potrzeby testow)    
    def data_list_tail(self):
        list = []
        current = self.tail
        while current is not None:
            list.append(current.data)
            current = current.prev
        return list 


