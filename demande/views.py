from django.shortcuts import render

from django.shortcuts import render
from django.shortcuts import render, redirect
from demande.forms import DemandeForm
from demande.models import Demande
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.core import serializers


@api_view(["POST"])
def dem(request):
    serializer = DemandeForm(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"dema": serializer.data})

    return Response(serializer.errors, status=status.HTTP_200_OK)


@api_view(["GET"])
def print(request):
    demandes = Demande.objects.all()
    demande_list = []

    for demande in demandes:
        demande_list.append(
            {
                "id": demande.id,
                "prenom": demande.prenom,
                "nom": demande.nom,
                "date_Aller": demande.date_aller,
                "date_retour": demande.date_retour,
                "sujet": demande.sujet_mission,
                "plan": demande.plan,
                "accompagnant": demande.accompagnant,
                "reponse_admin": demande.reponse_admin,
                "id_user": demande.id_user,
                "date_submit": demande.date_submit
                # Add more fields as needed
            }
        )

    return JsonResponse({"demandes": demande_list})


@api_view(["GET"])
def show(request, id):
    demandes = Demande.objects.filter(id_user=id)
    demande_list = []

    for demande in demandes:
        demande_list.append(
            {
                "id": demande.id,
                "prenom": demande.prenom,
                "nom": demande.nom,
                "date_Aller": demande.date_aller,
                "date_retour": demande.date_retour,
                "sujet": demande.sujet_mission,
                "plan": demande.plan,
                "accompagnant": demande.accompagnant,
                "reponse_admin": demande.reponse_admin,
                "id_user": demande.id_user,
                "date_submit": demande.date_submit
                # Add more fields as needed
            }
        )

    return JsonResponse({"demandes": demande_list})


@api_view(["GET"])
def edit(request, id):
    try:
        demande = Demande.objects.get(id=id)
        # You can serialize the demande object to JSON if needed
        data = {
            "id": demande.id,
            "prenom": demande.prenom,
            "nom": demande.nom,
            "date_Aller": demande.date_aller,
            "date_retour": demande.date_retour,
            "sujet": demande.sujet_mission,
            "plan": demande.plan,
            "accompagnant": demande.accompagnant,
        }
        return JsonResponse(data)
    except Demande.DoesNotExist:
        return JsonResponse({"error": "Demande not found"}, status=404)


@api_view(["PUT"])
def update(request, id):
    # Assuming you have a unique identifier, such as 'id' to identify the instance to update
    try:
        instance = Demande.objects.get(id=id)
    except Demande.DoesNotExist:
        return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = DemandeForm(instance=instance, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"dema": serializer.data})

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def accept_demand(request, id):
    try:
        demand = Demande.objects.get(id=id)
        demand.reponse_admin = "true"
        demand.save()
        return Response({"message": "Demand accepted successfully."})
    except Exception as e:
        return Response({"error": str(e)}, status=400)


@api_view(["POST"])
def refuse_demand(request, id):
    try:
        demand = Demande.objects.get(id=id)
        demand.reponse_admin = "false"
        demand.save()
        return Response({"message": "Demand refused."})
    except Exception as e:
        return Response({"error": str(e)}, status=400)


@api_view(["DELETE"])
def destroy(request, id):
    try:
        demande = Demande.objects.get(id=id)
        demande.delete()
        return Response({"message": "Demande deleted successfully"})
    except Demande.DoesNotExist:
        return Response(
            {"detail": "Demande not found"}, status=status.HTTP_404_NOT_FOUND
        )
