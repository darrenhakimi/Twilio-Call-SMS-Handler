# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class BrandedCallList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the BrandedCallList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.preview.trusted_comms.branded_call.BrandedCallList
        :rtype: twilio.rest.preview.trusted_comms.branded_call.BrandedCallList
        """
        super(BrandedCallList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Business/BrandedCalls'.format(**self._solution)

    def create(self, from_, to, reason):
        """
        Create a new BrandedCallInstance

        :param unicode from_: Twilio number from which to brand the call
        :param unicode to: The terminating Phone Number
        :param unicode reason: The business reason for this phone call

        :returns: Newly created BrandedCallInstance
        :rtype: twilio.rest.preview.trusted_comms.branded_call.BrandedCallInstance
        """
        data = values.of({'From': from_, 'To': to, 'Reason': reason, })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return BrandedCallInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.TrustedComms.BrandedCallList>'


class BrandedCallPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the BrandedCallPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.trusted_comms.branded_call.BrandedCallPage
        :rtype: twilio.rest.preview.trusted_comms.branded_call.BrandedCallPage
        """
        super(BrandedCallPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of BrandedCallInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.trusted_comms.branded_call.BrandedCallInstance
        :rtype: twilio.rest.preview.trusted_comms.branded_call.BrandedCallInstance
        """
        return BrandedCallInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.TrustedComms.BrandedCallPage>'


class BrandedCallInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload):
        """
        Initialize the BrandedCallInstance

        :returns: twilio.rest.preview.trusted_comms.branded_call.BrandedCallInstance
        :rtype: twilio.rest.preview.trusted_comms.branded_call.BrandedCallInstance
        """
        super(BrandedCallInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'bg_color': payload['bg_color'],
            'caller': payload['caller'],
            'created_at': deserialize.iso8601_datetime(payload['created_at']),
            'font_color': payload['font_color'],
            'from_': payload['from'],
            'logo': payload['logo'],
            'reason': payload['reason'],
            'status': payload['status'],
            'to': payload['to'],
            'url': payload['url'],
            'use_case': payload['use_case'],
        }

        # Context
        self._context = None
        self._solution = {}

    @property
    def account_sid(self):
        """
        :returns: Account Sid.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def bg_color(self):
        """
        :returns: Background color of the current phone call
        :rtype: unicode
        """
        return self._properties['bg_color']

    @property
    def caller(self):
        """
        :returns: Caller name of the current phone call
        :rtype: unicode
        """
        return self._properties['caller']

    @property
    def created_at(self):
        """
        :returns: The date this current phone call was created
        :rtype: datetime
        """
        return self._properties['created_at']

    @property
    def font_color(self):
        """
        :returns: Font color of the current phone call
        :rtype: unicode
        """
        return self._properties['font_color']

    @property
    def from_(self):
        """
        :returns: The originating phone number
        :rtype: unicode
        """
        return self._properties['from_']

    @property
    def logo(self):
        """
        :returns: Logo URL of the caller
        :rtype: unicode
        """
        return self._properties['logo']

    @property
    def reason(self):
        """
        :returns: The business reason for this current phone call
        :rtype: unicode
        """
        return self._properties['reason']

    @property
    def status(self):
        """
        :returns: The status of the current phone call
        :rtype: unicode
        """
        return self._properties['status']

    @property
    def to(self):
        """
        :returns: The terminating phone number
        :rtype: unicode
        """
        return self._properties['to']

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def use_case(self):
        """
        :returns: The use case for the current phone call
        :rtype: unicode
        """
        return self._properties['use_case']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.TrustedComms.BrandedCallInstance>'
