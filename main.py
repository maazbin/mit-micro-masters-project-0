import numpy as np

def randomization(n):
    """
    Arg:
      n - an integer
    Returns:
      A - a randomly-generated nx1 Numpy array.
    """
    #Your code here
    A = np.random.randint(n)
    return A
    raise NotImplementedError

def operations(h, w):
    """
    Takes two inputs, h and w, and makes two Numpy arrays A and B of size
    h x w, and returns A, B, and s, the sum of A and B.

    Arg:
      h - an integer describing the height of A and B
      w - an integer describing the width of A and B
    Returns (in this order):
      A - a randomly-generated h x w Numpy array.
      B - a randomly-generated h x w Numpy array.
      s - the sum of A and B.
    """
    #Your code here
    A = np.random.randint(100,size = (h,w)) 
    B = np.random.randint(100,size = (h,w)) 
    s = A+B
    
    return A,B,s 

    raise NotImplementedError


def norm(A, B):
    """
    Takes two Numpy column arrays, A and B, and returns the L2 norm of their
    sum.

    Arg:
      A - a Numpy array
      B - a Numpy array
    Returns:
      s - the L2 norm of A+B.
    """
    #Your code here
    s = np.linalg.norm(A+B)
    
    return  s

    raise NotImplementedError


def neural_network(inputs, weights):
    """
     Takes an input vector and runs it through a 1-layer neural network
     with a given weight matrix and returns the output.

     Arg:
       inputs - 2 x 1 NumPy array
       weights - 2 x 1 NumPy array
     Returns (in this order):
       out - a 1 x 1 NumPy array, representing the output of the neural network
    """
    #Your code here
    neural_net = np.tanh(np.transpose((weights)*inputs))  #tanh(wT * inputs)
    return neural_net
    raise NotImplementedError

def scalar_function(x, y):
    """
    Returns the f(x,y) defined in the problem statement.
    """
    #Your code here
    raise NotImplementedError

def vector_function(x, y):
    """
    Make sure vector_function can deal with vector input x,y 
    """
    #Your code here
    raise NotImplementedError


def main():
  print("Randomization")  #randomization  
  for n in range(1,11):
    x = randomization(n)
    print(x)
    # print(x.shape())
  print(operations(2,2))  
  
  print()
  print()

  print('operations')   #operations
  A  ,B,s = operations(2,2)
  print(f'A : {A}')
  print(f'B : {B}')
  print(f'sum(A+B) : {s}')

  print() 
  print()

  print('norm')   #norm

  A = np.random.random([1,3])
  B = np.random.random([1,3])
  print(f'A = {A}, B = {B}')
  print(f'norm of A + B ={norm(A,B)}')

  print('neural_network')  # newral network
  
  inputs = np.random.random([2,1])
  weights = np.random.random([2,1])
  neural_net = neural_network(inputs, weights)
  print(f'single layer neural network = {neural_net}')  





main()  
