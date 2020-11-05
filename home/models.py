# Home models
from puput.models import EntryPage
from django.db import models
from django.utils.translation import ugettext_lazy as _
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import PageChooserPanel

from django.utils import translation


class TranslatedField:
    def __init__(self, ru_field, en_field):
        self.en_field = en_field
        self.ru_field = ru_field

    def __get__(self, instance, owner):
        if translation.get_language() == 'ru':
            return getattr(instance, self.ru_field)
        else:
            return getattr(instance, self.en_field)


class HomePage(Page):
    body_ru = RichTextField(_('Moto'), blank=True)
    body_en = RichTextField(_('Moto'), blank=True)
    body = TranslatedField(
        'body_ru',
        'body_en',
    )
    body2_ru = RichTextField(blank=True)
    body2_en = RichTextField(blank=True)
    body2 = TranslatedField(
        'body2_ru',
        'body2_en',
    )
    teaser = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    button1 = models.ForeignKey(
         'wagtailcore.Page',
         null=True,
         blank=True,
         on_delete=models.SET_NULL,
         related_name="+"
    )
    button2 = models.ForeignKey(
         'wagtailcore.Page',
         null=True,
         blank=True,
         on_delete=models.SET_NULL,
         related_name="+"
    )
    bodyleft_ru = RichTextField(_('Left section'), blank=True)
    bodyleft_en = RichTextField(_('Left section'), blank=True)
    bodyleft = TranslatedField(
        'bodyleft_ru',
        'bodyleft_en',
    )
    bodyright_ru = RichTextField(_('Right section'), blank=True)
    bodyright_en = RichTextField(_('Right section'), blank=True)
    bodyright = TranslatedField(
        'bodyright_ru',
        'bodyright_en',
    )
    entries = EntryPage.objects.live()
    entries = entries[0:2]
    # parent_page_types = []
    subpage_types = ['puput.BlogPage', 'article.ArticlePage']

    content_panels = Page.content_panels + [
        # FieldPanel('body_en', heading='Heading', help_text='Help text', classname="full"),
        FieldPanel('body_ru',
                   heading='Heading',
                   help_text='Help text',
                   classname="full"),
        PageChooserPanel('button1'),
        FieldPanel('body2_ru',
                   classname="full"),
        ImageChooserPanel('teaser'),
        PageChooserPanel('button2'),
        FieldPanel('bodyleft_ru',
                   classname="full"),
        FieldPanel('bodyright_ru',
                   classname="full"),
    ]
