from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import ImageUploadSerializer
# from .functions import ocr_function
from .models import ImageModel
from PIL import Image  # Assuming PIL for image processing
from io import BytesIO
import numpy as np
import easyocr

# reader = easyocr.Reader(['en'], gpu=False)

class OCRViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageUploadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data['image']

            image_bytes = image.read()
            image_pil = Image.open(BytesIO(image_bytes))
            image_array = np.array(image_pil)

            # Run OCR function on the NumPy array
            # text = ocr_function(image_array)
            text = "Hello World"

            return Response({'text': text}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def ocr_function(image):
#     # image is a NumPy array
#     result = reader.readtext(image, detail=0)
#     result = " ".join(result)
#     return result