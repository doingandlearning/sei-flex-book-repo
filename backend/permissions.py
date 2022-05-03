from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    A base class from which all permission classes should inherit.
    """

    def has_permission(self, request, view):
       # Authenticated users only can see list view
        if request.user and request.user.is_authenticated:
            return True
        return False

    # Authorization
    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """

        # POST
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.creator == request.user

        # if request.method in ('GET', 'HEAD', 'OPTIONS'):  #
        #     return True
        # else:
        #     if obj.creator == request.user:
        #         return True
        #     else:
        #         return False


class IsSafeMethod(permissions.BasePermission):
    message = 'Only save http methods allowed'

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS


class IsPutOrGetMethod(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method == 'PUT' or request.method == 'GET'
        # return request.method in ['PUT', 'GET']
        # return request.method == 'PUT'


class IsAuthor(permissions.BasePermission):
    message = 'You have to be the author in order to amend this object'

    def has_object_permission(self, request, view, obj):
        # if obj.creator == request.user:
        #     return True
        # else:
        #     return False
        return obj.creator == request.user


class IsPremiumUser(permissions.BasePermission):
    message = 'You have to be a premium user for this action'

    def has_object_permission(self, request, view, obj):
        return request.user.is_premium


class IsAuthorAndPremiumUser(permissions.BasePermission):
    message = 'You have to be the author of the book as well as premium user'

    def has_object_permission(self, request, view, obj):
        # 1. Check whether the request is either 'GET', 'HEAD' or 'OPTIONS'
        if request.method in permissions.SAFE_METHODS:
            return True

        # 2. If not safe method:
        return IsAuthor.has_object_permission(self, request, view, obj) | IsPremiumUser.has_object_permission(self, request, view, obj)
