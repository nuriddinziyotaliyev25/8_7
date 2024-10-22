from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.response import Response
from .models import Type, Food, Comment, User
from .serializers import TypeSerializer, FoodSerializer,\
                        CommentSerializer, RegisterSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin, \
                                RetrieveModelMixin, UpdateModelMixin, \
                                DestroyModelMixin


class TypeListGenericView(GenericAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    def get(self, request):
        types = self.get_queryset()
        types_serializer = self.get_serializer(types, many=True)
        return Response(types_serializer.data, status=200)

    def post(self, request):
        type_serializer: TypeSerializer = self.get_serializer(data=request.data)
        if type_serializer.is_valid():
            type_serializer.save()
            context = {
                'message': "Turga ma'lumot qo'shildi",
                'type': type_serializer.data
            }
            return Response(context, status=200)
        return Response(type_serializer.errors, status=400)


class TypeDetailGenericView(GenericAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    lookup_field = 'pk'

    def get(self, request, pk):
        _type = self.get_object()
        type_serializer: TypeSerializer = self.get_serializer(_type)
        return Response(type_serializer.data, status=200)

    def put(self, request, pk):
        type_serializer: TypeSerializer = self.get_serializer(data=request.data, partial=True)
        if type_serializer.is_valid():
            _type = self.get_object()
            updated_type = type_serializer.update(instance=_type, validated_data=type_serializer.validated_data)
            context = {
                'message': "Tur ma'lumoti tahrirlandi",
                'type': self.get_serializer(updated_type).data
            }
            return Response(context, status=200)
        return Response(type_serializer.errors, status=400)

    def delete(self, request, pk):
        self.get_object().delete()
        return Response({'message': "Tur ma'lumoti o'chirildi!"}, status=200)


class FoodListGenericView(GenericAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get(self, request):
        foods = self.get_queryset()
        foods_serializer = self.get_serializer(foods, many=True)
        return Response(foods_serializer.data, status=200)

    def post(self, request):
        food_serializer: FoodSerializer = self.get_serializer(data=request.data)
        if food_serializer.is_valid():
            food_serializer.save()
            context = {
                'message': "Taom ma'lumotlari qo'shildi",
                'food': food_serializer.data
            }
            return Response(context, status=200)
        return Response(food_serializer.errors, status=400)


class FoodDetailGenericView(GenericAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    lookup_field = 'pk'

    def get(self, request, pk):
        food = self.get_object()
        food_serializer: FoodSerializer = self.get_serializer(food)
        return Response(food_serializer.data, status=200)

    def put(self, request, pk):
        food_serializer: FoodSerializer = self.get_serializer(data=request.data, partial=True)
        if food_serializer.is_valid():
            _food = self.get_object()
            updated_food = food_serializer.update(instance=_food, validated_data=food_serializer.validated_data)
            context = {
                'message': "Taom ma'lumoti tahrirlandi",
                'food': self.get_serializer(updated_food).data
            }
            return Response(context, status=200)
        return Response(food_serializer.errors, status=400)

    def delete(self, request, pk):
        self.get_object().delete()
        return Response({'message': "Taom ma'lumoti o'chirildi!"}, status=200)


class CommentListMixinView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CommentDetailMixinView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, pk, *args, **kwargs):
        return self.retrieve(request, pk, *args, **kwargs)

    def put(self, request, pk, *args, **kwargs):
        return self.update(request, pk, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        return self.destroy(request, pk, *args, **kwargs)


class RegisterView(CreateAPIView):
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

