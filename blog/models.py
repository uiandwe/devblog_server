from django.conf import settings
from django.db import models


class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

from django.conf import settings
from django.db import models
from django.utils.timezone import now as datetime_now
from django.utils.translation import ugettext_lazy as _
import datetime

class RegistrationProfile(models.Model):
    """
    A simple profile which stores an activation key for use during
    user account registration.
    """
    ACTIVATED = u"ALREADY_ACTIVATED"

    user = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, verbose_name=_('user'), related_name='api_registration_profile')
    activation_key = models.CharField(_('activation key'), max_length=40)

    def activation_key_expired(self):

        # utils imported here to avoid circular import
        import blog.api.utils as utils

        expiration_date = datetime.timedelta(
            days=utils.get_settings('REGISTRATION_API_ACCOUNT_ACTIVATION_DAYS'))
        return self.activation_key == self.ACTIVATED or \
            (self.user.date_joined + expiration_date <= datetime_now())