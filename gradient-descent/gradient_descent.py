import numpy as np

data = np.loadtxt("housing_data.csv", delimiter=',', skiprows=1)

def linear_regression(w, x, b):
    return np.dot(w,x) + b

def cost_function(w,b,data):
    ret = 0
    for i in range(len(data)):
        x = data[i][0:len(data[i])-1]
        y_actual = (data[i][-1])
        y_hat = linear_regression(w,x,b)
        ret += (y_hat - y_actual)**2
    ret *= (1/(2*len(data)))

    return ret


def gradient_descent(a, w, b, data):
    w_i = np.zeros(len(data[0])-1)
    temp_b = 0
    for i in range(len(data)):
        x = data[i][0:len(data[i])-1]
        y_actual = (data[i][-1])
        y_hat = linear_regression(w,x,b)
        temp_b += (y_hat - y_actual)
        for j in range(len(w_i)):
            w_i[j] += (y_hat - y_actual) * x[j]

        
    w -= a * (1/(len(data))) * w_i
    b -= a * (1/(len(data))) * temp_b
    return w, b