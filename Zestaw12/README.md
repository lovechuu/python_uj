<h3> ZADANIE 12.3 (SNAKE)</h3>
<p>Uproszczona wersja gry Snake.
<p>Wąż ma początkowo rozmiar jednego kwadratu, porusza się ruchem jednostajnym w kierunku poziomym lub pionowm, zmiana kierunku (skręt) następuje po naciśnięciu kursora. 
Zabroniony jest ruch wstecz (koniec gry). Zakładamy, że plansza ma periodyczne warunki brzegowe.
<p>Zadaniem gracza jest poruszanie wężem i zjadanie pożywnych owoców <img src="/Zestaw12/assets/apple.png"> oraz omijaniem owoców zatrutych <img src="/Zestaw12/assets/rotten_apple.png">, które pojawiają się losowo na planszy i żyją określony czas. 
W każdym momencie na planszy obecny jest najwyżej jeden owoc.
Zjedzenie pożywnego owocu powoduje wydłużenie węża i dodanie punktu, zjedzenie zatrutego - skrócenie długości węża i odjęcie punktu. 
<p>Gra kończy się zwycięstwem po upływie 5 minut lub przegraną: po niedozwolonym ruchu lub skróceniu długości węża do 0. 
Wynik gry to stan licznika owoców.
