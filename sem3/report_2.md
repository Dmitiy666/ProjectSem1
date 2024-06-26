# Отчет 2. Исследование метода Q-learning в среде Frozen Lake 

## 1. Сравнение алгоритмов V и Q learning (2 балла)
Для алгоритма `V learning` на поле (4х4) при `gamma=0.9` сходимость (mean reward > 0.85)

достигается в среднем за 33 итерации (от 16 до 83). 

Графики зависимости reward от количества итераций приведены ниже. 

<img src="image/V.PNG"/>

Для алгоритма `Q learning` на поле (4х4) при `gamma=0.9` сходимость (mean reward > 0.9)

достигается в среднем за 20 итерации (от 16 до 56). 

Графики зависимости reward от количества итераций приведены ниже. 

<img src="image/Q.PNG"/>
в
**Вывод:**** У алгоритма V learning сходиомсть достигается за 33 иттераций,

у алгоритма Q learning сходимость достигается за 20 иттераций, а средняя награда 0,9

в отличии от алгоритма ценностей, который быстрее достигает сходимости,

но с меньшей наградой. То есть если нам важна скорость обучения - 

лучшим вариантом будет алгоритм ценностей V learning, в случае если же нам 

более важно качество алгоритма, я бы предпочел - алгоритм действий Q learning.



## 2. Влияние гиперпараметра `GAMMA` на скорость сходимости . (2 балла)

Для алгоритма `Q learning` на поле (4х4) при `gamma=0.8` сходимость (mean reward > 0.9) достигается в среднем за 84 итерации (от 26 до 140). 

Графики зависимости reward от количества итераций приведены ниже. 

<img src="image/3S.PNG"/>

Для алгоритма `V learning` на поле (4х4) при `gamma=0.8` сходимость (mean reward > 0.85) достигается в среднем за 20 итерации (от 14 до 27). 

Графики зависимости reward от количества итераций приведены ниже. 

**Вывод:** Увеличение гиперпараметра `GAMMA` приводит к уменьшению количества иттераций 

Это связано с тем, что гамма отвечает за то на сколько агент будет жадным

Уменьшая параметр гамма агент делается более жадным, поэтому требуется больше времени

<img src="image/3SS.PNG"/>

## 3. Сравнение алгоритмов V и Q learning на поле большего размера (3 балла)

Для алгоритма Q learning на поле (8х8) при gamma=0.9 сходимость (mean reward > 0.9) достигается в

среднем за 290 итераций (от 100 до 480). Графики зависимости reward от количества итераций приведены ниже.

<img src="image/s4q.PNG"/>

Для алгоритма V learning на поле (8х8) при gamma=0.9 сходимость (mean reward > 0.85) достигается в

среднем за 1015 итераций (от 580 до 1 450). Графики зависимости reward от количества итераций приведены ниже.

<img src="image/s4v.PNG"/>

**Вывод:**
: На большем поле агенту необходимо большее количество иттераций, чтобы достигнуть сходимости

При алгоритме действия сходимость достигается за 380 иттераций , 

а при алгоритме ценности за 870 иттераций
