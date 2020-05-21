## Дані

Дані зібрані з розділу "ТВ, Аудіо/Відео, Фото". Статистика по даним:

-   всього зібрано 59644 відгуків
-   з них 29171 відгуків з рейтингом або заповненими секціями "переваги"/"недоліки"
-   з них 5830 українською мовою

В результаті кластеризації даних за сентиментами було отримано наступний розподіл за сегментами:
- pos: 7163
- neg: 4115
- neut: 1643

Всі відгуки [тут](./rozetka_all.zip), yкраїнською [тут](./rozetka_uk.json)


## Проблеми
Основні проблеми: а) мало даних, б) мало даних у нейтральному сегменті
Першу проблему намагалась вирішити перекладами, але мене швидко забанила гугл транслейт апішка :) Другу проблему трошки вдалось порішати, фільтруючи "переваги" і "недоліки" на предмет можливо нейтрального тексту


## Підхід

Оскільки іноді я читаю невідомо чим, то провтикала такі нюанси, як крос-валідація і що треба **вибрати** класифікатор, а не **написати**. І звернула увагу на це аж майже в останній момент 🙁 Тому, як навіжена, пиляла Naive Bayes класифікатор (ну але, оскільки не доімплементувала його на практичному занятті, то доробила тут, сподіваюсь, більш-менш вірно). В кінці я таки використала трохи магії з `sklearn`, правда, ну от взагалі не впевнена у правильності дій, бо послуговуалась в основному гуглом і не до кінця поки розумію, що воно під капотом робить

## Ітерації

Кожна наступна ітерація є кумулятивною (оперує на результаті попередньої, окрім n-gramms, там були опробувані всі варіанти)

### Tokenization

-   classification report

```
              precision    recall  f1-score   support

         neg       0.90      0.34      0.49      1241
        neut       0.72      0.06      0.12       489
         pos       0.63      0.98      0.76      2147

    accuracy                           0.66      3877
   macro avg       0.75      0.46      0.46      3877
weighted avg       0.73      0.66      0.60      3877
```

-   cross-validation report

```
             precision recall f1-score
pos               0.74   0.95     0.83
neut               0.5    0.2     0.29
neg               0.81   0.61      0.7
                                      
accuracy                          0.75
macro avg         0.68   0.59     0.61
weighted avg      0.73   0.75     0.72
```

### Lowercasing

-   classification report

```
              precision    recall  f1-score   support

         neg       0.91      0.35      0.50      1241
        neut       0.62      0.04      0.07       489
         pos       0.63      0.98      0.77      2147

    accuracy                           0.66      3877
   macro avg       0.72      0.46      0.45      3877
weighted avg       0.72      0.66      0.59      3877
```

-   cross-validation report

```
             precision recall f1-score
pos               0.74   0.95     0.83
neut               0.5    0.2     0.29
neg               0.81   0.61      0.7
                                      
accuracy                          0.75
macro avg         0.68   0.59     0.61
weighted avg      0.73   0.75     0.72
```

дивно, чомусь тут метрики погіршились

### Lemmatization

-   classification report

```
              precision    recall  f1-score   support

         neg       0.89      0.34      0.49      1241
        neut       0.47      0.01      0.03       489
         pos       0.62      0.99      0.76      2147

    accuracy                           0.66      3877
   macro avg       0.66      0.45      0.43      3877
weighted avg       0.69      0.66      0.58      3877
```

-   cross-validation report

```
             precision recall f1-score
pos               0.77   0.94     0.84
neut              0.49   0.23     0.31
neg               0.79   0.66     0.72
                                      
accuracy                          0.76
macro avg         0.68   0.61     0.63
weighted avg      0.74   0.76     0.74
```


### Filtering symbols, punctuation, latin words, nums

-   classification report

```
              precision    recall  f1-score   support

         neg       0.81      0.40      0.54      1241
        neut       0.17      0.01      0.01       489
         pos       0.65      0.98      0.78      2147

    accuracy                           0.67      3877
   macro avg       0.54      0.46      0.44      3877
weighted avg       0.64      0.67      0.60      3877
```

-   cross-validation report

```
             precision recall f1-score
pos               0.77   0.93     0.84
neut              0.41   0.15     0.22
neg               0.76   0.67     0.71
                                      
accuracy                          0.75
macro avg         0.65   0.58     0.59
weighted avg      0.72   0.75     0.72
```

 шось не то
 

### Processing negations

-   classification report

