from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from utilits.util import req_cont
import json

class IndexView(APIView):
    def get(self, request, cont_num=None):
        # Извлекаем номер контейнера из параметров GET-запроса
        if cont_num is None:
            return Response({'result': f'Нет данных по контейнеру'}, status=status.HTTP_200_OK)
        result = req_cont(cont_num)

        # Здесь вы можете выполнить необходимые действия с номером контейнера
        # Например, выполнить поиск и вернуть результат

        # Возвращаем ответ
        return Response({'result': result}, status=status.HTTP_200_OK)

    # def post(self, request, *args, **kwargs):
    #     cont_num = request.data.get('cont_num')
    #     print(cont_num)
    #     return Response({"message": f"Hello, World! {cont_num}"}, status=status.HTTP_200_OK)


