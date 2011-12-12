from zope.i18nmessageid import MessageFactory
from iservices.rssdocument import config

from Products.Archetypes import atapi
from Products.CMFCore import utils

RSSDocumentMessageFactory = MessageFactory('iservices.rssdocument')

def initialize(context):
    """Initializer called when used as a Zope 2 product.
    """
    from content import rssdocument
    
    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(config.PROJECTNAME),
        config.PROJECTNAME)

    for atype, constructor in zip(content_types, constructors):
        utils.ContentInit("%s: %s" % (config.PROJECTNAME, atype.portal_type),
            content_types      = (atype,),
            permission         = config.ADD_CONTENT_PERMISSIONS[atype.portal_type],
            extra_constructors = (constructor,),
            ).initialize(context)
