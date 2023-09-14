import pandas as pd
# import matplotlib.pyplot as plt
import numpy
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error



def crypto_map():
    file = open('crypto_w_abrev.txt')
    full_to_abrev = {}

    for line in file.readlines():
        temp = line.split()
        abbreviation = temp[-1]
        full_name = temp[0]
        for i in range(1, len(temp) - 1):
            full_name += ' ' + temp[i]
        full_to_abrev[full_name] = abbreviation
    return full_to_abrev

def get_price(name):
    map = crypto_map()
    ticker = map[name]
    print('Getting price for ' + ticker)
    df = pd.read_csv(ticker + '.csv', index_col='time')
    df.drop(['open', 'low', 'high', 'volumefrom', 'volumeto'], axis=1, inplace=True)
    return df

def create_dataset(dataset, look_back=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back-1):
		a = dataset[i:(i+look_back), 0]
		dataX.append(a)
		dataY.append(dataset[i + look_back, 0])
	return numpy.array(dataX), numpy.array(dataY)

def simple_train(name):
    price = get_price(name)
    dataset = price.values
    dataset = dataset.astype('float32')
    # print(dataset)
    
    scaler = MinMaxScaler(feature_range=(0, 1))
    dataset = scaler.fit_transform(dataset)
    # print(dataset)
    
    train_size = int(len(dataset) * 0.67)
    test_size = len(dataset) - train_size
    train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]
    # print(train, test)
    
    look_back = 1
    trainX, trainY = create_dataset(train, look_back)
    testX, testY = create_dataset(test, look_back)
    
    trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
    testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
    
    model = Sequential()
    model.add(LSTM(4, input_shape=(1, look_back))) # 4 LTSM blocks
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=2)

    trainPredict = model.predict(trainX)
    testPredict = model.predict(testX)
    
    trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
    print('Train Score: %.2f RMSE' % (trainScore))
    testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
    print('Test Score: %.2f RMSE' % (testScore))
    
    print(trainPredict)
    print(testPredict)
    
    # shift train predictions for plotting
    # trainPredictPlot = numpy.empty_like(dataset)
    # trainPredictPlot[:, :] = numpy.nan
    # trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
    # shift test predictions for plotting
    # testPredictPlot = numpy.empty_like(dataset)
    # testPredictPlot[:, :] = numpy.nan
    # testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict
    # plot baseline and predictions
    # plt.plot(scaler.inverse_transform(dataset))
    # plt.plot(trainPredictPlot)
    # plt.plot(testPredictPlot)
    # plt.show()
simple_train('Bitcoin')