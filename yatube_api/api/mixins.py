from rest_framework import mixins, viewsets


class CreateRetrieveViewSet(mixins.RetrieveModelMixin,
                            mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    pass
