from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # The tutorial uses the default `commit=True`.
            # But why save the user to the database
            # before the password is hashed?
            user = user_form.save(commit=False)
            # Hash the password according to
            # `PASSWORD_HASHERS` in `settings.py`.
            user.set_password(user.password)
            user.save()

            # Use `commit=False` because otherwise we may
            # get collisions due to the `user` member variable
            # of `UserProfileInfo`, which is a `OneToOneField(User)`.
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else: # One or both forms were invalid.
            print(user_form.errors, profile_form.errors)
    else: # Not a POST request.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'basic_app/registration.html',
                  {'registered': registered, 'user_form': user_form,
                   'profile_form': profile_form})
