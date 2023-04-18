def print_matrix(data_matrix):
  for i in range(len(data_matrix)):
    for j in range(len(data_matrix[0])):
      print(data_matrix[i][j], end=" ")
    print("")
2

def matrix_sum(matr_1, matr_2):
  new_matrix=[]
  if len(matr_1) == len(matr_2) and len(matr_1[0]) == len(matr_2):
    for i in range(len(matr_1)):
      new_matrix.append([])
      for j in range(len(matr_2)):
        new_matrix[i].append(matr_1[i][j]+matr_2[i][j])
    
  return new_matrix
3
3



# первая матрица
n_1 = int(input("Количтество строк: "))
m_1 = int(input("Количтество столбцов: "))
matrix_1=[]
for i in range(n_1):
  buf_stroka = list(map(int,input("Введите строку целиком: ").split(" ")))
  if len(buf_stroka) > m_1:
    while len(buf_stroka) > m_1:
      buf_stroka.pop()
  elif len(buf_stroka) < m_1:
    while len(buf_stroka) < m_1:
      buf_stroka.append(0)
  matrix_1.append(buf_stroka)

# вторая матрица
n_2 = int(input("Количтество строк: "))
m_2 = int(input("Количтество столбцов: "))
matrix_2=[]
for i in range(n_2):
  buf_stroka = list(map(int,input("Введите строку целиком: ").split(" ")))
  if len(buf_stroka) > m_2:
    while len(buf_stroka) > m_2:
      buf_stroka.pop()
  elif len(buf_stroka) < m_2:
    while len(buf_stroka) < m_2:
      buf_stroka.append(0)
  matrix_2.append(buf_stroka)
matrix_res=[]




#if(m_1 == n_2):
#  for i in range(n_1):
#    buf_stroka=[]
#    for j in range(m_2):
#      buf_res=0
#      for k in range(m_1):
#        buf_res+=matrix_1[i][k]*matrix_2[k][j]
#      buf_stroka.append(buf_res)
#    matrix_res.append(buf_stroka)  

#else:
#  print("Нельзя перемножать")

print_matrix(matrix_sum(matrix_1,matrix_2))