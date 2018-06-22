from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.views.generic.edit import ModelFormMixin
from django.contrib import messages
from .forms import FormCoor, FormMedicion
from .models import Medicion, Coordenadas
# Create your views here.


def index(request):
    return HttpResponse("Hola index.")


class RegCoor(CreateView):
    template_name = 'formcoor.html'
    form_class = FormCoor
    model = Coordenadas
    def get_form_kwargs(self):
        kwargs = super(ModelFormMixin, self).get_form_kwargs()
        kwargs.update({'instance': self.object})
        kwargs.update({'request': self.request})
        return kwargs
    def get_success_url(self):
        messages.success(self.request, "Registrado exitosamente", extra_tags="sticky")
        return reverse_lazy('clim:lis_coor')
    def get_context_data(self, **kwargs):
        if not self.request.user.is_staff and not self.request.user.is_admin:
            raise Http404
        context = super(RegCoor, self).get_context_data(**kwargs)
        context['tit_cont'] = 'Registrar'
        context['sub_tit_cont'] = ' Coordenadas'
        return context
    def form_valid(self, form):
        if not self.request.user.is_staff and not self.request.user.is_admin:
            raise Http404
        if form.has_changed:
            print("cambio")
        return super(RegCoor, self).form_valid(form)


class LiCoor(ListView):
    template_name = 'clim/li_coor.html'
    model = Coordenadas
    paginate_by = 30
    def get_queryset(self):
        if not self.request.user.is_staff and not self.request.user.is_admin:
            raise Http404
        qs = Coordenadas.objects.filter().order_by('-fcs')
        lat = self.request.GET.get('lat', None)
        lon = self.request.GET.get('lon', None)
        fec_ini = self.request.GET.get('fec_ini', None)
        fec_fin = self.request.GET.get('fec_fin', None)
        # Sample.objects.filter(date__range=["2011-01-01", "2011-01-31"])
        if fec_ini and fec_fin:
            if fec_ini <= fec_fin:
                qs = qs.filter(fcs__range=['{} 00:00:01'.format(fec_ini), '{} 23:59:59'.format(fec_fin)])
        if fec_ini and fec_fin == "":
            qs = qs.filter(fcs__range=['{} 00:00:01'.format(fec_ini), '{} 23:59:59'.format(fec_ini)])
        if fec_fin and fec_ini == "":
            qs = qs.filter(fcs__range=['{} 00:00:01'.format(fec_fin), '{} 23:59:59'.format(fec_fin)])
        if lat:
            qs = qs.filter(lat=lat)
        if lon:
            qs = qs.filter(lon=lon)
        return qs
    def get_context_data(self, **kwargs):
        context = super(LiCoor, self).get_context_data(**kwargs)
        fec_ini = self.request.GET.get('fec_ini', None)
        fec_fin = self.request.GET.get('fec_fin', None)
        lat = self.request.GET.get('lat', None)
        lon = self.request.GET.get('lon', None)
        context["tot"] = len(self.get_queryset())
        context["tit_cont"] = 'Coordenadas'
        context["sub_tit_cont"] = ' Lista'
        if lat:
            context["lat"] = lat
        if fec_ini:
            context["fec_ini"] = fec_ini
        if fec_fin:
            context["fec_fin"] = fec_fin
        if lon:
            context["lon"] = lon
        return context

class RegMedi(CreateView):
    template_name = 'formmedi.html'
    form_class = FormMedicion
    model = Medicion
    def get_form_kwargs(self):
        kwargs = super(ModelFormMixin, self).get_form_kwargs()
        kwargs.update({'instance': self.object})
        kwargs.update({'request': self.request})
        return kwargs
    def get_success_url(self):
        messages.success(self.request, "Registrado exitosamente", extra_tags="sticky")
        return reverse_lazy('clim:lis_medi')
    def get_context_data(self, **kwargs):
        if not self.request.user.is_staff and not self.request.user.is_admin:
            raise Http404
        context = super(RegMedi, self).get_context_data(**kwargs)
        context['tit_cont'] = 'Registrar'
        context['sub_tit_cont'] = ' Medicion'
        return context
    def form_valid(self, form):
        if not self.request.user.is_staff and not self.request.user.is_admin:
            raise Http404
        if form.has_changed:
            print("cambio")
        return super(RegMedi, self).form_valid(form)


class LiMedi(ListView):
    template_name = 'clim/li_medi.html'
    model = Medicion
    paginate_by = 30
    def get_queryset(self):
        if not self.request.user.is_staff and not self.request.user.is_admin:
            raise Http404
        qs = Medicion.objects.filter().order_by('-fcs')
        temp = self.request.GET.get('temp', None)
        humedad = self.request.GET.get('humedad', None)
        viento = self.request.GET.get('viento', None)
        desc = self.request.GET.get('desc', None)
        fec_ini = self.request.GET.get('fec_ini', None)
        fec_fin = self.request.GET.get('fec_fin', None)
        # Sample.objects.filter(date__range=["2011-01-01", "2011-01-31"])
        if fec_ini and fec_fin:
            if fec_ini <= fec_fin:
                qs = qs.filter(fcs__range=['{} 00:00:01'.format(fec_ini), '{} 23:59:59'.format(fec_fin)])
        if fec_ini and fec_fin == "":
            qs = qs.filter(fcs__range=['{} 00:00:01'.format(fec_ini), '{} 23:59:59'.format(fec_ini)])
        if fec_fin and fec_ini == "":
            qs = qs.filter(fcs__range=['{} 00:00:01'.format(fec_fin), '{} 23:59:59'.format(fec_fin)])
        if temp:
            qs = qs.filter(temp=temp)
        if humedad:
            qs = qs.filter(humedad=humedad)
        if viento:
            qs = qs.filter(viento=viento)
        if desc:
            qs = qs.filter(desc=desc)
        return qs
    def get_context_data(self, **kwargs):
        context = super(LiMedi, self).get_context_data(**kwargs)
        fec_ini = self.request.GET.get('fec_ini', None)
        fec_fin = self.request.GET.get('fec_fin', None)
        temp = self.request.GET.get('temp', None)
        humedad = self.request.GET.get('humedad', None)
        viento = self.request.GET.get('viento', None)
        desc = self.request.GET.get('desc', None)
        context["tot"] = len(self.get_queryset())
        context["tit_cont"] = 'Medicion'
        context["sub_tit_cont"] = ' Lista'
        if temp:
            context["temp"] = temp
        if fec_ini:
            context["fec_ini"] = fec_ini
        if fec_fin:
            context["fec_fin"] = fec_fin
        if humedad:
            context["humedad"] = humedad
        if viento:
            context["viento"] = viento
        if desc:
            context["desc"] = desc
        return context
