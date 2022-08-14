from multiprocessing.sharedctypes import Value
import mingus.core.chords as chords

# Triads: ‘m’, ‘M’ or ‘’, ‘dim’.
# Sevenths: ‘m7’, ‘M7’, ‘7’, ‘m7b5’, ‘dim7’, ‘m/M7’ or ‘mM7’
# Augmented chords: ‘aug’ or ‘+’, ‘7#5’ or ‘M7+5’, ‘M7+’, ‘m7+’, ‘7+’
# Suspended chords: ‘sus4’, ‘sus2’, ‘sus47’, ‘sus’, ‘11’, ‘sus4b9’ or ‘susb9’
# Sixths: ‘6’, ‘m6’, ‘M6’, ‘6/7’ or ‘67’, 6/9 or 69
# Ninths: ‘9’, ‘M9’, ‘m9’, ‘7b9’, ‘7#9’
# Elevenths: ‘11’, ‘7#11’, ‘m11’
# Thirteenths: ‘13’, ‘M13’, ‘m13’
# Altered chords: ‘7b5’, ‘7b9’, ‘7#9’, ‘67’ or ‘6/7’
# Special: ‘5’, ‘NC’, ‘hendrix’
topics = {
    '1':'Building Chords and extensions'
}

def find_topic(input):
    try:
        return topics[f'{input}']
    except KeyError:
        return list(topics.keys())[list(topics.values()).index(f'{input}')]



quiz_1 = {
    'q1':chords.triads("F")[0],
    'q2':[chords.determine(["A", "C", "E", "G"], True)[0]],
    'q3':chords.from_shorthand("Cm7"),
    'q4':chords.from_shorthand("D7b9"),
    'q5':chords.determine(["G", "B", "D", "F", "A#"])
}



def quiz_1_answers(q):
    return quiz_1[f"q{q}"]

def grade(user_answers):
    grade = 0
    q = 1
    for answer in user_answers:
        if str(answer) == str(quiz_1_answers(q)):
            grade += 1
        print(f"User answer: {answer}, correct answer: {quiz_1_answers(q)}")
        q += 1
    print(grade)
    return grade
