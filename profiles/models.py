from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProfileBase(models.Model):
    user = models.OneToOneField(User)

    class Meta:
        abstract = True


class Profile(ProfileBase):
    company = models.CharField(max_length=50, blank=True, null=True, verbose_name=_('company'))
    description = models.TextField(blank=True, null=True, verbose_name=_('description'))
    status = models.CharField(max_length=150, blank=True, null=True, verbose_name=_('status'))
    update_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        fullname = self.user.get_full_name()
        if len(fullname) > 2:
            return self.user.get_full_name()
        else:
            return self.user.username