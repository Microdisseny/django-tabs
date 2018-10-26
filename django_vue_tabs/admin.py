from django import forms
from . import settings


class TabsMixin(object):
    change_form_template = 'django_vue_tabs/change_form.html'

    @property
    def media(self):
        css = {
            'all': ('django_vue_tabs/vue-tabs-component-1.1.0.css',)
        }
        js = super(TabsMixin, self).media._js
        if settings.DJANGO_VUE_TABS_USE_VUE_JS:
            js.append('django_vue_tabs/vue-2.4.2.min.js')
        js += ['django_vue_tabs/vue-tabs-component-1.1.0.js',
               'django_vue_tabs/tabs.js']
        return forms.Media(css=css, js=js)

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        if hasattr(self, 'tabs'):
            extra_context['tabs'] = self.tabs
        else:
            extra_context['tabs'] = []
        return super(TabsMixin, self).add_view(
            request, form_url=form_url,
            extra_context=extra_context)
            
    def make_tabs_includables(self):
        if hasattr(self, 'tabs_includables'):
            # TODO
            return self.tabs_includables
        
        if not hasattr(self, 'tabs'):
            return None
            
        result = []
        for name, classes in tabs:
            tab_fieldsets = []
            for fieldset in self.get_fieldsets():
                if 'classes' in fieldset and bool(set(classes) & set(fieldset['classes'])):
                    tab_fieldsets.append(fieldset)
            for fieldset in self.get_inline_formsets():
                if 'classes' in fieldset and bool(set(classes) & set(fieldset['classes'])):
                    tab_fieldsets.append(fieldset)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        if hasattr(self, 'tabs'):
            extra_context['tabs'] = self.tabs
        else:
            extra_context['tabs'] = []
        return super(TabsMixin, self).change_view(
            request, object_id=object_id, form_url=form_url,
            extra_context=extra_context)
