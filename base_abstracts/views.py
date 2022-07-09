from django.shortcuts import render
from rest_flex_fields import FlexFieldsModelViewSet

# Create your views here.

class TrackableMixin(FlexFieldsModelViewSet):
    def create(self, request, *args, **kwargs):
        new_req = request.POST.copy()
        new_req.data = request.data.copy()
        if request.data:
            new_req.data['created_by'] = request.user.id
            new_req.data['updated_by'] = request.user.id

        return super().create(new_req, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        new_req = request.POST.copy()
        new_req.data = request.data.copy()
        if request.data:
            new_req.data['updated_by'] = request.user.id

        return super().create(new_req, *args, **kwargs)
