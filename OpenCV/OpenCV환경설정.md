- open cv 개발 환경 만들기.. 
- 가상 환경 생성

conda create -n cv2 python=3.8

- 가상환경 활성화시킴
conda activate cv2

- 패키지들 설치 
pip install opencv-contrib-python :contrib 확장해서 추가적으로 더 설치하는 것이다.                                
pip install jupyter matplotlib pillow : python기반으로 만들어진.. 이미지 다루는 툴                 

- matplotlib 폰트설정. //cv2 에 따로 matplotlib을 설치했기때문에  ....                             
C:\Users\Playdata\Anaconda3\envs\cv2\Lib\site-packages\matplotlib\mpl-data  --> matplotlib 환경설정하는 디렉토리                        
- anaconda3/envs : 가상환경 경로를 모아놓은 디렉토리. // 가상환경별로 디렉토리가 생김 //                       

-- 설정해야하는 것들~!
#font.family:  malgun gothic
#axes.unicode_minus: False 
