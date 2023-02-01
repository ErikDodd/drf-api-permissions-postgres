from rest_framework import generics
from .serializers import ShoeSerializer
from .models import Shoe
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class ShoeList(generics.ListCreateAPIView):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer

class ShoeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
