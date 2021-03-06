# -*- coding: utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions
from profiles.models import Profile


class ProfileTranslationOptions(TranslationOptions):
    fields = ('description', )
    
translator.register(Profile, ProfileTranslationOptions)