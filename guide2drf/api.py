from rental.api_views import BorrowedViewset,FriendViewset,BelogingViewset
from rest_framework import routers

router=routers.DefaultRouter()

router.register(r'belongings',BelogingViewset)
router.register(r'friends',FriendViewset)
router.register(r'borrowed',BorrowedViewset)