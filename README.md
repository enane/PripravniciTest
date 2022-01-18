# PripravniciTest
Par zadačića


1.Napisi funkciju 'same(array, array)' koja prihvata 2 niza. Funkcija treba da vrati 'true' ako vrijednosti u nizu 1 imaju odgovarajuce kvadrirane vrijednosti u nizu 2, vazna napomena je da frekvencija mora biti ista.

same([1,2,3],[4,1,9]) //true
same([1,2,3],[1,9]) //false
same([1,2,1],[4,4,1]) //false (mora biti ista frekvencija odnosno broj kvadradta dvojke mora biti samo jedan a broj kvadrata jedinice bi trebalo da bude dva)

2. Napisi funkciju "countUniqueValues(array)" koja prihvata niz i vraca broj jedinstvenih vrijednosti.

countUniqueValues([1,1,1,1,1,1,2]) //2
countUniqueValues([1,2,3,4,12,7,12,13]) //7
countUniqueValues([]) //0

3. Napisati funkciju "cammel(string)" koja prihvata string i pretvara ga u cammel case verziju sebe. Treba maći znakove interpunkcije sa kraja stringa, prvo slovo treba da bude malo.

cammel("Enida je zavrsila c!") // "enidaJeZavrsilaC"
