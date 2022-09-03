# App de registro de producto - Vistas para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 19 -08 -2022

from django.shortcuts import render
from django.http import HttpResponse
from modprd.app_regprd.form import *
from django.urls import reverse_lazy
from modprd.app_regprd.models import *
from .models import *
from django.views.generic import *

#Vista principal del registro de productos 

class ini_regprd():
    def view_prd(request):
        return render(request, 'app_regprd_iu.html')

#----------VISTAS PARA EL REGISTRO DE PRODUCTOS SIGEPI------------

#Vista para el registro de producto

class vst_regprd(CreateView):
    model= prd_base
    form_class = form_reg_prd
    template_name ='mod_prd_frm_registrar.html'
    success_url = reverse_lazy('cn_prd')

    def get_queryset(self):
        return prd_base.objects.filter(id_usu =self.request.user)


#Vista para la seleccion de edicion de producto

class vst_selecprd(ListView):
    model= prd_base
    #form_class = form_selec_prd
    template_name ='con_trj_prd.html'
    success_url = reverse_lazy('cn_prd')
    context_object_name = 'Busqueda_prd'

    def get_queryset(self):
        return prd_base.objects.filter(ids_usu =self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'editar un producto'
        context['action'] = 'update'
        return context

#Vista para la edicion de un producto 

class vst_updprd(UpdateView):
    model= prd_base
    form_class = form_reg_prd
    template_name ='mod_prd_editar.html'
    success_url = reverse_lazy('cn_prd')

    def get_queryset(self):
        return prd_base.objects.filter(ids_usu =self.request.user)

#Vista para la eliminacion de un producto

class vst_delprd (DeleteView):
    model = prd_base
    template_name ='mod_prd_eliminar.html'
    success_url = reverse_lazy('cn_prd')

    def get_queryset(self):
        return prd_base.objects.filter(nom_prd =self.request.user)

#Vista para el registro de un requerimiento de existencia

class vst_regreqexist(CreateView):
    model= prd_req_Exist
    form_class = form_req_exist
    template_name ='mod_prd_frm_requexist.html'
    success_url = reverse_lazy('cn_prd')

    def get_queryset(self):
        return prd_req_Exist.objects.filter(nom_reqexs =self.request.user)

#Vista para el registro de un requerimiento de calidad

class vst_regreqcal(CreateView):
    model= prd_req_cal
    form_class = form_req_cal
    template_name ='mod_prd_frm_reqcal.html'
    success_url = reverse_lazy('cn_prd')

    def get_queryset(self):
        return prd_req_cal.objects.filter(id_categ =self.request.user)

# Vista para el registro del requerimiento de calidad
class vst_regreqcal(CreateView):
    model= prd_req_cal
    form_class = form_req_cal
    template_name ='mod_prd_frm_reqcal.html'
    success_url = reverse_lazy('cn_prd')

    def get_queryset(self):
        return prd_req_cal.objects.filter(id_categ =self.request.user)

# vista para el registro del requerimiento de la categoria
class vst_regcateg(CreateView):
    model= prd_categ
    form_class = form_categ
    template_name ='mod_prd_frm_categ.html'
    success_url = reverse_lazy('cn_prd')

    def get_queryset(self):
        return prd_req_cal.objects.filter(id_categ =self.request.user)

#vista para el registro de tipo 
class vst_regtipo(CreateView):
    model= prd_tipo
    form_class = form_tipo
    template_name ='mod_prd_frm_tipo.html'
    success_url = reverse_lazy('cn_prd')

    def get_queryset(self):
        return prd_req_cal.objects.filter(id_categ =self.request.user)

#Vista para el registro de campo 

class vst_regcampo(CreateView):
    model= campo
    form_class = form_campo
    template_name ='mod_prd_frm_campo.html'
    success_url = reverse_lazy('cn_prd')

    def get_queryset(self):
        return prd_req_cal.objects.filter(id_categ =self.request.user)

