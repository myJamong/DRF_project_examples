## 웹 프레임워크는 왜 사용하는가?
Web이라는 것은 매우 유기적으로 커져왔다.
HTML이라는 작은 씨앗으로 시작해서 기하급수적으로 성장해왔다.
그래서 좋은 기능들도 많지만... 매우 복잡해졌다.
웹 프레임워크는 이러한 복잡성을 줄이기 위해 사용된다.

---
## Why Django?
우선 Django는 Python의 유일한 웹 프레임워크는 아니다. 여러 장점이 있기 때문에 사용한다.

- Large and supportive Community
- mature and stable framework
- batteries inclueded --> for any starter project there's nothing else that you need to install.
  simply use Django
- Huge third-party package ecosystem
- Pluggable structure --> able to reuse apps --> from other projects or already made.
- Django ORM
- Python

---
## Files
- manage.py : command center of your project --> 터미널에서 커맨드로 실행하는 파일. 장고 제어 기능
- project/urls.py : mostly route forward to other apps
- project/settings.py : project-wide settings
- app/urls.py : define path
- app/views.py : code logics
- app/models.py : define how database table should look like
- app/templates : html 파일 경로

---
## Django Flow
브라우저에 url 요청이 발생하면...
1. project/urls.py에 확인
2. app 단의 urls.py 파일로 포 워딩
3. views.py로 포워딩해서 로직이 발생하고
4. 랜더링되는 template으로 연결해서 화면단 결정
5. 반환

---
## ORM
Object-Relational Mapper
- makes connection between objects and relational tables.

---
## Django REST Framework (DRF)
- Django 프레임워크에서 Web API를 개발할 수 있는 Toolkit
- Django models, views와 url patterns와 통합
    - Serializers라는 클래스를 제공하여 Django models를 JSON/XML나 다른 방식으로 변환하여 return, payload 가능
    - API에 뭐가 보이고 안보이고를 views를 통해 제어하고
    - tools를 사용해서 urls와 연결하고 오브젝트가 어딨고 어떻게 제어할지 결정
- Provides mechanisms for both function and class based views
- Serialization for both ORM and non-ORM based data
- Built-in web interface

### DRF Components
- Serializers
    - Change objects into text and text back into objects
    - With or without the Django ORM
- Views
    - Utilities to write Django views that serialize and deserialize objects
- ViewSets
    - Class based view utilities encapsulating common REST/HTTP methods
- Routers
    - Map between ViewSets and Django url routes
