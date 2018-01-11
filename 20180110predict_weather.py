import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import ShuffleSplit

trainPredFile = "C:\Users\lzhaoai\Desktop\predict_weather\ForecastDataforTraining_201712.csv"
trainTrueFile = "C:\Users\lzhaoai\Desktop\predict_weather\In_situMeasurementforTraining_201712.csv"
testPredFile = "C:\Users\lzhaoai\Desktop\predict_weather\ForecastDataforTesting_201712.csv"

file1 = trainPredFile
file2 = trainTrueFile
file3 = testPredFile

xsize = 548
ysize = 421

chunksize = xsize * ysize * 10
df_train = pd.read_csv(file1, chunksize = chunksize)
df_train_true = pd.read_csv(file2, chunksize = chunksize / 10)
df_test = pd.read_csv(file3, chunksize = chunksize)


from sklearn.neural_network import MLPRegressor

clf_p = MLPRegressor(random_state = 0)
predict = pd.DataFrame(columns = ["xid","yid","date_id","hour","wind"])
for i in range(90): 
    X_train = df_train.get_chunk(chunksize).drop(["date_id","hour"], axis = 1)
    X_train = pd.get_dummies(X_train, columns = ["model"]).values
    X_test = df_test.get_chunk(chunksize).drop(["date_id","hour"], axis = 1)
    X_test = pd.get_dummies(X_test, columns = ["model"]).values
    Data= df_train_true.get_chunk(chunksize / 10).reset_index(drop=True)
    y_train = Data["wind"].values.reshape(-1,1)
    Data.drop(["wind"],axis = 1,inplace = True)
    y_train_org = y_train.copy().ravel()
    y_train = np.kron(y_train,np.ones(10).reshape(-1,1)).ravel()
    rs = ShuffleSplit(n_splits=1, test_size=.25, random_state=0)
    for train_index, val_index in rs.split(X_train):
        X_train_train,y_train_train = X_train[train_index],y_train[train_index]
        X_train_val,y_train_val = X_train[val_index],y_train[val_index]
        clf_p.partial_fit(X_train_train,y_train_train)
        insamplemse = ((clf_p.predict(X_train_train) - y_train_train)**2).mean()
        outsamplemse = ((clf_p.predict(X_train_val) - y_train_val)**2).mean()
        y_pred = clf_p.predict(X_train)
        y_pred = np.mean(y_pred.reshape(-1,10),axis = 1)
        allsamplemse = ((y_pred - y_train_org)**2).mean()
        print "day "+str(i/18)+", hour "+str(3+i%18)+", total MSE: "+str("{:.4f}".format(insamplemse))\
        +" "+str("{:.4f}".format(outsamplemse))+" "+str("{:.4f}".format(allsamplemse))
    y_test = clf_p.predict(X_test)
    y_test = np.mean(y_test.reshape(-1,10),axis = 1)
    wind = pd.DataFrame(y_test,columns = ["wind"])
    predict = predict.append(pd.concat((Data,wind),axis = 1),ignore_index = True)
predict.to_csv("predict.csv",index = False)