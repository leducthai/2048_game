
from logic import *
from tkinter import *

window = Tk()

def start_state():
    label_archieve['first_words'] = Label(window , text = 'how big do you want your grid to be: ' , fg= 'black' )
    button_archieve['bt'] = Button(window , text= 'Start' , command= start)
    label_archieve['input_n'] = Entry(window )
    label_archieve['input_n'].grid(column= 0 , columnspan= 3 , row= 0)
    button_archieve['bt'].grid(column=4 , row=0)
    label_archieve['first_words'].grid(column= 0 , columnspan= 3 , row= 1 )

def retry_but():
    button_archieve['left_move'].grid_forget()
    button_archieve['right_move'].grid_forget()
    button_archieve['up_move'].grid_forget()
    button_archieve['down_move'].grid_forget()
    label_archieve['guild_text'].grid_forget()
    button_archieve['retry_but'].grid_forget()
    delete_grid(main_grid[0].n)
    start_state()

def nxt_state():
    label_archieve['input_n'].grid_forget()
    button_archieve['bt'].grid_forget()
    label_archieve['first_words'].grid_forget()

def start():
    ip = str(label_archieve['input_n'].get())
    label_archieve['input_n'].delete(0 , END)
    aa , bb = valid1(ip)
    if aa:
        nxt_state()
        main_grid[0] = grid(int(ip))
        main_grid[0].add_two()
        ml(main_grid[0].n )
    else:
        label_archieve['first_words'].grid_forget()
        #first_text[0] = bb
        label_archieve['first_words'] = Label(window , text = bb , fg= 'red' )
        label_archieve['first_words'].grid(column= 0 , columnspan= 3 , row= 1 )

def ml(n ):
    show_grid(n , main_grid[0].g)
    label_archieve['guild_text'] = Label(window , text= 'make your first move pls !' )
    button_archieve['left_move'] = Button(window , text = 'left' , fg= 'green' , command=l_m)
    button_archieve['right_move']= Button(window , text = 'right' , fg= 'green', command= r_m)
    button_archieve['up_move']= Button(window , text = 'up' , fg= 'green', command= u_m)
    button_archieve['down_move']= Button(window , text = 'down' , fg= 'green', command=d_m)
    button_archieve['retry_but']= Button(window , text = 'retry' , fg= 'green', command=retry_but)
    label_archieve['guild_text'].grid(column=0, columnspan= n , row=n)
    button_archieve['retry_but'].grid(column=n , row= 0)
    button_archieve['left_move'].grid(column=0 , row=n+2 )
    button_archieve['right_move'].grid(column=3 , row=n+2 )
    button_archieve['up_move'].grid(column=2 , row=n+1 )
    button_archieve['down_move'].grid(column=2 , row=n+2 )

def l_m():
    delete_grid(main_grid[0].n)
    label_archieve['guild_text'].grid_forget()
    t_f1 = main_grid[0].com_left()
    t_f2 = main_grid[0].merge_l()
    main_grid[0].com_left()
    if t_f1 or t_f2:
        main_grid[0].add_two()
    ii , jj = main_grid[0].is_on()
    label_archieve['guild_text'] = Label(window , text= jj )
    label_archieve['guild_text'].grid(column=0, columnspan= 9 , row=main_grid[0].n)
    show_grid(main_grid[0].n , main_grid[0].g)
    if not ii:
        button_archieve['left_move'].grid_forget()
        button_archieve['right_move'].grid_forget()
        button_archieve['up_move'].grid_forget()
        button_archieve['down_move'].grid_forget()

def r_m():
    delete_grid(main_grid[0].n)
    label_archieve['guild_text'].grid_forget()
    t_f1 = main_grid[0].com_right()
    t_f2 = main_grid[0].merge_r()
    main_grid[0].com_right()
    if t_f1 or t_f2:
        main_grid[0].add_two()
    ii , jj = main_grid[0].is_on()
    label_archieve['guild_text'] = Label(window , text= jj )
    label_archieve['guild_text'].grid(column=0, columnspan= 9 , row= main_grid[0].n)
    show_grid(main_grid[0].n , main_grid[0].g)
    if not ii:
        button_archieve['left_move'].grid_forget()
        button_archieve['right_move'].grid_forget()
        button_archieve['up_move'].grid_forget()
        button_archieve['down_move'].grid_forget()

def d_m():
    delete_grid(main_grid[0].n)
    label_archieve['guild_text'].grid_forget()
    main_grid[0].transpose()
    t_f1 = main_grid[0].com_right()
    t_f2 = main_grid[0].merge_r()
    main_grid[0].com_right()
    main_grid[0].reverse()
    if t_f1 or t_f2:
        main_grid[0].add_two()
    ii , jj = main_grid[0].is_on()
    label_archieve['guild_text'] = Label(window , text= jj )
    label_archieve['guild_text'].grid(column=0, columnspan= 9 , row=main_grid[0].n)
    show_grid(main_grid[0].n , main_grid[0].g)
    if not ii:
        button_archieve['left_move'].grid_forget()
        button_archieve['right_move'].grid_forget()
        button_archieve['up_move'].grid_forget()
        button_archieve['down_move'].grid_forget()
    
def u_m():
    delete_grid(main_grid[0].n)
    label_archieve['guild_text'].grid_forget()
    main_grid[0].transpose()
    t_f1 = main_grid[0].com_left()
    t_f2 = main_grid[0].merge_l()
    main_grid[0].com_left()
    main_grid[0].reverse()
    if t_f1 or t_f2:
        main_grid[0].add_two()
    ii , jj = main_grid[0].is_on()
    label_archieve['guild_text'] = Label(window , text= jj )
    label_archieve['guild_text'].grid(column=0, columnspan= 9 , row=main_grid[0].n)
    show_grid(main_grid[0].n , main_grid[0].g)
    if not ii:
        button_archieve['left_move'].grid_forget()
        button_archieve['right_move'].grid_forget()
        button_archieve['up_move'].grid_forget()
        button_archieve['down_move'].grid_forget()


def delete_grid(n ):
    for i in range(n):
        for j in range(n):
            dic[i , j].grid_forget()

def show_grid(n , g):
    for i in range(n):
        for j in range(n):
            dic[i , j] = Label(window , text= g[i][j])
    for i in range(n):
        for j in range(n):
            dic[i , j].grid(row = i , column = j)

button_archieve = {}
label_archieve = {}

main_grid = [0]
dic = {}

start_state()


window.mainloop()

