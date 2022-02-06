from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from news.models import Article, Journalist


class ArticleSerializer(serializers.ModelSerializer):
    """
    ModelSerializer는 Model을 기반으로해서 만들어진 Serializer이다.
    default field와 validator를 생성해주고 create와 update를 구현해준다.
    적은 코드로 Serializer 구현이 가능하다.
    """

    # serializer 필드를 추가할 수 있다.
    time_since_publication = serializers.SerializerMethodField()

    # author = JournalistSerializer() # object 전체가 보이도록 설정 - 이경우 JournalistSerializer class가 읽히도록 위에 있어야한다.
    author = serializers.StringRelatedField() # Foreign Key로 되어 있을 때 PK가 아닌 String 형태의 값으로 보여지도록 설정


    class Meta:
        model = Article
        # fields = "__all__" # all the fields of our models
        # fields = ("title", "description", "body",) # we want to choose a couple of fields
        exclude = ("id",) # hide

    def get_time_since_publication(self, object):
        """
        get_<필드명> 형태의 함수명으로 필드의 값을 구현
        :param object: serializer가 받은 instance 오브젝트
        :return: 필드 값
        """
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    def validate(self, data):
        """
        object validation작업을 구현하는 것으로 여러 필드를 엮은 검증이 필요한 경우 사용된다.
        아래의 경우는 title과 description 필드는 동일하지 못하도록 검증 단계를 추가
        :param data: 오브젝트
        :return: 오브젝트
        """
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and Description must be different from one another.")
        return data

    def validate_title(self, value):
        """
        단일 필드에 대해서 검증이 필요한 경우 validate_<필드명> 형식으로 구현한다.
        아래의 경우 title 필드 길이가 30이상이되도록 제한을 둔다.
        :param value: 필드 값
        :return: 필드 값
        """
        if len(value) < 30:
            raise serializers.ValidationError("The title has to be at least 30 characters long.")
        return value


class JournalistSerializer(serializers.ModelSerializer):
    # 필드로 연관된 Serializer를 추가하면 리스트에 함께 보여진다.
    # articles = ArticleSerializer(many=True, read_only=True)
    articles = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="article-detail") # 각각 article에 대한 GET request hyperlink로 연결할 수 있다. view_name 옵션으로 url에서 명시한 view_name으로 연결한다.

    class Meta:
        model = Journalist
        fields = "__all__"
