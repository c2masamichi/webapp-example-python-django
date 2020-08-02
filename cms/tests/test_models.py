from django.core.exceptions import ValidationError
import pytest

from blog.models import Entry


@pytest.mark.django_db
def test_get():
    r = Entry.objects.all()
    print('-----')
    print(r)
    print('-----')


@pytest.mark.django_db
@pytest.mark.parametrize(
    ('title', 'body'),
    (
        ('a' * 101, 'created on test'),
        ('created on test', 'a' * 10001),
    ),
)
def test_create_validate(title, body):
    with pytest.raises(ValidationError):
        entry = Entry(title=title, body=body)
        entry.full_clean()


@pytest.mark.django_db
@pytest.mark.parametrize(
    ('title', 'body'),
    (
        ('a' * 101, 'created on test'),
        ('created on test', 'a' * 10001),
    ),
)
def test_update_validate(title, body):
    entry_id = 1
    entry = Entry.objects.get(pk=entry_id)
    with pytest.raises(ValidationError):
        entry.title = title
        entry.body = body
        entry.full_clean()
