from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'index.html')


def analyzer(request):
    # Get the input text
    input_text = request.GET.get('input_text', 'default')

    # Get the checkbox data
    removepunc = request.GET.get('removepunc', 'off')
    cap = request.GET.get('cap', 'off')
    lower = request.GET.get('lower', 'off')
    space = request.GET.get('space', 'off')

    if removepunc == 'on':
        # Define punctuation characters
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~—'''

        # Initialize the variable to store analyzed text
        analyzed = ''

        # Remove punctuation characters from input text
        for char in input_text:
            if char not in punctuation:
                analyzed += char

        # Prepare context for rendering
        params = {'purpose': 'remove punctuation', 'analyzed_text': analyzed, 'origional_text': input_text}

        # Render the analyzed text
        return render(request, 'analyzed.html', params)
    elif cap == 'on':
        # Intialize the variable to store analyzed text
        analyzed = ''

        # Change the lower to uppercase
        for char in input_text:
            analyzed = analyzed + char.upper()

        # prepare context for redring
        params = {'purpose': 'change to Upper', 'analyzed_text': analyzed, 'origional_text': input_text}
        return render(request, 'analyzed.html', params)

    elif space == 'on':
        # initializing the variable to store the analyzed text
        analyzed = ''

        # Removing the exrta space
        input_text = input_text.split()
        analyzed = ' '.join(input_text)
        # Prepare context for redering
        params = {'purpose': 'Remove extra space', 'analyzed_text': analyzed, 'origional_text': input_text}
        return render(request, 'analyzed.html', params)

    elif lower == 'on':
        # Intialize the variable to store analyzed text
        analyzed = ''

        # Change the uppercase lower case
        for char in input_text:
            analyzed = analyzed + char.lower()

        # prepare context for redring
        params = {'purpose': 'change to lower', 'analyzed_text': analyzed, 'origional_text': input_text}
        return render(request, 'analyzed.html', params)


def about(request):
    return render(request, 'about.html')
