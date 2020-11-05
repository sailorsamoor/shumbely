from django.conf import settings
from django.conf.urls import include, url, re_path
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from search import views as search_views

from puput import urls as puput_urls

urlpatterns = [

    url(r'^django-admin/', admin.site.urls),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should e the last pattern in
    # the list:
    url(r'', include(puput_urls), name='index'),
    #  url(r'', include(wagtail_urls), name='index'),

    # Alternatively, if youbas want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),
]

urlpatterns += i18n_patterns(
    # These URLs will have /<language_code>/ appended to the beginning

    # re_path(r'^search/$', search_views.search, name='search'),

    re_path(r'', include(wagtail_urls), name='index'),
)
if settings.DEBUG:
    import os
    from django.conf.urls.static import static
    from django.views.generic.base import RedirectView
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL + 'images/',
                document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
    urlpatterns += static(settings.MEDIA_URL,
                document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        url(
            r'^favicon\.ico$',
            RedirectView.as_view(url=settings.STATIC_URL +
                                 'ssspuput/images/favicon.ico'),
        ),
    ]
