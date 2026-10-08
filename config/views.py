from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto
from .forms import ProjetoForm

def listar_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos/listar.html', {
        'projetos': projetos
    })

def criar_projeto(request):
    form = ProjetoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_projetos')

    return render(request, 'projetos/form.html', {
        'form': form
    })

def editar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    form = ProjetoForm(
        request.POST or None,
        instance=projeto
    )

    if form.is_valid():
        form.save()
        return redirect('listar_projetos')

    return render(request, 'projetos/form.html', {
        'form': form
    })

def excluir_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        projeto.delete()
        return redirect('listar_projetos')

    return render(request,
                 'projetos/excluir.html',
                 {'projeto': projeto})