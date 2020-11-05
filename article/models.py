from django.db import models
from django.utils.translation import ugettext as _
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index
from django.utils import timezone


class ArticlePage(Page):
    intro = RichTextField(_('Short intro'), blank=True)
    body = RichTextField(_('Article text'), blank=True)
    date = models.DateField(_('Article Date'), default=timezone.now())

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.FilterField('date'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full", help_text='This is article'),
        FieldPanel('date', classname="full", help_text='This is article'),
        FieldPanel('body', classname="full", help_text='This is article')
    ]
    subpage_types = ['article.ArticlePage']
