from django.shortcuts import render

def viceversa(request):
    return render(
        request,
        'viceversa.html'
        )

def reverse(request):
    user_text = request.GET['reversedText']
    num_of_words = len(user_text.split())
    reversed_user_text = user_text[::-1]
    return render(
        request, 
        'reverse.html', 
        {'usertext':user_text,
        'reversedtext':reversed_user_text,
        'numberofwords':num_of_words}
        )
