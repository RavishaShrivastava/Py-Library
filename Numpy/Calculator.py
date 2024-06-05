#importing numpy library
import numpy as np

#A function defined to perform calculation using numpy
def simple_cal():

  #displaying welcome message
  print("Welcome to simple calculator")

  while True:
    #displaying the function a calculator can perform 
    print('1: Add 2 Arrays')
    print('2: sub 2 Arrays')
    print('3: div Array')
    print('4: mod Array')
    print('5: mul Array')
    print('6: Min Elem in Array')
    print('7: Max Ele in Array')
    print('8: squart root')
    print('9: Power')
    print('10: reciprocal')
    print('11: sin and cos')
    print('12: Exit the cal')
    #12 different types of action can be performed

    #taking int input from user(the integer should be selected from above displayed number)
    c = input('Enter the number of your choice: ') 

    # 2 matrix are used in following input values
    if c == '1' or c=='2' or c=='3' or c=='4' or c=='5':  
      #input are taken in matrix format
      row = int(input('Enter row: '))
      col = int(input('Enter col: '))

      #defining a zeros matrix and replacing that values with user given inputs
      a=np.zeros((row,col))
      for i in range(row):
        for j in range(col):
          a[i][j]=int(input(f'[{i+1},{j+1}]: '))
      print('Matrix1:\n',a)
      b=np.zeros((row,col))
      for i in range(row):
        for j in range(col):
          b[i][j]=int(input(f'[{i+1},{j+1}]: ')) 
      print('Martix2:\n',b)

      #adding 2 matrix 
      if c=='1':
        print(np.add(a,b))
        break

      #subtraction of 2 matrix
      if c=='2':
        print(np.subtract(a,b))
        break

      #dividing 2 matrix
      if c=='3':
        print(np.divide(a,b))
        break

      #mod of 2 matrix
      if c=='4':
        print(np.mod(a,b))
        break

      #multiplying 2 matrix
      else:
        print(np.multiply(a,b))
        break

    #single matrix are used in following input values
    elif c=='6' or c=='7' or c=='8' or c=='9' or c=='10' or c=='11':
      row=int(input('Enter rows: '))
      col = int(input('Enter col: '))
      d=np.zeros((row,col))
      for i in range(row):
        for j in range(col):
          d[i][j]=int(input(f'[{i+1},{j+1}]: '))
      print(d)

      #finding the minimum element
      if c=='6':
        print(np.min(d))
        break

      #finding the maximum element 
      elif c=='7':
        print(np.max(d))
        break

      #finding the square root of elements
      elif c=='8':
        print(np.sqrt(d))
        break

      #Exponent of elements in matrix
      elif c=='9':
        p=int(input('Enter a expo number: '))
        print(np.power(d,p))
        break

      #Reciprocating the elements present in matrix
      elif c=='10':
        print('Reciprocal',np.reciprocal(d))
        break

      #find the trigonometry (sin and cos)
      elif c=='11':
        print('Sin:',np.sin(d))
        print('Cos:',np.cos(d))
        break
      else:
        pass

    #Exit of calculation
    else:
      break
      
simple_cal()
