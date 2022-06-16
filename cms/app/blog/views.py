from django.core.paginator import Paginator

from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Entry


def index(request):
    limit = 5
    page_number = request.GET.get('page')

    entries = Entry.objects.order_by('created').reverse()
    paginator = Paginator(entries, limit)

    entries_showed = paginator.get_page(page_number)
    context = {
        'entries': entries_showed,
        'page_numbers': range(1, entries_showed.paginator.num_pages + 1)
    }
    return render(request, 'blog/index.html', context)


def detail(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'blog/detail.html', {'entry': entry})