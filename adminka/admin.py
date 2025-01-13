from django.contrib import admin
from core.models import (News, NewsImage, Teacher,
                         BestSt, BestGr, BestTcOld, Olimpiada,
                         Sport, EduMatCom)
# Register your models here.

admin.site.register(News)
admin.site.register(NewsImage)
admin.site.register(Teacher)
admin.site.register(BestSt)
admin.site.register(BestGr)
admin.site.register(BestTcOld)
admin.site.register(Olimpiada)
admin.site.register(Sport)
admin.site.register(EduMatCom)