# streamlit run --server.runOnSave true app.py
#
import streamlit as st
import base64

from spacy import displacy

st.markdown(
"""
<style>
header .decoration {
  background-image: linear-gradient(90deg,#1eb4e9,#1eb4e9);
}
.reportview-container .main .block-container {
  padding: 0;
}
code {
  color: #e91e3a;
}
.st-c5 {
  border-color: #1eb4e9;
}
</style>
""", unsafe_allow_html=True)
#st.image('https://i.imgur.com/CJxBSYA.jpg', use_column_width=True)

st.title("🤦🏼‍♀️ Feminizer")
st.write('Фемінайзер виявляє проґавлені фемінітиви.')
st.write('')

samples = """\
Ека Згуладзе йде з посади першого заступника міністра внутрішніх справ
Я почала працювати програмістом на другому курсі навчання
Автором роботи є фотограф Ольга Баранець
Володя не був пияком розповіла кореспондентові Високого Замку голова Мечищівської сільради Євгенія Скрипецька
Важко поранені 22-річна оператор відеоспостереження й один засуджений
Юна дизайнер каже що на створення одягу її надихнули електрика концептуальне мистецтво та фільми Олександра Шапіро
Вона у нас як той дракон, що дихає вогнем і відлякує ворогів
Цього року в ній брали участь держсекретар Наталя, дружина президента США Мішель Обама, лауреати Нобелівської премії миру 2011 Лейма Гбоу і Тавакуль Карман
Першим тренером була Раїса Безсонова
Нагадаємо, раніше повідомлялося, що Україна направила країнам Митного союзу проект меморандуму про надання їй статусу спостерігача
Я проходила комісію щороку, я ж військовий льотчик
Президент зібрала екстрену нараду силовиків
Посол Великої Британії в Україні пані Джудіт Гоф розпочала нараду
Ота, що прибігала до тебе, вона теж студент?
Про це Телекритиці повідомила журналіст каналу Анастасія Станко
Вибори мера Києва відбудуться твердо цього року сказала лідер БЮТ
ГПУ викликала на допит народних депутатів від Опозиційного Блоку Наталю Королевську, Олександра Вілкула, а Вадима Новинського до МВС
За словами Наталії Сербин з громадської Народної ради страйк оголосили бо студенти мають певні права які не виконуються
Про це заявила керівник фракції Блоку Вітренко в Донецької обласній раді Наталія Білоцерківська
Був професором креативного письменництва в Університеті Аделаїди
Повідомлення про звільнення начальника відділу метеорологічних прогнозів Людмили Савченко є неправдивими
Під листом, у якому вимагається звільнити 30 заарештованих у Мурманську активістів Greenpeace, підписалися більше 16 тисяч осіб
Ініціатором проведення турніру під відкритим небом виступила промоутерська компанія Elite-Boxing
Партія висунула Юлію Тимошенко кандидатом на присудження Нобелівської премії миру
Згодом стала активним членом Спілки театральних діячів
""".splitlines()

#with open('directfem.txt.3') as f:
#    samples = [line.strip().split(':')[1] for line in f]

@st.cache(allow_output_mutation=True)
def load_nlp():
    import stanza
    from spacy_stanza import StanzaLanguage
    nlp = stanza.Pipeline(lang='uk')
    snlp = StanzaLanguage(nlp)
    return nlp, snlp

def write_svg(svg):
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    css = '<p style="text-align:center; display: flex; justify-content: left;">'
    html = r'<img style="padding-bottom:10px;" src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(css+html, unsafe_allow_html=True)

def write_svg1(svg):
    html = f'<figure>{svg}</figure>'
    st.write(html, unsafe_allow_html=True)

def cy(x):
    return displacy.render(x, options=dict(compact=True, collapse_phrases=True, word_spacing=15, distance=100))

@st.cache(allow_output_mutation=True)
def snlp(sentence):
    nlp, snlp = load_nlp()
    return snlp(sentence)

@st.cache(allow_output_mutation=True)
def nlp(sentence):
    nlp, snlp = load_nlp()
    return nlp(sentence)

import fem

@st.cache(allow_output_mutation=True)
def ignore():
    return {}
    #return {2, 3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 22, 23, 24, 25, 26, 27, 29, 32}

#st.write(ignore())

for i, s in enumerate(samples):
    if s[0] == '#':
        continue

    if i in ignore():
        continue

    #st.subheader(s)
    t = s
    s = st.text_input(s, s, key=f'edit{i}')
    if not s:
        continue
    if s != t:
        print('new:', s)
    #print(len(s), s)

    sent = nlp(s).sentences[0]

    ch = fem.children(sent)
    for p,r,o in fem.verify(sent):
        st.write((fem.fmt(p), r, fem.fmt(o)))
        if r == 'nsubj' and fem.case(o) == 'Acc':
            st.warning('Acc!')

    #if st.checkbox('ignore', value=i in ignore(), key=f'ignore{i}'):
    #    ignore().add(i)

    if st.checkbox('🤔', key=f'more{i}'):
        write_svg(cy(snlp(s)))
        st.write(['root'] + [fem.fmt(w, feats=True) for w in sent.words])

        st.write([(fem.fmt(f), r, fem.fmt(t)) for f,r,t in sent.dependencies])
