import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
import statsmodels.api as sm
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

n = 100
beta_0 = 5
beta_1 = 2

np.random.seed(1)

x = 10 * ss.uniform.rvs(size = n)
y = beta_1 * x + beta_0 + ss.norm.rvs(loc = 0, scale = 1, size = n)

plt.figure()
plt.plot(x, y, "o", ms = 5)

X = np.array([0, 10])
plt.plot(X, beta_1 * X + beta_0)

plt.xlabel("x")
plt.ylabel("y")
plt.show()

rss = []
slopes = np.arange(-10, 15, 0.001)

for slop in slopes:
    rss.append(np.sum((y - slop * x - beta_0) ** 2))

ind_min = np.argmin(rss)
print("Estimate for the slope is ", slopes[ind_min])

plt.figure()
plt.plot(slopes, rss)
plt.xlabel("Slope")
plt.ylabel("RSS")
plt.show()

mod = sm.OLS(y, x)
est = mod.fit()

print(est.summary())



X = sm.add_constant(x)
mod = sm.OLS(y, X)
est = mod.fit()

print(est.summary())

n = 500
beta_0 = 5
beta_1 = 2
beta_2 = -1

np.random.seed(1)

x_1 = 10 * ss.uniform.rvs(size = n)
x_2 = 10 * ss.uniform.rvs(size = n)

y = beta_2 * x_2 + beta_1 * x_1 + beta_0 + ss.norm.rvs(loc = 0, scale = 1, size = n)

X = np.stack([x_1, x_2], axis = 1)

fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
ax.scatter(X[:, 0], X[:, 1], y, c = y)
ax.set_xlabel("$x_1$")
ax.set_ylabel("$y_1$")
ax.set_zlabel("$z_1$")
plt.show()

lm = LinearRegression(fit_intercept = True)
lm.fit(X, y)

print("Approx of y(0) (which is equal to beta 0) is ", lm.intercept_)
print("Approx of beta 1 is", lm.coef_[0])
print("Approx of beta 2 is", lm.coef_[1])

X_0 = np.array([2, 4])
print("Prediction of y(2, 4) is: ", lm.predict(X_0.reshape(1, -1)))

print("Score (equals to R^2 value) is ", lm.score(X, y))


X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.5, random_state = 1)

lm = LinearRegression(fit_intercept = True)
lm.fit(X_train, y_train)

print(lm.score(X_test, y_test))