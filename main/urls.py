from rest_framework import routers
from django.urls import path
from .views import OCRViewSet

# urlpatterns = [
#     path('ocr/', OCRView.as_view(), name='ocr'),
# ]

router = routers.DefaultRouter()
router.register('ocr', OCRViewSet, basename='ocr')
urlpatterns = router.urls