from plone.theme.interfaces import IDefaultPloneLayer
from zope.interface import Interface
from zope import schema

from iservices.rssdocument import RSSDocumentMessageFactory as _


class IRSSDocumentLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 Layer for this product
    """

class IRSSDocument(Interface):
    """
    A Plone document that embedds a RSS feed with JQuery
    """
    title = schema.TextLine(title=_(u'RSS Feed Name'),
                            description=_(u'A descriptive name for the RSS Feed such as "My brand new Blog"'),
                            required=True)
    rsslink = schema.TextLine(title=_(u'RSS URL'),
                            description=_(u'The URL of the RSS Feed'),
                            required=True)
    max_entries = schema.Int(title=_(u'Max Entries'),
                            description=_(u'Maximum Number of entries to show'),
                            required=True)
    