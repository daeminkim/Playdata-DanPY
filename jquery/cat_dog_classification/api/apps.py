from django.apps import AppConfig
from tensorflow.keras import models

#project(application)이 처음 시작할 때 (장고 서버가 시작할때 ) 각각의 app에 있는 config클래스의 객체를 생성
# App이름 Config -> app에대한 설정정보를 가지고 있는 클래스.
# app이 일하면서 필요한 자원들이 있으면 이클래스의 instance/class변수로 정의 할 수 있다.
class ApiConfig(AppConfig):
    name = 'api'
    model = models.load_model(r'model\cat_dog_resnet50v2')
    



