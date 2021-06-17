from django import forms

class UploadForm(forms.Form):
    # form field들을 class변수로 작성. 변수이름(요청파라미터 이름) = 요청파라미터 타입에 맞는 FormField
    upimg = forms.ImageField()

