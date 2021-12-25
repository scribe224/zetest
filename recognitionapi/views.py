from django.shortcuts import render
import easyocr # модуль распознавания текста.
from django.core.files.storage import default_storage #так, модуль работы с хранилищем как-то завязанный с django. пока не разбирался.

from rest_framework import viewsets
from .serializers import RecognitionSerializer
from .models import Recognition
from rest_framework.views import APIView
from rest_framework.response import Response

# тут попытка сделать через viewset но непонятно, как обрабатывать post. сделал пока стандартным способом.
#class RecognitionViewSet(viewsets.ModelViewSet):
#    queryset = Recognition.objects.all().order_by('id')
#    serializer_class = RecognitionSerializer

class RecognitionView(APIView):
    def get(self, request):
        recognitions = Recognition.objects.all()
        serializer = RecognitionSerializer(recognitions, many=True)
        return Response({"recognitions": serializer.data})
    def post(self, request):
        recognition = request.data.get('status')
        print('Получены данные.')
        serializer = RecognitionSerializer(data = request.data)
        print('my file:', request.data['sourceimage'])
        #  save file (example from stackoverflow)
        file = request.FILES['sourceimage'] # мы пошли через загрузку файла, но в целом надо предусмотреть распознавание картинки в онлайн по url-у
        file_name = default_storage.save('images/'+file.name, file) # будем сохранять в папке images. по большому счету файлы нам не нужны.

        #  stackoverflow$)
        file = default_storage.open(file_name)
        file_url = default_storage.url(file_name)
        print(file)
        # а теперь давайте-ка распознаем нераспознанный текст на картинке ;)
        # напомню, жуну что путь к картинке в переменной file_name а не file.
        
        reader = easyocr.Reader(['ru', 'en'])
        resulttext = reader.readtext(file_name, detail=0, paragraph=True)
        print(type(resulttext)) # по итогу - list. Возможно из за атрибута paragraph
        print(resulttext)
        finaltext = ''
        with open('resultfile.txt', 'w') as file:
            for row in resulttext:
                file.write(row+'\n')
                finaltext += row+"\n"
        if serializer.is_valid(raise_exception=True):
                recognition_saved = serializer.save()
        return Response({"status": "created successfully", "recognition":finaltext})