from django.http import HttpResponse, JsonResponse
from .models import Product, Promotion
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

# Create your views here.

@permission_classes([IsAuthenticated])
@api_view(["GET"])
def get_all_products(request):
    data = Product.objects.all()
    serializer = ProductSerializerGET(data, many=True)
    return JsonResponse(serializer.data, safe=False)

@permission_classes([IsAuthenticated])
@csrf_exempt
@api_view(["POST"])
def post_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(data=serializer.data, status=201)
    return JsonResponse(data=serializer.errors, status=400)

@permission_classes([IsAuthenticated])
@api_view(["GET"])
def get_all_promotion(request):
    data = Promotion.objects.all()
    serializer = PromotionSerializerGET(data, many=True)
    return JsonResponse(serializer.data, safe=False)

@permission_classes([IsAuthenticated])
@csrf_exempt
@api_view(["POST"])
def post_promotion(request):
    serializer = PromotionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(data=serializer.data, status=201)
    return JsonResponse(data=serializer.errors, status=400)

@permission_classes([IsAuthenticated])
@api_view(["GET"])
def get_product_by_id(request, id):
    data = get_object_or_404(Product, pk=id)
    serializer = ProductSerializerGET(data)
    return JsonResponse(data=serializer.data)

@permission_classes([IsAuthenticated])
@api_view(["PUT"])
def put_product_by_id(request, id):
    data = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(data, request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(data=serializer.data)
    return JsonResponse(data=serializer.errors, status=400)

@permission_classes([IsAuthenticated])
@api_view(["DELETE"])
def delete_product_by_id(request, id):
    data = get_object_or_404(Product, pk=id)
    data.delete()
    return HttpResponse(status=204)
    
@permission_classes([IsAuthenticated])
@api_view(["GET"])
def get_promotion_by_id(request, id):
    data = get_object_or_404(Promotion, pk=id)
    serializer = PromotionSerializerGET(data)
    return JsonResponse(data=serializer.data)

@permission_classes([IsAuthenticated])
@api_view(["PUT"])
def put_promotion_by_id(request, id):
    data = get_object_or_404(Promotion, pk=id)
    serializer = PromotionSerializer(data, request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(data=serializer.data)
    return JsonResponse(data=serializer.errors, status=400)

@permission_classes([IsAuthenticated])
@api_view(["DELETE"])
def delete_promotion_by_id(request, id):
    data = get_object_or_404(Promotion, pk=id)
    data.delete()
    return HttpResponse(status=204)




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = '__all__' 

class ProductSerializerGET(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = '__all__' 
        depth=1

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Promotion
        fields = '__all__' 

class PromotionSerializerGET(serializers.ModelSerializer):
    class Meta:
        model=Promotion
        fields = '__all__' 
        depth=1