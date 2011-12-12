from base import RSSDocumentTestCase
from iservices.rssdocument.interfaces import IRSSDocument

class TestProductInstall(RSSDocumentTestCase):

    def afterSetUp(self):
        self.types = ('RSSDocument',)

    def testTypesInstalled(self):
        for t in self.types:
            self.failUnless(t in self.portal.portal_types.objectIds(),
                            '%s content type not installed' % t)

    def testPortalFactoryEnabled(self):
        for t in self.types:
            self.failUnless(t in self.portal.portal_factory.getFactoryTypes().keys(),
                            '%s content type not installed' % t)

class TestInstantiation(RSSDocumentTestCase):

    def afterSetUp(self):
        # Adding an InstantMessage anywhere - can only be done by a Manager or Portal Owner
        self.setRoles(['Manager'])
        self.portal.invokeFactory('RSSDocument', 'rssdoc1')

    def testCreateRSSDocument(self):
        self.failUnless('rssdoc1' in self.portal.objectIds())

    def testRSSDocumentInterface(self):
        rssdoc = self.portal.rssdoc1
        self.failUnless(IRSSDocument.providedBy(rssdoc))

    def testRSSDocumentAccessorMutator(self):
        obj = self.portal.rssdoc1

        url = 'http://www.example.org/'
        obj.setRSSLink(url)
        self.failUnlessEqual(obj.getRSSLink(), url)

        url = 'false:url'
        obj.setRSSLink(url)
        self.failUnlessEqual(obj.getRSSLink(), url)
        
def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestProductInstall))
    suite.addTest(makeSuite(TestInstantiation))
    return suite
