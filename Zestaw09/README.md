<h3>ZADANIE 9.4 (SORTEDLIST)</h3>
<p>Na bazie list powiązanych pojedynczo lub podwójnie stworzyć klasę SortedList, która przechowuje listę stale posortowaną. Największy element jest na początku listy (head).

<pre>
class SortedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def insert(self, node): pass
        # L = SortedList() ; L.insert(Node(3))

    def remove(self): pass
        # Zwraca node z elementem największym, czyli head.
        # Długość listy zmniejsza się o jeden węzeł.

    def merge(self, other): pass
        # Scalanie dwóch list posortowanych.
        # Po tej operacji lista other ma być pusta.

    def clear(self): pass   # czyszczenie listy
</pre>
