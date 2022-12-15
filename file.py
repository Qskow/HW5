#1

print("""Проверьте свой пароль на безопасность

-Должен быть не менее 6 символов;
-Должен содержать хотя бы одну цифру;
-Не должен состоять только из цифр;
-Не должен содержать слово “password” в любом регистре.""")

def pass_check(a):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    try:
        assert(len(a) > 6)
        assert(any(num.isdigit() for num in a))
        assert(not a.isdigit())
        assert("password" not in a and "PASSWORD" not in a and "Password" not in a)
    except:
        return False
    else:
        return True

password = input("Введите пароль: ")
pass_check(password)

if pass_check(password) == True:
    print("Пароль подходит")
else:
    print("Пароль введен неправильно")

#2

def sum(*args):
    n = 0
    for i in args:
        n += i
    return n

print(sum())

#3

def fiba(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fiba(n - 1) + fiba(n - 2)

print(fiba(1))