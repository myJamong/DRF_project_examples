from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsReviewAuthorOrReadOnly(permissions.BasePermission):
    """특정 인스턴스에 대한 권한 부여"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.review_author == request.user # 리뷰를 작성한 사람만 자신의 리뷰를 수정할 수 있다.
