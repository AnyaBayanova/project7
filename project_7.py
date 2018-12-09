def vmor():
    us = input('Введите обычный текст на русском: ').lower()
    m = []
    for l in us:
        if l == 'а':
            l = '*-'
            m.append(l)
            print(l, end=' ')
        elif l == 'б':
            l = '-***'
            m.append(l)
            print(l, end=' ')
        elif l == 'в':
            l = '*--'
            m.append(l)
            print(l, end=' ')
        elif l == 'г':
            l = '--*'
            m.append(l)
            print(l, end=' ')
        elif l == 'д':
            l = '-**'
            m.append(l)
            print(l, end=' ')
        elif l == 'е':
            l = '*'
            m.append(l)
            print(l, end=' ')
        elif l == 'ё':
            l = '*'
            m.append(l)
            print(l, end=' ')
        elif l == 'ж':
            l = '***-'
            m.append(l)
            print(l, end=' ')
        elif l == 'з':
            l = '--**'
            m.append(l)
            print(l, end=' ')
        elif l == 'и':
            l = '**'
            m.append(l)
            print(l, end=' ')
        elif l == 'й':
            l = '*--'
            m.append(l)
            print(l, end=' ')
        elif l == 'к':
            l = '-*-'
            m.append(l)
            print(l, end=' ')
        elif l == 'л':
            l = '*-**'
            m.append(l)
            print(l, end=' ')
        elif l == 'м':
            l = '--'
            m.append(l)
            print(l, end=' ')
        elif l == 'н':
            l = '-*'
            m.append(l)
            print(l, end=' ')
        elif l == 'о':
            l = '---'
            m.append(l)
            print(l, end=' ')
        elif l == 'п':
            l = '*--*'
            m.append(l)
            print(l, end=' ')
        elif l == 'р':
            l = '*-*'
            m.append(l)
            print(l, end=' ')
        elif l == 'с':
            l = '***'
            m.append(l)
            print(l, end=' ')
        elif l == 'т':
            l = '-'
            m.append(l)
            print(l, end=' ')
        elif l == 'у':
            l = '**-'
            m.append(l)
            print(l, end=' ')
        elif l == 'ф':
            l = '**-*'
            m.append(l)
            print(l, end=' ')
        elif l == 'х':
            l = '****'
            m.append(l)
            print(l, end=' ')
        elif l == 'ц':
            l = '-*-*'
            m.append(l)
            print(l, end=' ')
        elif l == 'ч':
            l = '---*'
            m.append(l)
            print(l, end=' ')
        elif l == 'ш':
            l = '----'
            m.append(l)
            print(l, end=' ')
        elif l == 'щ':
            l = '--*-'
            m.append(l)
            print(l, end=' ')
        elif l == 'ъ':
            l = '--*--'
            m.append(l)
            print(l, end=' ')
        elif l == 'ы':
            l = '-*--'
            m.append(l)
            print(l, end=' ')
        elif l == 'ь':
            l = '-**-'
            m.append(l)
            print(l, end=' ')
        elif l == 'э':
            l = '**-**'
            m.append(l)
            print(l, end=' ')
        elif l == 'ю':
            l = '**--'
            m.append(l)
            print(l, end=' ')
        elif l == 'я':
            l = '*-*-'
            m.append(l)
            print(l, end=' ')
        elif l == '0':
            l = '-----'
            m.append(l)
            print(l, end=' ')
        elif l == '1':
            l = '*----'
            m.append(l)
            print(l, end=' ')
        elif l == '2':
            l = '**---'
            m.append(l)
            print(l, end=' ')
        elif l == '3':
            l = '***--'
            m.append(l)
            print(l, end=' ')
        elif l == '4':
            l = '****-'
            m.append(l)
            print(l, end=' ')
        elif l == '5':
            l = '*****'
            m.append(l)
            print(l, end=' ')
        elif l == '6':
            l = '-****'
            m.append(l)
            print(l, end=' ')
        elif l == '7':
            l = '--***'
            m.append(l)
            print(l, end=' ')
        elif l == '8':
            l = '---**'
            m.append(l)
            print(l, end=' ')
        elif l == '9':
            l = '----*'
            m.append(l)
            print(l, end=' ')
        elif l == '.':
            l = '******'
            m.append(l)
            print(l, end=' ')
        elif l == ',':
            l = '*-*-*-'
            m.append(l)
            print(l, end=' ')
        elif l == ':':
            l = '---***'
            m.append(l)
            print(l, end=' ')
        elif l == ';':
            l = '-*-*-'
            m.append(l)
            print(l, end=' ')
        elif l == '(':
            l = '-*--*-'
            m.append(l)
            print(l, end=' ')
        elif l == ')':
            l = '-*--*-'
            m.append(l)
            print(l, end=' ')
        elif l == '—':
            l = '-****-'
            m.append(l)
            print(l, end=' ')
        elif l == '/':
            l = '-**-*'
            m.append(l)
            print(l, end=' ')
        elif l == '?':
            l = '**--**'
            m.append(l)
            print(l, end=' ')
        elif l == '!':
            l = '--**--'
            m.append(l)
            print(l, end=' ')
        elif l == ' ':
            l = '  '
            m.append(l)
            print(l, end='')
    return m
