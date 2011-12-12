from Products.Five import zcml
from Products.Five import fiveconfigure

from Testing import ZopeTestCase as ztc

from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

@onsetup
def setup_product():
    """Set up the package and its dependencies.
    
    The @onsetup decorator causes the execution of this body to be deferred
    until the setup of the Plone site testing layer. We could have created our
    own layer, but this is the easiest way for Plone integration tests.
    """
    
    fiveconfigure.debug_mode = True
    import iservices.rssdocument
    zcml.load_config('configure.zcml', iservices.rssdocument)
    fiveconfigure.debug_mode = False
    
    ztc.installPackage('iservices.rssdocument')

setup_product()
ptc.setupPloneSite(products=['iservices.rssdocument'])

class RSSDocumentTestCase(ptc.PloneTestCase):
    """We use this base class for all the tests in this package. If necessary,
    we can put common utility or setup code in here. This applies to unit 
    test cases.
    """

class RSSDocumentFunctionalTestCase(ptc.FunctionalTestCase):
    """We use this class for functional integration tests that use doctest
    syntax. Again, we can put basic common utility or setup code in here.
    """


