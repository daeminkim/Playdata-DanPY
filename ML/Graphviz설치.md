# Mac graphviz 설치 

방법1) 
$brew install graphviz

방법2)
$conda install graphviz

패키지 설치 확인 
$ brew list |grep graphviz


# 순서 (내가 했던거 기준)
1. 터미널에서 conda install graphviz 를 입력하고 설치한다.
2. 설치 완료후 pip install graphviz 를 입력한다.
3. 터미널 종료후에 다시 실행한다.
- 주의 2번을 꼭해야함.. 까먹고 있다가 설치를 여러번 했었다.

### 설치 에러 "dot -c"
 
### from graphviz import Source 에러 방생 했을때 명령프롬프트를 관리자 모드로 실행시키고 
- 명령 프롬프트 ""관리자 모드""로 실행시킨 후에 dot -c 입력후 
- 다시 프롬프트 실행후에 
- 주피터 노트북 실행 

#### 에러 이름
####  CalledProcessError  
##### There is no layout engine support for "dot"
##### Perhaps "dot -c" needs to be run (with installer's privileges) to register the plugins?
