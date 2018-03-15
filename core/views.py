from django.shortcuts import render


def hi(request, n1, n2):
    return render(request, 'hi.html', {
        's': n1 + n2
    })


def r(request, begin, end):
    if begin > end:
        rr = reversed(range(end, begin + 1))
    else:
        rr = range(begin, end + 1)

    return render(request, 'r.html', {
        'rr': rr
    })
