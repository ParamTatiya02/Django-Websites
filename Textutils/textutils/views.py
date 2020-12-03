# This is created
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def analyze(request):
    dj_text = request.POST.get('text', 'default')
    remove_punctuation = request.POST.get('remove_punctuation', 'off')
    full_caps = request.POST.get('full_caps', 'off')
    new_line_remover = request.POST.get('new_line_remover', 'off')
    extra_space_remover = request.POST.get('extra_space_remover', 'off')
    str_1 = dj_text
    purpose = ""

    if remove_punctuation == "on":
        punctuation = '''!()-[];:'",<>./?@#$%^&*_~'''
        analyzed = ""
        for char in dj_text:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose': 'Remove punctuation', 'analyzed_text': analyzed}
        str_1 = analyzed
        purpose += " | Remove punctuation "
    if full_caps == "on":
        print("2", str_1)
        str_1 = str_1.upper()
        params = {'purpose': 'Changed to UPPERCASE', 'analyzed_text': str_1}
        purpose += "| Caps |"
    if new_line_remover == "on":
        analyzed = ""
        for char in str_1:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed new line', 'analyzed_text': analyzed}
        str_1 = analyzed
        purpose += "| remove new line "
    if extra_space_remover == "on":
        analyzed = ""
        for i, char in enumerate(str_1):
            if str_1[i] == " " and str_1[i+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Extra space remover', 'analyzed_text': analyzed}
        str_1 = analyzed
        purpose += "| Spaces remove |"
    params = {'purpose': purpose, 'analyzed_text': str_1}
    if remove_punctuation == "on" or full_caps == "on" or new_line_remover == "on" or extra_space_remover == "on":
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('error')
