# hypothesis function
def h(theta0, theta1, x):
    return theta0 + theta1 * x
# cost function
def cost(theta0, theta1, x, y):
    m = len(x)
    total_cost = 0
    for i in range(m):
        total_cost += (h(theta0, theta1, x[i]) - y[i]) ** 2
    return total_cost / (2 * m)
# gradient descent function
def gradient_descent(theta0, theta1, x, y, alpha, iterations):
    m = len(x)
    for _ in range(iterations):
        sum0 = 0
        sum1 = 0
        for i in range(m):
            sum0 += h(theta0, theta1, x[i]) - y[i]
            sum1 += (h(theta0, theta1, x[i]) - y[i]) * x[i]
        theta0 -= alpha * sum0 / m
        theta1 -= alpha * sum1 / m
    return theta0, theta1
# initialize parameters
theta0 = 0
theta1 = 0
alpha = 0.0000001
iterations = 1000
# training data 
# size of house in square feet
size = [2104, 1416, 1534, 852, 1940, 2000, 1890, 4478, 1268, 2300]

# prices of house in (1000 $)
price = [400, 232, 315, 178, 400, 380, 360, 500, 200, 450]
# perform gradient descent
theta0, theta1 = gradient_descent(theta0, theta1, size, price, alpha, iterations)
print(f"Optimized parameters: theta0 = {theta0}, theta1 = {theta1}")
# predict price for a new house
new_size = 852
predicted_price = h(theta0, theta1, new_size)
print(f"Predicted price for a house of size {new_size} sq ft: {predicted_price} (in 1000 $)")