from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from eds.models import Selection
from eds.permissions import IsSelectionOwner
from eds.serializers import SelectionS, SelectionLS, SelectionDetailS, SelectionCreateS


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.all()
    default_serializer = SelectionS

    serializer_classes = {
        "list": SelectionLS,
        "retrieve": SelectionDetailS,
        "create": SelectionCreateS
    }

    default_permission = [AllowAny()]
    permissions = {
        "create": [IsAuthenticated()],
        "retrieve": [IsAuthenticated()],
        "partial_update": [IsAuthenticated(), IsSelectionOwner()],
        "update": [IsAuthenticated(), IsSelectionOwner()],
        "delete": [IsAuthenticated(), IsSelectionOwner()]

    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)
