# Programowanie w jezyku Python 2016/2017 zadanie 2

W celu oszacowania czasu wykonania programu kuszące jest czasem zalozyc liniowa złożoność obliczeniowa.
Czas sortowania możemy oszacować monotonicznej listy na 17.9 us dla 1000 elementów:

```bash
python -m timeit -s "s = list(range(1000))" "sorted(s)"
100000 loops, best of 3: 17.9 usec per loop
```


Próbując uogólnić ten wynik na listę składająca sie z 10^6 elementów spodziewalibyśmy się wyniku okolo 18 ms. Dokonując pomiaru otrzymujemy jednak czas o około 35% większy: 

```bash
python -m timeit -s "s = list(range(1000000))" "sorted(s)"
10 loops, best of 3: 24.5 msec per loop
```


Przygotuj program do automatycznego wyznaczania złożoności obliczeniowej.

Program ten powinien otrzymywać na wejściu:
 -  Inicjalizacje odpowiednich struktur
 - Funkcje lub klase odpowiedzialna za wykonanie algorytmu
 - Kod odpowiedzialny za posprzątanie

Jako wynik powinniśmy otrzymać:
 - Informacje o przypuszczalnej klasie złożoności obliczeniowej ( O(n), O(n log(n)), O(n^2))
 - Funkcje umożliwiające przewidywanie jaki będzie czas wykonania programu dla zadanej wielkości problemu
 - Funkcję umożliwiającą przewidywanie jaki jest maksymalny rozmiar problemu obliczeniowego dla zadanego czasu

Wyznaczanie złożoności niektórych algorytmów może trwać bardzo długo. Aby umożliwić wykonanie programu w rozsądnym czasie program powinien posiadać ograniczenie w postaci parametru “timeout” ustawionego domyślnie na 30 sekund. W przypadku nie otrzymania ostatecznego wyniku w założonym czasie program powinien zwrócić wynik cząstkowy (np “złożoność gorsza niż O(n)”).

Program powinien dać się zainstalować jako pakiet pip bezpośrednio z repozytorium (np używając komendy 
`pip install git+https://github.com/AGHPythonCourse2017/zad01-grzanka.git`)

Program powinien wykorzystywać następujące elementy:
 - Logger
 - dekoratory
 - własne wyjątki

Program powinien przejść test flake8 (zgodność z PEP8).

Za wykonania zadania mozna zdobyc maksymalnie 0.9 punktu.

Dodatkowo trzeba wykonać trzy recenzje rozwiązań zadania nr 1 i umieścić w repozytorium w pliku review.txt odnośniki do odpowiednich “Pull request”. Ten fragment zadania umożliwia zdobycie maksymalnie 0.1 punktu.

Tresc zadania w Google Drive: https://goo.gl/r87sPE

Termin oddania zadania: 8 maja 2017, 20:00
