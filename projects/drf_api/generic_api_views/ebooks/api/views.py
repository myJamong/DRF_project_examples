from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from ebooks.models import Ebook, Review
from ebooks.api.pagination import SmallSetPagination
from ebooks.api.serializers import EbookSerializer, ReviewSerializer
from ebooks.api.permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly


class EbookListCreateAPIView(generics.ListCreateAPIView):
    """아래 Mixin들의 조합과 동일한 역할을 한다. 자주 사용되는 조합으로 미리 만들어진 것"""
    queryset = Ebook.objects.all().order_by("-id")
    serializer_class = EbookSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly] # 각 view별로 특정 권한을 부여할 수 있다. admin에서 로그인 하면 가능
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination

'''
class EbookListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
'''


class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, Update, Destroy, GenericAPIView 의 조합"""
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [IsAdminUserOrReadOnly]


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)

        review_author = self.request.user
        review_queryset = Review.objects.filter(ebook=ebook, review_author=review_author)
        if review_queryset.exists():
            raise ValidationError("You Have Already Reviewed this Ebook!")

        serializer.save(ebook=ebook, review_author=review_author)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]
