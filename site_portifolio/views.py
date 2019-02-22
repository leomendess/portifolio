from django.shortcuts import render

# Create your views here.
def home(request):
    eu = {
        'nome': 'Leonardo'
        'nome': 'Leonardo'
        'nome': 'Leonardo'
    conhecimentos = ['HTML', 'CSS', 'JavaScript','Python', 'Django', 'Git', 'Tamborim', 'dar cambalhotas', 'Plantar Bananeira']
    return render(request, 'index.html', {'conhecimentos': conhecimentos, 'nome': nome})
