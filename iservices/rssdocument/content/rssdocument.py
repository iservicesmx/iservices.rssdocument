import urlparse
from urllib import quote

from zope.interface import implements
from Products.Archetypes import atapi

from Products.ATContentTypes.content import base
from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from Products.CMFCore.permissions import View
from Products.CMFCore.permissions import ModifyPortalContent
from AccessControl import ClassSecurityInfo

from iservices.rssdocument import RSSDocumentMessageFactory as _
from iservices.rssdocument.interfaces import IRSSDocument
from iservices.rssdocument import config

RSSDocumentSchema = ATContentTypeSchema.copy() + atapi.Schema((

  atapi.StringField('RSSLink',
              required=True,
              widget = atapi.StringWidget(label = _(u'RSS URL'),
                                          description=_(u'The URL of the RSS Feed')),
             ),
  atapi.IntegerField('max_entries',
              required=True,
              widget = atapi.IntegerWidget(label = _(u'Max Entries'),
                                           description=_(u'Maximum Number of entries to show')),
             ),

))
finalizeATCTSchema(RSSDocumentSchema)


class RSSDocument(base.ATCTContent):
    """A Plone document that embedds a RSS feed with JQuery"""

    implements(IRSSDocument)
    schema = RSSDocumentSchema
    security       = ClassSecurityInfo()

    security.declareProtected(ModifyPortalContent, 'setRSSLink')
    def setRSSLink(self, value, **kwargs):
        """RSS Link mutator - taken from ATLink

        Use urlparse to sanify the url
        Also see http://dev.plone.org/plone/ticket/3296
        """
        if value:
            value = urlparse.urlunparse(urlparse.urlparse(value))
        self.getField('RSSLink').set(self, value, **kwargs)

    security.declareProtected(View, 'getRSSLink')
    def getRSSLink(self):
        """Sanitize output - taken from ATLink
        """
        value = self.Schema()['RSSLink'].get(self)
        if not value: value = '' # ensure we have a string
        return quote(value, safe='?$#@/:=+;$,&%')

atapi.registerType(RSSDocument, config.PROJECTNAME)
