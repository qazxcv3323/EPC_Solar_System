# EPC Solar System Defect Check Classification And EDA


## EPC_Solar_System_AI_Anlyasis

1. requirements.txt     
    - ex)pip install -r requirements.txt(Library Version)

2. Data_Generation_Candidate - Data Generation Candidate(데이터 생성 후보 모음)
    - 데이터를 생성하는 방식, 예외처리등등 생성 후보 코드
    - 실제 필리핀 기후환경과 비슷하게 데이터를 생성.

3. EPC_Solar_System_AI_Anlyasis.ipynb 
    #### data generate -> EDA -> modeling -> Best Model visualization
    - 데이터 생성 -> EDA 분석 및 시각화 -> 모델링 -> 모델 결과 시각화


## 프로세스 흐름
- 데이터 생성 및 전처리: 실제와 유사한 조건을 반영한 데이터 생성 및 전처리를 수행합니다.
- EDA 및 모델링:        데이터 탐색, 시각화, 모델링을 통해 결함에 영향을 미치는 주요 요인을 분석합니다.
    - EDA를 통한 결과에서 필요한 변수 추가(변수 추가 조건이나 예외처리 적용)
    
- 결과 분석 및 비교: 생성된 데이터와 실제 데이터를 비교하여 모델의 정확성과 신뢰성을 평가합니다.


## File Description 

EPC_Data_generate & Modeling.ipynb     =    초기 데이터 생성 & Modeling 
data_generation.py                     =    초기 데이터 생성.py
demo.ipynb                             =    초기 데이터를 이용하여 시각화와 모델링(유의미한 분석을 위해 시도)---1
modeling.ipynb                         =    시각화와 모델링결과를 활용하여 유의미한 데이터 확보 (모델링 중점)---2
Classification_test.ipynb              =    시각화와 모델링결과를 활용하여 유의미한 데이터 확보             ---3
EPC_Solar_System_AI_Anlyasis.ipynb     =    최종 데이터 생성, 분석, 모델링, 모델링 결과 시각화 및 분석.

# 개요

- 필리핀 기후환경과 비슷한 데이터를 생성하여 시각화와 모델을 돌려본 후 의미있는 결과를 뽑기 위함.
    - 여기서 모델링은 많은 Feature 중 어떤 Feature가 Defect(결함)에 가장 영향을 많이 준 Feature 인지 확인.
    - Feature간 상관관계 분석.
    - 모델링 결과를 통해 유의미한 결과를 획득하기 위함.
    - 실제 데이터가 구해지면 생성한 데이터와 실제 데이터 비교 후 시각화.

- 실제 데이터가 구해졌을때, 시각화를 통한 분석과 데이터 전처리 후 모델링 실행결과를 생성 데이터와 비교.
    - 실제데이터라 함은 우선적으로 Kaggle Data 기반으로 비지도학습으로 학습 후 labeling -> EDA -> Modeling 순서로 실행예정.
9
- 생성 데이터와 실제 데이터간의 공통 Feature에 대한 분석.
    - 그래프 비교, heatmap ,correlation 등등을 통해 유의미한 패턴이나 데이터 확인.


- 추후 통계적 기법 사용.
    - 다양한 데이터의 정규성 검정방식을 이용하여 확인.
    - ex) shapiro, anderson, kstest, jarque_bera
        ### shapiro (Shapiro-Wilk 검정):

        통계 분석: 데이터가 정규 분포를 따르는지를 확인하여 다양한 통계 분석 기법을 적용하기 전에 사용

        ### anderson (Anderson-Darling 검정):

        확률 분포 검정: 주어진 데이터가 특정 분포와 얼마나 유사한지를 평가하기 위해 사용

        ### kstest (Kolmogorov-Smirnov 검정):

        분포 검정: 주어진 데이터가 특정 분포와 일치하는지를 평가하기 위해 사용

        ### jarque_bera (Jarque-Bera 검정):

        검정 :데이터의 정규성을 평가하여 데이터 마이닝 모델의 가정을 확인합니다.



## 결론
이 프로젝트는 태양광 시스템 결함의 대한 분류와 분석을 위한 접근을 시도하였습니다.
통계적 기법과 데이터 분석, 시각화를 통해 모델의 예측 성능을 향상시키고, 실제 상황에 적용 가능한 유의미한 결과를 발견하는것을 목표로 합니다.
