import numpy as np
vertual_a_b=[3,76]

data=[[2,81],[4,93],[6,91],[8,97]]
x=[i[0] for i in data]
y=[i[1] for i in data]

a=vertual_a_b[0]
b=vertual_a_b[1]
def predict(x1):
    return a*x1+b

def mse(y_hat,y1):
    return ((y_hat,y1)**2).mean()

predict_result=[]

for i in range(len(x)):
    predict_result.append(predict(x[i]))

def final_mse(predict_result,y1):
    return mse(np.array(y1),np.array(predict_result))

for i in range(len(x)):
    print("공부한 시간=%.f, 실제점수=%.f, 예측 점수=%.f"%(x[i],y[i],predict(x[i])))
print("최종 mse:%f"+str(final_mse(predict_result,y)))



