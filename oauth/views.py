from django.shortcuts import render

# Create your views here.
from urllib.parse import urlparse
import datetime
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model
from .models import OAuthUser
from django.contrib.auth import login
from django.shortcuts import get_object_or_404
from django.views.generic import FormView, RedirectView
from oauth.forms import RequireEmailForm
from django.urls import reverse
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseForbidden
from .oauthmanager import get_manager_by_type, OAuthAccessTokenException

import logging

logger = logging.getLogger(__name__)


def get_redirecturl(request):
    nexturl = request.GET.get('next_url', None)
    if not nexturl or nexturl == '/login/' or nexturl == '/login':
        nexturl = '/'
        return nexturl
    p = urlparse(nexturl)
    if p.netloc:
        site = get_current_site().domain
        if not p.netloc.replace('www.', '') == site.replace('www.', ''):
            logger.info('非法url:' + nexturl)
            return "/"
    return nexturl


def oauthlogin(request):
    type = request.GET.get('type', None)
    if not type:
        return HttpResponseRedirect('/')
    manager = get_manager_by_type(type)
    if not manager:
        return HttpResponseRedirect('/')
    nexturl = get_redirecturl(request)
    authorizeurl = manager.get_authorization_url(nexturl)
    return HttpResponseRedirect(authorizeurl)


def authorize(request):
    type = request.GET.get('type', None)
    if not type:
        return HttpResponseRedirect('/')
    manager = get_manager_by_type(type)
    if not manager:
        return HttpResponseRedirect('/')
    code = request.GET.get('code', None)
    try:
        rsp = manager.get_access_token_by_code(code)
    except OAuthAccessTokenException as e:
        logger.warning("OAuthAccessTokenException:" + str(e))
        return HttpResponseRedirect('/')
    except Exception as e:
        logger.error(e)
        rsp = None
    nexturl = get_redirecturl(request)
    if not rsp:
        return HttpResponseRedirect(manager.get_authorization_url(nexturl))
    user = manager.get_oauth_userinfo()
    if user:
        if not user.nikename or not user.nikename.strip():
            import datetime
            user.nikename = "djangoblog" + datetime.datetime.now().strftime('%y%m%d%I%M%S')
        try:
            temp = OAuthUser.objects.get(type=type, openid=user.openid)
            temp.picture = user.picture
            temp.matedata = user.matedata
            temp.nikename = user.nikename
            user = temp
        except ObjectDoesNotExist:
            pass
        # facebook的token过长
        if type == 'facebook':
            user.token = ''
        if user.email:
            with transaction.atomic():
                author = None
                try:
                    author = get_user_model().objects.get(id=user.author_id)
                except ObjectDoesNotExist:
                    pass
                if not author:
                    result = get_user_model().objects.get_or_create(email=user.email)
                    author = result[0]
                    if result[1]:
                        author.username = user.nikename
                        author.source = 'authorize'
                        author.save()

                user.author = author
                user.save()

                oauth_user_login_signal.send(sender=authorize.__class__, id=user.id)
                login(request, author)
                return HttpResponseRedirect(nexturl)
        else:
            user.save()
            url = reverse('oauth:require_email', kwargs={
                'oauthid': user.id
            })

            return HttpResponseRedirect(url)
    else:
        return HttpResponseRedirect(nexturl)
