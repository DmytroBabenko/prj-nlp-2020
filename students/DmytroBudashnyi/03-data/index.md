# Дані

## I. Збір та анотування даних

1. Опрацюйте один із архівів Wiktionary і витягніть усі синонімні ряди для будь-якої мови. Будь ласка, не обирайте англійську, українську чи російську мови. Деталі задачі:
   * Не кожне слово матиме синоніми, тож витягайте лише ті слова, які мають синонімні ряди.
   * Останні архіви Wiktionary можна знайти на <https://dumps.wikimedia.org/backup-index.html>.
   * Використайте SAX-парсинг для цієї задачі.
   * У теці з вашим іменем збережіть програму та синонімні ряди, які вдалось дістати.

Програма і синонімічні ряди - [тут](./slovak_synonyms.ipynb)

2. Зайдіть на <http://ann.lisp.kiev.ua/>, знайдіть там теку з вашим іменем та проанотуйте 2 документи з корпусу БрУК на наявність іменованих сутностей. Перед анотуванням уважно прочитайте [інструкції з анотування](https://github.com/lang-uk/ner-uk/blob/master/doc/README.md).

Готово: [Проанотовано](http://ann.lisp.kiev.ua/ann/DmytroBudashnyi/)

3. Визначте рівень згоди між анотувальниками (або inter-annotator agreement) у корпусі [NUCLE Error Corpus](http://www.comp.nus.edu.sg/~nlp/conll14st.html#nucle32). Деталі задачі:

Можна вважати, що нічого не зробив. Я видалив з ноутбука весь код, що стосувався підрахунку, бо не встиг його довести до розуму: [все що є](./inter-annotator_agreement.ipynb)

## II. Робота над проєктом

1. Зберіть першу порцію даних для вашого проєкту та опишіть їх: формат, розмір, наявність розмітки, чи є якісь упередження (жанр, діалект, часовий проміжок). Докріпіть приклад даних (текст, файл тощо).

Дані зібрав скрейпером написаним з використанням `scrapy`, зберігаю для зручності в jsonlines форматі, вже зараз описиючи дані, зрозумів, що треба додати ще час, коли новина була додана.
[Приклад даних](./course_work_data_example.ipynb)

2(a). Якщо для вашого проєкту треба розмітити дані, розробіть анотаційний проєкт для ваших даних:
   - напишіть інструкцію для анотування з прикладами анотування
   - опишіть, як би ви могли автоматично покращити якість даних (розмітити частину даних, відфільтрувати погану розмітку, проранжувати приклади тощо)

Анотування, все ще залишається під питанням. Думаю працювати над rule-based анотуванням для початку, виділити певні ключові слова, які будуть описувати сутність або групу сутностей, якім мають описувати тему.
Ще хочу додати до статей метадані, які додають видання "Нагадуємо, ми вже писали ...". І для початку шукати вживання тих самих сутностей в заголовках.

Думав над ручним анотуванням, але в цьому випадку все найімовірніше зведеться до розмітки дуже гучних тем, як от "Коронавірус", і тоді мала кількість подій, об'єднаних спільним сюжетом, можуть залишитися без уваги.