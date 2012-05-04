from Acquisition import aq_inner
from Products.Five.browser import BrowserView

class rsscodeView(BrowserView):
    js_code = "$(document).ready(function () {$('#rsscontainer-%s').rssfeed('%s', {limit: %s});});"
    def __call__(self,REQUEST,RESPONSE):
        context = aq_inner(self.context)
        RESPONSE.setHeader('Content-Type', 'application/javascript')
        return self.js_code % (context.UID(), context.getRSSLink(), context.getMax_entries())

