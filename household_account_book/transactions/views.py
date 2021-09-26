from django.shortcuts import render

from django.http import HttpResponse


def transaction_list(request):
    return HttpResponse(b"Hello World")


def transaction_new(request):
    return HttpResponse('取引の登録')


def transaction_edit(request, transaction_id):
    return HttpResponse('取引の編集')


def transaction_detail(request, transaction_id):
    return HttpResponse('取引の詳細閲覧')