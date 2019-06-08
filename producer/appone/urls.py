from rest_framework.routers import SimpleRouter
from appone.views import *
router = SimpleRouter()
router.register("place",placeOp)
router.register("college",collegeOp)
router.register("subject",subjectOp)
router.register("department",deptOp)