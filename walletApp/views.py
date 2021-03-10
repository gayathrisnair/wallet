from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import WalletSerializer      
from .models import Wallet
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
import json
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from decimal import *
from django.conf import settings
from django.db import IntegrityError


@api_view(["GET"])
def get_balance(request, phoneNumber):      
  user_wallet = Wallet.objects.filter(phoneNumber = phoneNumber).first()
  if user_wallet is not None:
    balance = user_wallet.balance
  else:
    return JsonResponse({'error': 'No wallet found for given user'}, safe=False, status=status.HTTP_400_BAD_REQUEST) 
  return JsonResponse({"balance": balance})

@api_view(["POST"])
def add_wallet(request):
  payload = json.loads(request.body)
  try:
    wallet = Wallet.objects.create(
      phoneNumber=payload["phoneNumber"],
      balance=payload["amount"])
    serializer = WalletSerializer(wallet)
    return JsonResponse({'wallet': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
  except IntegrityError as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND) 

@api_view(["POST"])
def add_credit(request, phoneNumber):       
  credit_amount = request.GET.get('amount')
  try:
    wallet = Wallet.objects.filter(phoneNumber =phoneNumber).first()
    wallet.balance = wallet.balance + Decimal(credit_amount)
    wallet.save()
    serializer = WalletSerializer(wallet)
    return JsonResponse({'wallet': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND) 

@api_view(["POST"])
def debit_wallet(request, phoneNumber):
  amount = request.GET.get('amount')
  try:
      wallet = Wallet.objects.filter(phoneNumber = phoneNumber).first()
      wallet.balance = wallet.balance - Decimal(amount)
      if wallet.balance < settings.MIN_BALANCE:
        return JsonResponse({'message': 'Amount cannot be debited as minBalance needs to be mainted' }, safe=False, status=status.HTTP_400_BAD_REQUEST)
      wallet.save()
      serializer = WalletSerializer(wallet)
      return JsonResponse({'wallet': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
  except ObjectDoesNotExist as e:
      return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)      