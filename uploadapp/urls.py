from django.urls import path,include
from .views import FileUploadView
from .views import FileViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

#router.register('blob', FileViewset)

urlpatterns = [
    #path('blob/', include(router.urls)),
    path('', FileUploadView.as_view()),
    # path('exp/', ExperimentViewSet.as_view())
]