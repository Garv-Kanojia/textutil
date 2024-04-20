from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request , 'index.html')

def get_data(request):
    return request.POST.get('text','default')

def remove(request):
    line = get_data(request)
    punctuations = '''!()-[]}{;:'"\,<`+=>./?@#$%^&*_~'''
    line2 = line.split('\n')
    djtext = ''
    dict = []
    for i in line2:
        for j in i:
            if j not in punctuations:
                djtext += j
        dict.append(djtext)
        djtext = ''
    return render(request , 'analyze2.html' , {'text' : dict})

def upper(request):
    line = get_data(request)
    line2 = line.split('\n')
    dict = []
    for i in line2:
        dict.append(i.upper())
    return render(request , 'analyze2.html' , {'text' : dict})

def count(request):
    line = get_data(request)
    cnt = ['Number of words in your sentence are ' , len(line.split())]    
    return render(request , 'analyze2.html' , {'text' : cnt})

def lower(request):
    line = get_data(request)
    line2 = line.split('\n')
    dict = []
    for i in line2:
        dict.append(i.lower())
    return render(request , 'analyze2.html' , {'text' : dict})

def lined(request):
    line = get_data(request)
    djtext = ''
    for i in line:
        djtext += i
    djtext2 = [djtext,]
    return render(request , 'analyze2.html' , {'text' : djtext2})