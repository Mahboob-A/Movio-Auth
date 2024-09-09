import json
from rest_framework.renderers import JSONRenderer


from rest_framework.renderers import JSONRenderer
import json


class UserJSONRenderer(JSONRenderer):
    """Renderer class for User Details"""

    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context is None:
            status_code = 200
        else:
            status_code = renderer_context.get("response").status_code

        # in case of DELETE request, the "data" will be None, else "data" will hold queryset or error codes
        if data is not None:
            errors = data.get("errors", None)
        else:
            errors = None

        # data has errors
        if errors is not None:
            return super(UserJSONRenderer, self).render(data)

        return json.dumps({"status_code": status_code, "user": data})


class MultiUserJSONRenderer(JSONRenderer):
    """Renderer class for Queryset of User Details"""

    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context is None:
            status_code = 200
        else:
            status_code = renderer_context.get("response").status_code

        errors = data.get("errors", None)

        # data has errors
        if errors is not None:
            return super(UserJSONRenderer, self).render(data)

        return json.dumps({"status_code": status_code, "user": data})
