#importing numpy
import numpy as np

def other_funtion():
  print('Welcome!!')
  
  while True:
    
    #below are the functions which calculator can perform 
    print('1: Create Zeros in matrix')
    print('2: create ones in matrix')
    print('3: inputs in Matrix by range')
    print('4: Identity Matrix')
    print('5: Randomzzz')
    print('6: type and dimension of matrix given')
    print('7: Reshape the matrix')
    print('8: indexing and slicing')
    print('9. Unique and shuffle')
    print('10: Exit')

    #taking input
    c= input('Enter a number: ')

    if c=='1':
      n=int(input('dimension: '))
      if n==1:
        print(np.zeros(n))
      else:
        row=int(input('Enter number of rows: '))
        col=int(input('Enter number of cols: '))
        print(np.zeros((row,col)))
    elif c=='2':
      n=int(input('dimension: '))
      if n==1:
        print(np.ones(n))
      else:
        row=int(input('Enter number of rows: '))
        col=int(input('Enter number of cols: '))
        print(np.ones((row,col)))
    elif c=='3':
      n=int(input('Enter the range:'))
      print(np.arange(n))
    elif c=='4':
      n=int(input('Enter dim:'))
      if n==1:
        print(np.eye(n))
      else:
        row=int(input('Enter row; '))
        col=int(input('Enter col: '))
        print(np.eye(row,col))
    elif c=='5':
      print('Rand function used:')
      n=int(input('Enter number of Elements: '))
      print(np.random.rand(n))
      print('Randn function used:')
      m=int(input('Enter number of element:'))
      print(np.random.randn(m))
      print('Randint function of Element:')
      a=int(input('Enter Lower bound:'))
      b=int(input('Enter upper bound:'))
      c=int(input('Enter the number of element'))
      print(np.random.randint(a,b,c))
    elif c=='6':
      print('Give a Matrix:')
      row=int(input('Row'))
      col=int(input('col'))
      a=np.zeros((row,col))
      for i in range(row):
          for j in range(col):
             a[i][j]=int(input(f'[{i+1},{j+1}]'))
      print(a)
      print('Dimension:',a.ndim)
      print('Type', a.dtype)
    elif c=='7':
        row=int(input('Row'))
        col=int(input('col'))
        a=np.zeros((row,col))
        for i in range(row):
            for j in range(col):
                a[i][j]=int(input(f'[{i+1},{j+1}]'))
        print(a)
        r=int(input('Enter row to be reshaped:'))
        c=int(input('Enter col to be replaced:'))
        print(np.reshape(r,c))
    elif c=='8':
        row=int(input('Row'))
        col=int(input('col'))
        a=np.zeros((row,col))
        for i in range(row):
            for j in range(col):
                a[i][j]=int(input(f'[{i+1},{j+1}]'))
        print(a)
        n=int(input('Enter a index to find its value: '))
        print(a[n])
        q=int(input('Enter slicing starting number:'))
        w=int(input('Enter slicing ending number:'))
        print(a[q:w+1])
    elif c=='9':
        row=int(input('Row'))
        col=int(input('col'))
        a=np.zeros((row,col))
        for i in range(row):
            for j in range(col):
                a[i][j]=int(input(f'[{i+1},{j+1}]'))
        print(a)
        print('unique ',np.unique(a))
        np.random.shuffle(a)
        print('shuffled ',a)
    else:
       print('Thank!! visit again!')
       break
    
other_funtion()
