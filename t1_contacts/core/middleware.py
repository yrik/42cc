from core.models import Http


class HttpMiddleware(object):
    def process_request(self, request):

        h = Http(user=request.user, path=request.path, method=request.method,
            GET=request.GET.urlencode(),
            POST=request.POST.urlencode(),
            META="; ".join(["%s:%s" % (k, v) for k, v in request.META.items()])
        )

        h.save()
        return None
