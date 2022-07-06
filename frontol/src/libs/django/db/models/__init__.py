import uuid

from django.utils.translation import gettext_lazy as _
from django.db.models import Model, UUIDField


class UUIDedModel(Model):
    class Meta:
        abstract = True

    uuid = UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True,
        editable=True,
        verbose_name=_('uuid'),
    )
