import pyautogui
import turtle

# x좌표를 받아서 해당하는 구역의 색깔로 바꿔주는 함수
def change_color(p_x):
    # 색깔별로 if문으로 나눠서 해당하는 색깔로 바꿔줌
    if p_x < -300:
        change_red()
    elif p_x < -240:
        change_orange()
    elif p_x < -180:
        change_yellow()
    elif p_x < -120:
        change_green()
    elif p_x < -60:
        change_blue()
    elif p_x < 0:
        change_navy()
    elif p_x < 60:
        change_purple()
    elif p_x < 120:
        change_black()
    else:
        change_white()

# pensize를 바꿔주는 함수
def change_pensize(p_x):
    pen_status = turtle_.pen()
    pen_size = pen_status['pensize']

    # '+'를 클릭했다면 커짐
    if p_x < 300:
        turtle_.pensize(pen_size + 1)
        turtle_.turtlesize(1 + (pen_size) / 10, 1 + (pen_size) / 10, 1 + (pen_size) / 10)
    # '-'를 클릭했다면 작아짐
    else:
        if pen_size - 1 > 0:
            turtle_.pensize(pen_size - 1)
            turtle_.turtlesize(1 + pen_size/10 - 0.1, 1 + pen_size/10 - 0.1, 1 + pen_size/10 - 0.1)

# 마우스를 클릭했을 때 처리해주는 함수
def draw(x, y):
    pos_x, pos_y = turtle_.pos()
    # 버튼 클릭 시 해당 함수 호출
    if pos_x >= -360 and pos_x <= 180 and pos_y <= 400 and pos_y >= 380:
        change_color(pos_x)
    elif pos_x >= 240 and pos_x <= 360 and pos_y <= 400 and pos_y >= 380:
        change_pensize(pos_x)
    elif pos_x >= 300 and pos_x <= 360 and pos_y <= -370 and pos_y >= -388:
        turtle_.clear()
        turtle_.turtlesize(1)
        create_buttons()
    # 버튼 클릭이 아니라면 pendown으로 그림을 그리게 함
    else:
        turtle_.pendown()

# penup으로 그림을 안 그리는 상태로 만들어 줌
def not_draw(x,y):
    turtle_.penup()

# 색깔을 바꿔주는 함수들
def change_red():
    turtle_.color('red')
def change_black():
    turtle_.color('black')
def change_orange():
    turtle_.color('orange')
def change_yellow():
    turtle_.color('yellow')
def change_green():
    turtle_.color('green')
def change_blue():
    turtle_.color('blue')
def change_navy():
    turtle_.color('navy')
def change_purple():
    turtle_.color('purple')
def change_white():
    turtle_.color('white')


# turtle이 버튼을 그리게 하는 함수
def create_buttons():
    #color buttons
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple', 'black', 'white']

    start_x, start_y = -360, 400
    h,w = 20, 60
    turtle_.color('black')
    turtle_.pensize(1)
    for i in range(9):
        turtle_.fillcolor(colors[i])
        turtle_.begin_fill()
        turtle_.goto(start_x, start_y)
        turtle_.pendown()
        turtle_.goto(start_x + w, start_y)
        turtle_.goto(start_x + w, start_y - h)
        turtle_.goto(start_x, start_y - h)
        turtle_.goto(start_x, start_y)
        turtle_.end_fill()
        turtle_.penup()

        start_x = start_x + w
    turtle_.color('black')

    # +,- buttons
    turtle_.goto(240, 400)
    turtle_.pendown()
    turtle_.goto(300, 400)
    turtle_.goto(300, 380)
    turtle_.goto(240, 380)
    turtle_.goto(240, 400)
    turtle_.goto(360, 400)
    turtle_.goto(360, 380)
    turtle_.goto(300, 380)
    turtle_.penup()

    turtle_.goto(265, 380)
    turtle_.write("+", font=("", 20))

    turtle_.goto(325, 387)
    turtle_.write("_", font=("", 20))


    #clear button
    turtle_.goto(360, -388)
    turtle_.pendown()
    turtle_.goto(300, -388)
    turtle_.goto(300, -370)
    turtle_.goto(360, -370)
    turtle_.goto(360, -388)
    turtle_.penup()

    turtle_.goto(315, -388)
    turtle_.write("clear", font=("", 15))

    turtle_.home()


# turtle 설정
turtle_ = turtle.Turtle()
turtle.setup(800, 800)      #turtle 창 크기 설정
turtle_.shape('turtle')
turtle_.speed(0)
turtle_.penup()

# 시작하자마자 버튼을을 그려줌
create_buttons()

# turtle을 마우스로 클릭했을 때 draw 함수를 호출, 땔 때 now_draw를 호출
turtle_.onclick(draw)
turtle_.onrelease(not_draw)

# 화면을 클릭했을 때 그 좌표로 turtle을 이동시킴
screen = turtle_.getscreen()
screen.onscreenclick(turtle_.goto)

# 키보드 입력을 받아서 색깔을 변경할 수 있도록 설정
screen.onkeypress(change_red, 'r')
screen.onkeypress(change_orange, "o")
screen.onkeypress(change_yellow, "y")
screen.onkeypress(change_green, "g")
screen.onkeypress(change_blue, "b")
screen.onkeypress(change_navy, "n")
screen.onkeypress(change_purple, "p")
screen.onkeypress(change_black, "space")
screen.onkeypress(change_white, "w")
screen.listen()

# 프로그램이 실행 중인 한 계속해서 turtle이 마우스를 따라다니도록 pyautogui를 사용해서 설정
x, y = pyautogui.position()
while True:
    tmp_x, tmp_y = pyautogui.position()
    tur_x, tur_y = turtle_.pos()
    turtle_.goto(tur_x + (tmp_x - x), tur_y - (tmp_y - y))
    x, y = tmp_x, tmp_y