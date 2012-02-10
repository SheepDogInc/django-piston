Form Validation
---------------

Django has an excellent built-in form validation facility, and Piston
can make good use of this.

You can decorate your actions with a @validate decorator, which receives
1 required argument, and one optional. The first argument is the form it
will use for validation, and the second argument is the place to look
for data. For the ``create`` action, this is ‘POST’ (default), and for
``update``, it’s ‘PUT’.

For example:

.. sourcecode:: python

    from django import forms
    from piston.utils import validate
    from mysite.myapp.models import Blogpost

    class BlogpostForm(forms.ModelForm):
        class Meta:
            model = Blogpost


    @validate(BlogpostForm)
    def create():
        pass

Or with a normal form:

.. sourcecode:: python

    from django import forms
    from piston.utils import validate

    class DataForm(forms.Form):
        data = forms.CharField(max_length=128)
        is_private = forms.BooleanField(default=True, required=False)

    @validate(DataForm, 'PUT')
    def update():
        pass

If data sent to an action that is decorated with a @validate action does
not pass the forms ``is_clean`` method, Piston will return an error to
the client, and will not execute the action. If the validation passes,
then the form object is attached to the request object. Thus you can get
to the form (and thus the cleaned\_data) via ``request.form`` as in this
example:

.. sourcecode:: python

    @validate(EchoForm, 'GET')
    def read(self, request):
        return {'msg': request.form.cleaned_data['msg']}


