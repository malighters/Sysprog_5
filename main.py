from src.yacc import parser


def main():
    print('Лаб 5. Lex/Yacc-парсер \nВиконав студент групи ТТП-32 Черненко Євгеній')
    while True:
        try:
            s = input('Вираз: ')
        except EOFError:
            break
        except SyntaxError:
            continue
        if s == 'quit':
            break
        if not s:
            continue
        result = parser.parse(s)
        if result is not None and len(result) == 1:
            result = result[0]
        print('Результат виконання:', result, '\n')



if __name__ == '__main__':
    main()