```
              precision    recall  f1-score   support

         neg       0.83      0.45      0.59      1241
        neut       0.32      0.02      0.03       489
         pos       0.66      0.98      0.79      2147

    accuracy                           0.69      3877
   macro avg       0.60      0.48      0.47      3877
weighted avg       0.67      0.69      0.63      3877
```

-   cross-validation report

```
             precision recall f1-score
pos               0.79   0.93     0.85
neut              0.46   0.18     0.25
neg               0.78   0.72     0.75
                                      
accuracy                          0.77
macro avg         0.68   0.61     0.62
weighted avg      0.74   0.77     0.74
```

я покладала більші надії на цей метод, ну але, мабуть, не до кінця його "прожарила", або десь помилилась, бо заперечень у даних вистачає


### n-grams

Тут я поєднувала н-грами з іншими (кумулятивними) процесорами

1. with lowerizing

-   classification report

```
              precision    recall  f1-score   support

         neg       0.89      0.31      0.46      1241
        neut       1.00      0.02      0.04       489
         pos       0.62      0.99      0.76      2147

    accuracy                           0.65      3877
   macro avg       0.83      0.44      0.42      3877
weighted avg       0.75      0.65      0.57      3877
```

-   cross-validation report

```
             precision recall f1-score
pos               0.82   0.85     0.84
neut              0.41   0.39      0.4
neg               0.76   0.72     0.74
                                      
accuracy                          0.75
macro avg         0.66   0.66     0.66
weighted avg      0.75   0.75     0.75
```

чогось такоє...

2. with lemmatization

-   classification report

```
              precision    recall  f1-score   support

         neg       0.88      0.33      0.48      1241
        neut       0.00      0.00      0.00       489
         pos       0.62      0.99      0.76      2147

    accuracy                           0.65      3877
   macro avg       0.50      0.44      0.41      3877
weighted avg       0.62      0.65      0.57      3877
```

шось зовсім пішло не так...


-   cross-validation report

```
             precision recall f1-score
pos               0.82   0.85     0.84
neut               0.4   0.36     0.38
neg               0.75   0.73     0.74
                                      
accuracy                          0.75
macro avg         0.66   0.65     0.65
weighted avg      0.74   0.75     0.75
```


3. with stop-words filtering

-   classification report

```
              precision    recall  f1-score   support

         neg       0.81      0.35      0.49      1241
        neut       0.00      0.00      0.00       489
         pos       0.63      0.98      0.77      2147

    accuracy                           0.66      3877
   macro avg       0.48      0.44      0.42      3877
weighted avg       0.61      0.66      0.58      3877
```

-   cross-validation report

```
             precision recall f1-score
pos               0.83   0.83     0.83
neut              0.33   0.32     0.33
neg               0.72   0.73     0.72
                                      
accuracy                          0.73
macro avg         0.63   0.63     0.63
weighted avg      0.73   0.73     0.73
```

... і тут...

4. with negation processing

-   classification report

```
              precision    recall  f1-score   support

         neg       0.80      0.35      0.49      1241
        neut       0.00      0.00      0.00       489
         pos       0.63      0.98      0.77      2147

    accuracy                           0.66      3877
   macro avg       0.48      0.45      0.42      3877
weighted avg       0.61      0.66      0.58      3877
```

-   cross-validation report

```
             precision recall f1-score
pos               0.83   0.84     0.84
neut              0.33   0.31     0.32
neg               0.73   0.73     0.73
                                      
accuracy                          0.74
macro avg         0.63   0.63     0.63
weighted avg      0.73   0.74     0.73
```

... теж ...

5. without any additional preprocessing

-   classification report

```
              precision    recall  f1-score   support

         neg       0.87      0.34      0.49      1241
        neut       1.00      0.02      0.05       489
         pos       0.63      0.98      0.76      2147

    accuracy                           0.66      3877
   macro avg       0.83      0.45      0.43      3877
weighted avg       0.75      0.66      0.59      3877
```

-   cross-validation report

```
             precision recall f1-score
pos               0.81   0.87     0.84
neut              0.43   0.35     0.38
neg               0.76   0.72     0.74
                                      
accuracy                          0.76
macro avg         0.67   0.65     0.66
weighted avg      0.75   0.76     0.75
```

як не дивно, але це найкращий результат серед "н-грамних" (якщо я нічого не плутаю), і можна зробити висновок, що з н-грамами краще не поєднувати інші текст процесори. але все одно результати погані. пробувала біграми - не допомогло
