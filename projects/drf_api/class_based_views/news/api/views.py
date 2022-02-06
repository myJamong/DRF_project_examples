from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from news.models import Article, Journalist
from news.api.serializers import ArticleSerializer, JournalistSerializer


class ArticleListCreateAPIView(APIView):
    """Article List 조회 및 생성"""
    def get(self, request):
        """
        GET method - Ariticle 전체에 대한 정보를 요청
        :param request: request
        :return: Response 객체
        """
        articles = Article.objects.filter(active=True) # QuerySet으로 데이터를 읽어온다.
        serializer = ArticleSerializer(articles, many=True) # QuerySet결과가 여러개라는 것을 명시하기 위해 many=True 없을 시 오류
        return Response(serializer.data)

    def post(self, request):
        """
        POST method - Article 생성 요청
        :param request: request
        :return: Response 객체
        """
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(): # 생성하려는 값들에 대한 유효성 검사
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailAPIView(APIView):
    """Article 개별적으로 DML"""
    def get_object(self, pk):
        article = get_object_or_404(Article, pk=pk) # object 존재여부 검사
        return article

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JournalistListCreateAPIView(APIView):
    def get(self, request):
        journalist = Journalist.objects.all()
        # serializer = JournalistSerializer(journalist, many=True)
        serializer = JournalistSerializer(journalist, many=True, context={"request": request})# serializer로 request를 전달하기 위한 용도로 context 옵션을 사용 - hyperlink를 사용하기 위해
        return Response(serializer.data)

    def post(self, request):
        serializer = JournalistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
