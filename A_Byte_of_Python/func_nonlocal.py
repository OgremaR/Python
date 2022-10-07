def func_outer():
    x = 2
    print('x равно', x)

    def func_inner():
        x = 5
        print('local', x)

    func_inner()
    print('Локальное x сменилось на', x)
func_outer()