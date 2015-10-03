from django.conf.urls import url
from django.http import HttpRequest
from django.views.generic import View
from yunity.utils.api import ApiBase


class Opportunities(ApiBase, View):
    def get(self, request):
        """list all opportunities

        @type request: HttpRequest
        """
        raise NotImplementedError

    def post(self, request):
        """create a new opportunity

        @type request: HttpRequest
        """
        raise NotImplementedError


class Opportunity(ApiBase, View):
    def get(self, request, opportunityid):
        """return details about opportunity, including participants

        @type request: HttpRequest
        @type opportunityid: int
        """
        raise NotImplementedError

    def put(self, request, opportunityid):
        """modify the opportunity

        @type request: HttpRequest
        @type opportunityid: int
        """
        raise NotImplementedError


class OpportunityWallposts(ApiBase, View):
    def get(self, request, opportunityid):
        """list all messages on the wall

        @type request: HttpRequest
        @type opportunityid: int
        """
        raise NotImplementedError

    def post(self, request, opportunityid):
        """adds a message to the wall

        @type request: HttpRequest
        @type opportunityid: int
        """
        raise NotImplementedError


class OpportunityWallpost(ApiBase, View):
    def put(self, request, opportunityid, wallpostid):
        """edit the message

        @type request: HttpRequest
        @type opportunityid: int
        @type wallpostid: int
        """
        raise NotImplementedError

    def delete(self, request, opportunityid, wallpostid):
        """delete the message

        @type request: HttpRequest
        @type opportunityid: int
        @type wallpostid: int
        """
        raise NotImplementedError


urlpatterns = [
    url(r'/?^$', Opportunities.as_view()),
    url(r'^(?P<opportunityid>[0-9]+)/?$', Opportunity.as_view()),
    url(r'^(?P<opportunityid>[0-9]+)/wallposts/?$', OpportunityWallposts.as_view()),
    url(r'^(?P<opportunityid>[0-9]+)/wallposts/(?P<wallpostid>[0-9]+)/?$', OpportunityWallpost.as_view()),
]
