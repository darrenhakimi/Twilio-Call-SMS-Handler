# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class InviteList(ListResource):
    """  """

    def __init__(self, version, service_sid, channel_sid):
        """
        Initialize the InviteList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service that the resource is associated with
        :param channel_sid: The SID of the Channel the new resource belongs to

        :returns: twilio.rest.chat.v2.service.channel.invite.InviteList
        :rtype: twilio.rest.chat.v2.service.channel.invite.InviteList
        """
        super(InviteList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'channel_sid': channel_sid, }
        self._uri = '/Services/{service_sid}/Channels/{channel_sid}/Invites'.format(**self._solution)

    def create(self, identity, role_sid=values.unset):
        """
        Create a new InviteInstance

        :param unicode identity: The `identity` value that identifies the new resource's User
        :param unicode role_sid: The Role assigned to the new member

        :returns: Newly created InviteInstance
        :rtype: twilio.rest.chat.v2.service.channel.invite.InviteInstance
        """
        data = values.of({'Identity': identity, 'RoleSid': role_sid, })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return InviteInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
        )

    def stream(self, identity=values.unset, limit=None, page_size=None):
        """
        Streams InviteInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode identity: The `identity` value of the resources to read
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v2.service.channel.invite.InviteInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(identity=identity, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, identity=values.unset, limit=None, page_size=None):
        """
        Lists InviteInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode identity: The `identity` value of the resources to read
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v2.service.channel.invite.InviteInstance]
        """
        return list(self.stream(identity=identity, limit=limit, page_size=page_size, ))

    def page(self, identity=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of InviteInstance records from the API.
        Request is executed immediately

        :param unicode identity: The `identity` value of the resources to read
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InviteInstance
        :rtype: twilio.rest.chat.v2.service.channel.invite.InvitePage
        """
        params = values.of({
            'Identity': serialize.map(identity, lambda e: e),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return InvitePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of InviteInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of InviteInstance
        :rtype: twilio.rest.chat.v2.service.channel.invite.InvitePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return InvitePage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a InviteContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.chat.v2.service.channel.invite.InviteContext
        :rtype: twilio.rest.chat.v2.service.channel.invite.InviteContext
        """
        return InviteContext(
            self._version,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a InviteContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.chat.v2.service.channel.invite.InviteContext
        :rtype: twilio.rest.chat.v2.service.channel.invite.InviteContext
        """
        return InviteContext(
            self._version,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Chat.V2.InviteList>'


class InvitePage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the InvitePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The SID of the Service that the resource is associated with
        :param channel_sid: The SID of the Channel the new resource belongs to

        :returns: twilio.rest.chat.v2.service.channel.invite.InvitePage
        :rtype: twilio.rest.chat.v2.service.channel.invite.InvitePage
        """
        super(InvitePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of InviteInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.chat.v2.service.channel.invite.InviteInstance
        :rtype: twilio.rest.chat.v2.service.channel.invite.InviteInstance
        """
        return InviteInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Chat.V2.InvitePage>'


class InviteContext(InstanceContext):
    """  """

    def __init__(self, version, service_sid, channel_sid, sid):
        """
        Initialize the InviteContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the resource from
        :param channel_sid: The SID of the Channel the resource to fetch belongs to
        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.chat.v2.service.channel.invite.InviteContext
        :rtype: twilio.rest.chat.v2.service.channel.invite.InviteContext
        """
        super(InviteContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'channel_sid': channel_sid, 'sid': sid, }
        self._uri = '/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a InviteInstance

        :returns: Fetched InviteInstance
        :rtype: twilio.rest.chat.v2.service.channel.invite.InviteInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return InviteInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the InviteInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Chat.V2.InviteContext {}>'.format(context)


class InviteInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, service_sid, channel_sid, sid=None):
        """
        Initialize the InviteInstance

        :returns: twilio.rest.chat.v2.service.channel.invite.InviteInstance
        :rtype: twilio.rest.chat.v2.service.channel.invite.InviteInstance
        """
        super(InviteInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'channel_sid': payload['channel_sid'],
            'service_sid': payload['service_sid'],
            'identity': payload['identity'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'role_sid': payload['role_sid'],
            'created_by': payload['created_by'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'channel_sid': channel_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: InviteContext for this InviteInstance
        :rtype: twilio.rest.chat.v2.service.channel.invite.InviteContext
        """
        if self._context is None:
            self._context = InviteContext(
                self._version,
                service_sid=self._solution['service_sid'],
                channel_sid=self._solution['channel_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def channel_sid(self):
        """
        :returns: The SID of the Channel the new resource belongs to
        :rtype: unicode
        """
        return self._properties['channel_sid']

    @property
    def service_sid(self):
        """
        :returns: The SID of the Service that the resource is associated with
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def identity(self):
        """
        :returns: The string that identifies the resource's User
        :rtype: unicode
        """
        return self._properties['identity']

    @property
    def date_created(self):
        """
        :returns: The RFC 2822 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The RFC 2822 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def role_sid(self):
        """
        :returns: The SID of the Role assigned to the member
        :rtype: unicode
        """
        return self._properties['role_sid']

    @property
    def created_by(self):
        """
        :returns: The identity of the User that created the invite
        :rtype: unicode
        """
        return self._properties['created_by']

    @property
    def url(self):
        """
        :returns: The absolute URL of the Invite resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a InviteInstance

        :returns: Fetched InviteInstance
        :rtype: twilio.rest.chat.v2.service.channel.invite.InviteInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the InviteInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Chat.V2.InviteInstance {}>'.format(context)
