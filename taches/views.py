from django.shortcuts import render , redirect , get_object_or_404 , HttpResponse
from django.urls import reverse , reverse_lazy
from django.views.generic import ListView , DetailView , CreateView , DeleteView , UpdateView
from .models import Taches , Categorie
from .forms import TacheForm , CategorieForm
from django.contrib.auth.mixins import LoginRequiredMixin




def Home(request):
    return render(request,'taches/home.html')

class TacheListView(ListView):
    model = Taches
    template_name = 'taches/tache_list.html'
    context_object_name = 'taches'

    def get_queryset(self):
        queryset = super().get_queryset()  # Obtenir le queryset de base

        # Filtrage par date d'échéance
        date_filtre = self.request.GET.get('date')
        if date_filtre:
            queryset = queryset.filter(date_echeance__date=date_filtre)

        # Filtrage par priorité
        priorite_filtre = self.request.GET.get('priorite')
        if priorite_filtre:
            queryset = queryset.filter(priorite=priorite_filtre)

        # Filtrage par catégorie (type de la catégorie)
        categorie_filtre = self.request.GET.get('q')  # Récupérer le terme de recherche de catégorie
        if categorie_filtre:
            # Utiliser la notation double underscore pour accéder au champ "type" de la catégorie associée
            queryset = queryset.filter(categorie__type__icontains=categorie_filtre)

        return queryset

class TacheCreateViewt(LoginRequiredMixin,CreateView):
    model = Taches
    form_class = TacheForm
    template_name = 'taches/tache_form.html'
    success_url = reverse_lazy('tache_list')

class TacheDetailView(DetailView):
    model = Taches
    template_name = 'taches/tache_detail.html'
    context_object_name = 'tache'

class TacheDeleteView(LoginRequiredMixin,DeleteView):
    model = Taches
    template_name = 'taches/tache_delete.html'
    success_url = reverse_lazy('tache_list')

class TacheUpdateView(LoginRequiredMixin,UpdateView):
    model = Taches
    form_class = TacheForm
    template_name = ('taches/tache_edit.html')
    success_url = reverse_lazy('tache_list')

class CategorieListView(ListView):
    model = Categorie
    template_name = 'taches/categorie_list.html'
    context_object_name = 'categories'
     

class CategorieCreateView(CreateView):
    model = Categorie
    form_class = CategorieForm
    template_name = 'taches/categorie_form.html'
    success_url = reverse_lazy('categorie_list')

class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = 'taches/categorie_delete.html'
    success_url = reverse_lazy('categorie_list')