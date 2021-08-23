from rest_framework import mixins, viewsets


class OnlyGETGroup(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    pass
