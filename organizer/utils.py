from django.shortcuts import render, redirect

class ObjectCreateMixin:
    form_class = None
    template_name = ''

    def get (self, request):
        return render(request, self.template_name, {'from':self.form_class()})

    def post (self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return render(new_object)
        else:
            return render(request, self.template_name, {'form':bound_form})