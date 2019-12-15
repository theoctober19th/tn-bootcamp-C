a = 5
b = 0

try:
    print(a/b)
    print('haha')
except ZeroDivisionError:
    print('0 halna painna')
except:
    print('ma sakdina')
finally:
    print('malai kasaile rokdaina')

print('program did not stop')