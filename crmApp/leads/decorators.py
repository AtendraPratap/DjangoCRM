from functools import wraps
from django.shortcuts import redirect


def OrganizerAndLoginRequiredDecorator(func):

    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organizer:
            return redirect("leads:lead-list")
        return func(request, *args, **kwargs)
    return wrapper