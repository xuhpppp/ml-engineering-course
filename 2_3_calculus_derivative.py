import sympy as sp

# Derivative of a function
x = sp.symbols('x')
f = sp.sin(x) * sp.exp(x)
derivative_f = sp.diff(f, x)
print("The derivative of f(x) = sin(x) * exp(x) is:")
print(derivative_f)

# Partial derivative of a multivariable function
y = sp.symbols('y')
g = sp.sin(x) * sp.cos(y)
partial_derivative_g_x = sp.diff(g, x)
partial_derivative_g_y = sp.diff(g, y)
print("\nThe partial derivative of g(x, y) = sin(x) * cos(y) with respect to x is:")
print(partial_derivative_g_x)
print("The partial derivative of g(x, y) = sin(x) * cos(y) with respect to y is:")
print(partial_derivative_g_y)

# Gradient of a multivariable function
z = sp.symbols('z')
h = sp.sin(x) * sp.cos(y) * sp.exp(z)
gradient_h = [sp.diff(h, var) for var in (x, y, z)]
print("\nThe gradient of h(x, y, z) = sin(x) * cos(y) * exp(z) is:")
print(gradient_h)
