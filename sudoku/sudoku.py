from tkinter import *

#함수 생성--------------------------

matrix = [[0 for i in range(9)] for j in range(9)]

def changer(m) : # 0으로 이루어진 9x9 행렬에 입력된 힌트를 채워 줌
    for i in range(9) :
        for j in range(9) :
            if len(globals()['e{}{}'.format(i,j)].get()) != 0 :
            # 입력창에 숫자가 써있는 경우에만
                m[i][j] = int(globals()['e{}{}'.format(i,j)].get())
                # 0으로 이루어진 9x9 행렬에 입력된 힌트를 채워 줌
    for k in m : print(k) # 행렬이 잘 생성되었는지 shall창에서 확인
    return
#---------------------------------------------------------------

blanks_location = []    

# 생성된 행렬을 이용한 스도쿠 풀이 알고리즘 작성
def determine(i, j) :
    global matrix
    det = [1,2,3,4,5,6,7,8,9]
    #행과 열 조건 만족하는지 검사
    for k in range(9) :
        if matrix[i][k] in det :
            det.remove(matrix[i][k])
        if matrix[k][j] in det :
            det.remove(matrix[k][j])

    #해당 위치를 포함하는 3x3 행렬 안에서 조건 만족하는지 검사
    i = i // 3
    j = j // 3
    for a in range(i*3, (i+1)*3) :
        for b in range(j*3, (j+1)*3) :
            if matrix[a][b] in det :
                det.remove(matrix[a][b])

    return det #이러면 빈칸에 들어갈 수 있는 숫자들만 det에 남아있다. (즉, 가능한 후보자들)
               #하지만 지금 당장 이 칸에서는 가능한 숫자더라도, 진행되면서 틀리는 경우가 있다.
               #그런 경우 다시 여기로 돌아와서 다음 후보자를 넣고 새로 진행하는 것.
               #그 알고리즘은 search에서 짤 것이다.

answer = False #답이 전부 채워졌으면 True 반환

def search(x) :
    global matrix
    global answer
    global blanks_location


    if answer == True :
        return #답이 작성된 경우 다시 답을 찾지 않기 위함

    if x == len(blanks_location) :
        #마지막 빈칸을 채운 후 정답이 잘 나왔는지 확인
        for q in matrix :
            print(q)
        #잘 나온 것을 확인했으니 entry에 정답 적어주는 알고리즘 작성 시작
        for ans in blanks_location :
            (i, j) = ans
            globals()['e{}{}'.format(i,j)].insert(0, str(matrix[i][j]))
            globals()['e{}{}'.format(i,j)]['fg'] = 'red'
        answer = True
        return

    else :
        (i, j) = blanks_location[x]
        det = determine(i, j)

        for p in det :
            matrix[i][j] = p
            search(x + 1)
            matrix[i][j] = 0     
    

def solver() : #버튼을 누르면 만든 함수를 순서대로 실행
    global matrix
    changer(matrix)
    for i in range(9) :
        for j in range(9) :
            if matrix[i][j] == 0 :
                blanks_location.append((i, j))
    search(0)

def again() :
    global answer
    global matrix
    global blanks_location
    
    matrix = [[0 for l in range(9)] for m in range(9)]
    blanks_location = []
    for i in range(9) :
        for j in range(9) :
            globals()['e{}{}'.format(i,j)].delete(0, END)
            globals()['e{}{}'.format(i,j)]['fg'] = 'black'
    answer = False

                
# UI 생성---------------------------------------

window = Tk()
window.title('Sudoku Solver')
window.geometry('532x565+200+100')        

for i in range(9) :
    for j in range(9) :
        globals()['e{}{}'.format(i,j)] = Entry(window, width = 5)
        globals()['e{}{}'.format(i,j)].grid(row = i, column = j,padx=10,
               pady=10,
               ipady=10)

button = Button(window, text = '풀어줘!', command = solver)
button.grid(row = 9, column = 4)
button = Button(window, text = '다시해볼래', command = again)
button.place(x = 330, y = 530.4)

label = Label(window, text="힌트 제외 칸은 입력하지 마세요")
label2 = Label(window, text="Made by 성찬훈")
label.place(x = 10, y = 534)
label2.place(x = 430, y = 534)

window.mainloop()
