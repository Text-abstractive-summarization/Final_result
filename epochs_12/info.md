eT5 모델  
학습 후 모델 저장, 모델 불러와서 추가 학습 -> 반복  
  
eT5 모델에 train_data 60000개 epochs 8씩 추가학습  
  
train_data 60000 epochs 8  
train_data 120000 epochs 8  
train_data 180000 epochs 8  
train_data 240000 epochs 8  
train_data 240000 epochs 8 모델에 train_data 30000개 추가학습  
5. train_data 270000 epochs 8  
  
train_data 270000 epochs 8 모델에 train_data 270000개 epochs4 추가학습  
6. train_data 270000 epochs 12  
  
train_data 270000 epochs 12 모델에 train_data 20000개 추가학습  
7.train_data 290000 epochs 12  
  
train_data 270000 epochs 8 모델에 train_data 20000개 추가학습  
8. train_data 290000 epochs 8  
  
...  
진행중  
...  
  
google colab pro plus 사용  
runtime이 최대 24시간이므로  
여건상 시간에 맞춰 데이터를 분할하여 학습 후 모델을 저장하고, 저장한 모델에 추가학습 하는 방식으로 진행  
추후 한번에 학습한 모델과, 추가학습한 모델을 비교해 볼 예정  