def vtext():
    us = list(input('Введите код Морзе: ').lower().split())
    m = []
    for l in us:
        if l == '*-':
            l = 'а'
            m.append(l)
            print(l, end=' ')
        elif l == '-***':
            l = 'б'
            m.append(l)
            print(l, end=' ')
        elif l == '*--':
            l = 'в'
            m.append(l)
            print(l, end=' ')
        elif l == '--*':
            l = 'г'
            m.append(l)
            print(l, end=' ')
        elif l == '-**':
            l = 'д'
            m.append(l)
            print(l, end=' ')
        elif l == '*':
            l = 'е'
            m.append(l)
            print(l, end=' ')
        elif l == '*':
            l = 'ё'
            m.append(l)
            print(l, end=' ')
        elif l == '***-':
            l = 'ж'
            m.append(l)
            print(l, end=' ')
        elif l == '--**':
            l = 'з'
            m.append(l)
            print(l, end=' ')
        elif l == '**':
            l = 'и'
            m.append(l)
            print(l, end=' ')
        elif l == '*--':
            l = 'й'
            m.append(l)
            print(l, end=' ')
        elif l == '-*-':
            l = 'к'
            m.append(l)
            print(l, end=' ')
        elif l == '*-**':
            l = 'л'
            m.append(l)
            print(l, end=' ')
        elif l == '--':
            l = 'м'
            m.append(l)
            print(l, end=' ')
        elif l == '-*':
            l = 'н'
            m.append(l)
            print(l, end=' ')
        elif l == '---':
            l = 'о'
            m.append(l)
            print(l, end=' ')
        elif l == '*--*':
            l = 'п'
            m.append(l)
            print(l, end=' ')
        elif l == '*-*':
            l = 'р'
            m.append(l)
            print(l, end=' ')
        elif l == '***':
            l = 'с'
            m.append(l)
            print(l, end=' ')
        elif l == '-':
            l = 'т'
            m.append(l)
            print(l, end=' ')
        elif l == '**-':
            l = 'у'
            m.append(l)
            print(l, end=' ')
        elif l == '**-*':
            l = 'ф'
            m.append(l)
            print(l, end=' ')
        elif l == '****':
            l = 'х'
            m.append(l)
            print(l, end=' ')
        elif l == '-*-*':
            l = 'ц'
            m.append(l)
            print(l, end=' ')
        elif l == '---*':
            l = 'ч'
            m.append(l)
            print(l, end=' ')
        elif l == '----':
            l = 'ш'
            m.append(l)
            print(l, end=' ')
        elif l == '--*-':
            l = 'щ'
            m.append(l)
            print(l, end=' ')
        elif l == '--*--':
            l = 'ъ'
            m.append(l)
            print(l, end=' ')
        elif l == '-*--':
            l = 'ы'
            m.append(l)
            print(l, end=' ')
        elif l == '-**-':
            l = 'ь'
            m.append(l)
            print(l, end=' ')
        elif l == '**-**':
            l = 'э'
            m.append(l)
            print(l, end=' ')
        elif l == '**--':
            l = 'ю'
            m.append(l)
            print(l, end=' ')
        elif l == '*-*-':
            l = 'я'
            m.append(l)
            print(l, end=' ')
        elif l == '-----':
            l = '0'
            m.append(l)
            print(l, end=' ')
        elif l == '*----':
            l = '1'
            m.append(l)
            print(l, end=' ')
        elif l == '**---':
            l = '2'
            m.append(l)
            print(l, end=' ')
        elif l == '***--':
            l = '3'
            m.append(l)
            print(l, end=' ')
        elif l == '****-':
            l = '4'
            m.append(l)
            print(l, end=' ')
        elif l == '*****':
            l = '5'
            m.append(l)
            print(l, end=' ')
        elif l == '-****':
            l = '6'
            m.append(l)
            print(l, end=' ')
        elif l == '--***':
            l = '7'
            m.append(l)
            print(l, end=' ')
        elif l == '---**':
            l = '8'
            m.append(l)
            print(l, end=' ')
        elif l == '----*':
            l = '9'
            m.append(l)
            print(l, end=' ')
        elif l == '******':
            l = '.'
            m.append(l)
            print(l, end=' ')
        elif l == '*-*-*-':
            l = ','
            m.append(l)
            print(l, end=' ')
        elif l == '---***':
            l = ':'
            m.append(l)
            print(l, end=' ')
        elif l == '-*-*-':
            l = ';'
            m.append(l)
            print(l, end=' ')
        elif l == '-*--*-':
            l = '('
            m.append(l)
            print(l, end=' ')
        elif l == '-*--*-':
            l = ')'
            m.append(l)
            print(l, end=' ')
        elif l == '-****-':
            l = '-'
            m.append(l)
            print(l, end=' ')
        elif l == '-**-*':
            l = '/'
            m.append(l)
            print(l, end=' ')
        elif l == '**--**':
            l = '?'
            m.append(l)
            print(l, end=' ')
        elif l == '--**--':
            l = '!'
            m.append(l)
            print(l, end=' ')
        elif l == '   ':
            l = ' '
            m.append(l)
            print(l, end=' ')
    return m
def choice():
    print('Выберите, что вы хотите сделать:')
    v = str(input(' Из текста в код Морзе - 1\n Из кода Морзе в текст - 2\n'))
    if v == '1':
        vmor()
    elif v == '2':
        vtext()
    else:
        choice()

choice()
