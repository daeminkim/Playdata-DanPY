### XGBoost 설치 방법
- 설치
pip install xgboost
conda install -y -c anaconda py-xgboost

- 주피터 노트북에서 바로 설치할때는 앞에 !pip install xgboost 이렇게 입력

### 나의 오류 
##### 오류 상황
 - 설치는 잘됏다고 했지만 import 를 하면                
 -- 오류 메세지 --     
XGBoostError: XGBoost Library (libxgboost.dylib) could not be loaded.
Likely causes:                   
  - 1번 원인 : OpenMP runtime is not installed (vcomp140.dll or libgomp-1.dll for Windows, libomp.dylib for Mac OSX, libgomp.so for Linux and other UNIX-like OSes).
  Mac OSX users: Run `brew install libomp` to install OpenMP runtime.                       
  - 2번 원인: You are running 32-bit Python on a 64-bit OS                              
Error message(s): ['dlopen(/Users/gimdaemin/opt/anaconda3/envs/ml/lib/python3.7/site-packages/xgboost/lib/libxgboost.dylib, 6): Library not loaded: /usr/local/opt/libomp/lib/libomp.dylib\n  Referenced from: /Users/gimdaemin/opt/anaconda3/envs/ml/lib/python3.7/site-packages/xgboost/lib/libxgboost.dylib\n  Reason: image not found']

이런 오류가 발생햇다 
- 원인
1. OpenMP runtime is not installed// 
2. You are running 32-bit Python on a 64-bit OS

- 해결 
2번 원인은 내가 현재 사용하고 있는 노트북이 Macbook Pro 이기 때문에 발생할 수 없는 오류였다 Mac os는 32bit의 파이썬을 지원하지 않기 때문이다.
1번 원인이 문제인 것인데 잘보면 오류 메세지에 Run `brew install libomp` to install OpenMP runtime. 해결 방법이 있었다. 그런데 내 맥북은 포멧을 해서 인지 brew가 없었다.(사실 brew가 뭔지도 몰랐고)
`brew install libomp` 이 명령문을 터미널에 입력했는데 brew를 찾지 못했다고 답을 받았다 그래서 brew를 설치하고 `brew install libomp` 를 입력하고 다시 XGboost 를 설치하니까 문제 해결됐다.
