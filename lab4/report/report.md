---
## Front matter
title: "Отчёт по лабораторной работе №1"
subtitle: "Шифры простой замены"
author: "Артур Арменович Давтян"

## Generic options
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
  - spelling=modern
  - babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Ознакомиться с шифрами простой замены и обучиться их программной реализации.

# Задание

- Реализовать шифр Цезаря с произвольным ключом k;
- Реализовать шифр Атбаша.

# Теоретическое введение

При подготовке использовалась методичка со страницы курса в ТУИС.[@tuis:ru]

Шифр Цезаря является примером метода подстановки. Дальнейшее усовершенствование оригинального сдвига символа на три позиции в шифре Цезаря состоит в использовании арифметики по модулю двадцать шесть для ключа шифрования, который больше двадцати шести. 

$$ E_n(x) = (x + n) mod 26 $$, 

где $x$ - значение открытого текста, $n$ - номер сдвига. 

Шифр Цезаря со сдвигом 1 (рис. [-@fig:001]):

![Шифр Цезаря со сдвигом 1](image/1.png){ #fig:001 width=70% }

Шифр Атбаш -- шифр простой замены. Шифрование происходит заменой первой буквы алфавита на последнюю, второй на предпоследнюю, и так далее. По сути, это шифр сдвига на всю длину. Шифр Атбаш для русского алфавита (рис. [-@fig:002]):

![Шифр Атбаш](image/2.png){ #fig:002 width=70% }

# Выполнение лабораторной работы

Работа была выполнена на языке программирования Python.

Сначала реализуем шифр Цезаря (рис. [-@fig:003]):

![Программная реализация шифра Цезаря](image/3.png){ #fig:003 width=70% }

В переменную alph помещаем латинский алфавит. В переменную shalph задаём алфавит, который начинается с буквы, соответствующей числу сдвига, и прибавляем начало алфавита до этой буквы. Так как в таком случае при числе сдвига больше 26 и меньше -26 программа работать не будет, задаём условие, что в этом случае за число сдвига берется остаток от деления числа на 26. После этого создаём таблицу, в которой каждой букве исходного алфавита сопоставляется буква нового алфавита. В конце выводим зашифрованный текст с помощью метода str.translate, в который передаём таблицу.

Реализация шифра Атбаш (рис. [-@fig:004]):

![Программная реализация шифра Атбаш](image/4.png){ #fig:004 width=70% }

В переменную alph помещаем алфавит, но в этом случае, опираясь на [@tuis:ru] добавляем к нему пробел. В переменную shalph помещаем тот же алфавит, но перевёрнутый с помощью  функционала python. Создаём таблицу и выводим зашифрованный текст.

Ввод исходного текста и числа сдвига (рис. [-@fig:005]):

![Программная реализация шифрования](image/5.png){ #fig:005 width=70% }

Для ввода исходного текста вводим правило, что не может быть чисел, в противном случае просьба ввести текст будет выведена заново. Для ввода числа сдвига вводим правило, что не может быть букв, в противном случае просьба ввести число сдвига будет выведена заново. Если всё введено правильно, то будет выведен текст, зашифрованный с помощью шифра Цезаря и Атбаш (рис. [-@fig:006]):

![Вывод программы](image/6.png){ #fig:006 width=70% }

# Выводы

Ознакомился с шифрами простой замены и обучился их программной реализации.

# Список литературы{.unnumbered}

::: {#refs}
:::
