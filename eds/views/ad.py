import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from eds.models import Ad, Category
from users.models import User

AD_ON_PAGE = 4
def root(request):
    return JsonResponse({"status": "ok"})


class AdDV(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({"id": ad.pk,
                             "name": ad.name,
                             "author": ad.author.username,
                             "price": ad.price,
                             "description": ad.description,
                             "address": [loc.name for loc in ad.author.locations.all()],
                             "is_published": ad.is_published,
                             "image": ad.image.url if ad.image else None
                             }, safe=False
                            )


class AdLV(ListView):
    model = Ad
    queryset = Ad.objects.order_by("-price")

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        paginator = Paginator(self.object_list, 4)
        page_num = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_num)

        ads = [dict(id=ad.pk,
                    name=ad.name,
                    author=ad.author.username,
                    price=ad.price,
                    description=ad.description,
                    address=[loc.name for loc in ad.author.locations.all()],
                    is_published=ad.is_published,
                    image=ad.image.url if ad.image else None)
               for ad in page_obj]

        result = {
            "items": ads,
            "num_pages": paginator.num_pages,
            "total": paginator.count
        }

        return JsonResponse(result, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdCV(CreateView):
    model = Ad
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)

        author = get_object_or_404(User, pk=ad_data["author_id"])
        category = get_object_or_404(Category, pk=ad_data["category_id"])

        new_ad = Ad.objects.create(name=ad_data["name"],
                                   price=ad_data["price"],
                                   author=author,
                                   category=category,
                                   description=ad_data["description"],
                                   is_published=ad_data.get("is_published", False)
                                   )
        return JsonResponse({"id": new_ad.pk,
                             "name": new_ad.name,
                             "author": new_ad.author.username,
                             "price": new_ad.price,
                             "description": new_ad.description,
                             "address": [loc.name for loc in new_ad.author.locations.all()],
                             "is_published": new_ad.is_published,
                             "image": new_ad.image.url if new_ad.image else None
                             })


@method_decorator(csrf_exempt, name='dispatch')
class AdUpIm(CreateView):
    model = Ad
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES.get('image')
        self.object.save()
        return JsonResponse({"id": self.object.pk,
                             "name": self.object.name,
                             "image": self.object.image.url
                             })


@method_decorator(csrf_exempt, name='dispatch')
class AdUV(UpdateView):
    model = Ad
    fields = "__all__"

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ad_data = json.loads(request.body)

        if "name" in ad_data:
            self.object.name = ad_data["name"]
        if "price" in ad_data:
            self.object.price = ad_data["price"]
        if "description" in ad_data:
            self.object.description = ad_data["description"]
        if "author_id" in ad_data:
            self.object.author_id = ad_data["author_id"]
        self.object.save()
        return JsonResponse({"id": self.object.pk,
                             "name": self.object.name,
                             "author": self.object.author.username,
                             "price": self.object.price,
                             "description": self.object.description,
                             })

@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteV(DeleteView):
    model = Ad
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        ad = self.get_object()
        ad_pk = ad.pk
        super().delete(request, *args, **kwargs)
        return JsonResponse({"id": ad_pk})
