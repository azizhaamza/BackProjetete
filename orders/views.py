from django.shortcuts import render, redirect
from orders.forms import OrderForm
from orders.models import Order
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.core import serializers


@api_view(["POST"])
def ord(request):
    serializer = OrderForm(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"dema": serializer.data})

    return Response(serializer.errors, status=status.HTTP_200_OK)


@api_view(["GET"])
def show(request):
    orders = Order.objects.all()
    orders_list = []

    for order in orders:
        orders_list.append(
            {
                "id": order.id,
                "prenom": order.prenom,
                "nom": order.nom,
                "date_Aller": order.date_aller,
                "date_retour": order.date_retour,
                "sujet": order.sujet_mission,
                "plan": order.plan,
                "accompagnant": order.accompagnant,
                # Add more fields as needed
            }
        )

    return JsonResponse({"orders": orders_list})


@api_view(["GET"])
def edit(request, id):
    try:
        order = Order.objects.get(id=id)
        # You can serialize the demande object to JSON if needed
        data = {
            "id": order.id,
            "prenom": order.prenom,
            "nom": order.nom,
            "date_Aller": order.date_aller,
            "date_retour": order.date_retour,
            "sujet": order.sujet_mission,
            "plan": order.plan,
            "accompagnant": order.accompagnant,
            # Add more fields as needed
        }
        return JsonResponse(data)
    except Order.DoesNotExist:
        return JsonResponse({"error": "Order not found"}, status=404)


@api_view(["PUT"])
def update(request, id):
    # Assuming you have a unique identifier, such as 'id' to identify the instance to update
    try:
        instance = Order.objects.get(id=id)
    except Order.DoesNotExist:
        return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = OrderForm(instance=instance, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"order": serializer.data})

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def destroy(request, id):
    try:
        order = Order.objects.get(id=id)
        order.delete()
        return Response({"message": "Order deleted successfully"})
    except Order.DoesNotExist:
        return Response({"detail": "order not found"}, status=status.HTTP_404_NOT_FOUND)
