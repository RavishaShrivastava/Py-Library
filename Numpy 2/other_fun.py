import numpy as np
def simple_cal():
  print("Welcome to simple calculator")
  while True:
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
    c = input('Enter the number of your choice: ')
    if c == '1' or c=='2' or c=='3' or c=='4' or c=='5':
      row = int(input('Enter row: '))
      col = int(input('Enter col: '))
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
      if c=='1':
        print(np.add(a,b))
        break
      if c=='2':
        print(np.subtract(a,b))
        break
      if c=='3':
        print(np.divide(a,b))
        break
      if c=='4':
        print(np.mod(a,b))
        break
      else:
        print(np.multiply(a,b))
        break
    elif c=='6' or c=='7' or c=='8' or c=='9' or c=='10' or c=='11':
      row=int(input('Enter rows: '))
      col = int(input('Enter col: '))
      d=np.zeros((row,col))
      for i in range(row):
        for j in range(col):
          d[i][j]=int(input(f'[{i+1},{j+1}]: '))
      print(d)
      if c=='6':
        print(np.min(d))
        break
      elif c=='7':
        print(np.max(d))
        break
      elif c=='8':
        print(np.sqrt(d))
        break
      elif c=='9':
        p=int(input('Enter a expo number: '))
        print(np.power(d,p))
        break
      elif c=='10':
        print('Reciprocal',np.reciprocal(d))
        break
      elif c=='11':
        print('Sin:',np.sin(d))
        print('Cos:',np.cos(d))
        break
      else:
        pass
    else:
      break
simple_cal()