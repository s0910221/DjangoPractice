from django.shortcuts import render


def hi(request, n1, n2):
    return render(request, 'hi.html', {
        's': n1 + n2
    })

def r(request, begin, end, option = None):
    if begin > end:
        rr = reversed(range(end, begin + 1))
    else:
        rr = range(begin, end + 1)
    if option == 0:
        rr = filter(lambda x : x % 2 == 0, rr)
    elif option == 1:
        rr = filter(lambda x : x % 2 == 1, rr)

    return render(request, 'r.html', {
        'rr': rr
    })

def tag_test(request):
    l = [1,2,3,4,5,6,7,8,9]
    return render(request, 'tag_test.html', {
        'l': l
    })