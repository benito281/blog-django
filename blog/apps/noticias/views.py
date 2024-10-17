from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from .models import Noticia, Categoria
from .forms import Formulario_Noticia, Formulario_Modificar_Noticia
from apps.comentarios.models import Comentario


def Home_Noticias(request):
    contexto = {}

    contexto["categorias"] = Categoria.objects.all()

    filtro = request.GET.get("categoria", "0")
    orden = request.GET.get("orden", "-creado")
    busqueda = request.GET.get("q", "")

    todas = Noticia.objects.all()

    if filtro and filtro != "0":
        todas = todas.filter(categorias__id=filtro)

    if busqueda:
        todas = todas.filter(titulo__icontains=busqueda) | todas.filter(
            contenido__icontains=busqueda
        )

    # Ordenar las noticias
    if orden == "titulo_asc":
        todas = todas.order_by("titulo")
    elif orden == "titulo_desc":
        todas = todas.order_by("-titulo")
    elif orden == "creado_asc":
        todas = todas.order_by("creado")
    else:  # Default to descending creation date
        todas = todas.order_by("-creado")

    paginator = Paginator(todas, 5)
    page = request.GET.get("page")

    try:
        noticias = paginator.page(page)
    except PageNotAnInteger:
        noticias = paginator.page(1)
    except EmptyPage:
        noticias = paginator.page(paginator.num_pages)

    contexto["noticias_populares"] = Noticia.objects.order_by("-visitas")[:3]
    contexto["noticias"] = noticias

    return render(request, "noticias/home_noticias.html", contexto)

class Cargar_noticia(LoginRequiredMixin, CreateView):
    model = Noticia
    template_name = "noticias/cargar_noticia.html"
    form_class = Formulario_Noticia
    success_url = reverse_lazy("noticias:home_noticias")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class Modificar_noticia(LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin, UpdateView):
    model = Noticia
    template_name = "noticias/modificar_noticia.html"
    form_class = Formulario_Modificar_Noticia
    success_url = reverse_lazy("noticias:home_noticias")
    permission_required = 'noticias.change_noticia'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def test_func(self):
        noticia = self.get_object()
        return self.request.user == noticia.usuario or self.request.user.groups.filter(name='colaborador').exists()

    def handle_no_permission(self):
        noticia = self.get_object()
        return redirect("noticias:detalle_noticia", pk=noticia.pk)

    def has_permission(self):
        # Permitir a los colaboradores editar cualquier noticia
        return self.request.user.has_perm('noticias.change_noticia')

class Borrar_noticia(PermissionRequiredMixin, DeleteView):
    model = Noticia
    permission_required = 'noticias.delete_noticia'

    def get_success_url(self):
        return reverse_lazy("noticias:home_noticias")
        
    def delete(self, request, *args, **kwargs):
        noticia = self.get_object()
        if request.user == noticia.usuario or request.user.groups.filter(name='colaborador').exists():
            
            return super().delete(request, *args, **kwargs)
        else:
            
            return HttpResponseRedirect(self.get_success_url())
    
    def has_permission(self):
        # Permitir a los colaboradores eliminar cualquier noticia
        return self.request.user.has_perm('noticias.delete_noticia')



def Detalle_noticia(request, pk):
    ctx = {}
    noticia = get_object_or_404(Noticia, pk=pk)

    noticia.visitas += 1
    noticia.save()

    ctx["likes"] = noticia.count_likes()
    ctx["noticia"] = noticia
    ctx["checklike"] = request.user in noticia.likes.all()
    com = Comentario.objects.filter(noticia=noticia)
    ctx["comentarios"] = com
    return render(request, "noticias/detalle_noticia.html", ctx)


def megusta(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.user in noticia.likes.all():
        noticia.likes.remove(request.user)
    else:
        noticia.likes.add(request.user.id)
    return redirect("/noticias/Detalle/" + str(noticia.id))
