from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Entry


def index(request):
    entries = Entry.objects.order_by('created').reverse()
    context = {'entries': entries}
    return render(request, 'blog/index.html', context)


def detail(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'blog/detail.html', {'entry': entry})