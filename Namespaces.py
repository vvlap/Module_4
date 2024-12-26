def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


test_function()
# при вызове inner_function() напрямую - выходит ошибка, внутренняя функция недоступна извне