from django.db import models
from puput.abstracts import EntryAbstract
from wagtail.admin.edit_handlers import FieldPanel


class VideoEntryAbstract(EntryAbstract):
    video_url = models.URLField(blank=True, null=True)
    content_panels = EntryAbstract.content_panels + [
        FieldPanel('video_url')
    ]

    class Meta:
        abstract = True
