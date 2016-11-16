# 파이썬 2.x 지원용
from __future__ import unicode_literals

from django.db import models
# 파이썬 2.x 인코딩 지원
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible #python 2.x 지원

#북마크 데이타베이스 생성

class Bookmark(models.Model):
    # title 컬럼은 공백(blank) 값을 가질 수도 있고 값이 없을(null) 수도 있습니다.
    title=models.CharField(max_length=250, blank=True, null=True)
    # URLField() 필드 클래스의 첫번째 파라미터인 'url'문구는 url 컬럼에 대한 레이블 문구입니다.
    url=models.URLField('url', unique=True)

    """
    __str__() 함수는 객체를 문자열로 표현할 때 사용하는 함수입니다. 나중에 보게 될 Admin 사이트나
    장고 셀등에서 테이블 명을 보여줘야 하는데 이때 __str__()함수를 정의하지 않으면 테이블명이 제대로 표현되지 않습니다.
    """

    def __str__(self):
        return self.title
