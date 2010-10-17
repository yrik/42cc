from core.models import Http


class HttpMiddleware(object):
    def process_request(self, request):
        content = ''
        for attr, value in request.__dict__.iteritems():
            content += attr + ': + value +;'
        h = Http(content=content)
        h.save()
        return None
