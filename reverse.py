####import
import numpy as np
import re
import winsound

####function

w="〇"
b="●"

#盤面用配列作成関数→OK
def create_board():
    a = np.zeros(64,dtype=str)
    return a

#初期化関数→OK
def syokika_board(a):
    for i in range(64):
        if i==27 or i==36:
            a[i] = w
        elif i==28 or i==35:
            a[i] = b
        else:
            a[i] = "　" 
    return a



#盤面表示関数→OK
def print_board(a):
    print('    a    b    c    d    e    f    g    h   ')
    print('  | ― | ― | ― | ― | ― | ― | ― | ― |')
    n=1
    print('',n,end="")
    for i in range(64):             
        if (i+1) % 8 == 0:
            print('|',a[i],'|')
            print('  | ― | ― | ― | ― | ― | ― | ― | ― |')
            if n < 8:
                n=n+1
                print('',n,end="")
            
        else:
            print('|',a[i],end=" ")




#対話式着手関数→OK(途中）
def listen_player(a,turn):
    turn_judge = turn % 2
    if turn_judge == 1:
        stone = b
        rstone = w
        player ="黒番"
    elif turn_judge == 0:
        stone = w
        rstone = b
        player ="白番"
        
    print("{0} {1} のターンです。どこに打ちますか？[a1-h8]" .format(player,stone))
    print("(打つ場所がない場合は　ｐ　と入力)")
    print("⇒",end="")
    l = input()
    regex = r'^[a-h]{1}[1-8]{1}$'
    if l == "p":
        return 0
    matchObj = re.match(regex,l,flags=0)
    if matchObj is None:
        print("")
        print("▲===========エラー===========▲")
        print("a1 ～　h8 の範囲で入力してください。")
        print("▲===========エラー===========▲")
        print("")
        return 1
    else: 
        indexlist = list('abcdefgh')
        fst = (l[:1])
        end = int(l[1:])
        indexnum = int(indexlist.index(fst)) 
        lctn_num = indexnum + ( end - 1 ) * 8
        if a[lctn_num] == "　":
            reverse_all(a,lctn_num,stone,rstone)
            if flag_sum > 0:
                if player == "黒番":
                    winsound.Beep(100,500)
                else:
                    winsound.Beep(500,500)
                a[lctn_num] = stone
                return 0
            else:
                print("")
                print("▲===========エラー===========▲")
                print("相手の石が返せる場所に置いてください。")
                print("▲===========エラー===========▲")
                print("")
                return 1
        else:
            print("")
            print("▲===========エラー===========▲")
            print("既に石がある場所にはおけません。")
            print("▲===========エラー===========▲")
            print("")
            return 1


#右側リバース関数→OK
        
def reverse_r(a,lctn_num,stone,rstone):
    array_tmp = np.zeros(7,dtype=int)
    max_right = int(7 - (lctn_num % 8))
    max_chk = max_right
    global flag_r
    flag_r=0
    for i in range(max_chk):
        chk_lctn = int(lctn_num + i + 1)
        if a[chk_lctn] == rstone:
            array_tmp[i] = chk_lctn
        elif a[chk_lctn] == stone:
            for n in array_tmp:
                if not n == 0:
                    a[n] = stone
            if np.any(array_tmp!=0):
                flag_r=1
            else:
                flag_r=0
            return a
        else:
            return a

        
#右下側リバース関数→OK
        
def reverse_rd(a,lctn_num,stone,rstone):
    array_tmp = np.zeros(7,dtype=int)
    max_right = int(7 - (lctn_num % 8))
    max_down = int(7 - (lctn_num // 8))
    max_chk = min(max_right,max_down)
    global flag_rd
    flag_rd=0
    for i in range(max_chk):
        chk_lctn = int(lctn_num + i * 9 + 9)
        if a[chk_lctn] == rstone:
            array_tmp[i] = chk_lctn
        elif a[chk_lctn] == stone:
            for n in array_tmp:
                if not n == 0:
                    a[n] = stone
            if np.any(array_tmp!=0):
                flag_rd=1
            else:
                flag_rd=0
            return a
        else:
            return a               


#下側リバース関数→OK
        
def reverse_d(a,lctn_num,stone,rstone):
    array_tmp = np.zeros(7,dtype=int)
    max_down = int(7 - (lctn_num // 8))
    max_chk = max_down
    global flag_d
    flag_d=0
    for i in range(max_chk):
        chk_lctn = int(lctn_num + i * 8 + 8)
        if a[chk_lctn] == rstone:
            array_tmp[i] = chk_lctn
        elif a[chk_lctn] == stone:
            for n in array_tmp:
                if not n == 0:
                    a[n] = stone
            if np.any(array_tmp!=0):
                flag_d=1
            else:
                flag_d=0
            return a
        else:
            return a


#左下側リバース関数→OK
        
def reverse_ld(a,lctn_num,stone,rstone):
    array_tmp = np.zeros(7,dtype=int)
    max_down = int(7 - (lctn_num // 8))
    max_left = int(lctn_num % 8)
    max_chk = min(max_down,max_left)
    global flag_ld
    flag_ld=0
    for i in range(max_chk):
        chk_lctn = int(lctn_num + i * 7 + 7)
        if a[chk_lctn] == rstone:
            array_tmp[i] = chk_lctn
        elif a[chk_lctn] == stone:
            for n in array_tmp:
                if not n == 0:
                    a[n] = stone
            if np.any(array_tmp!=0):
                flag_ld=1
            else:
                flag_ld=0
            return a
        else:
            return a


#左側リバース関数→OK
        
def reverse_l(a,lctn_num,stone,rstone):
    array_tmp = np.zeros(7,dtype=int)
    max_left = int(lctn_num % 8)
    max_chk = max_left
    global flag_l
    flag_l=0    
    for i in range(max_chk):
        chk_lctn = int(lctn_num - i - 1 )
        if a[chk_lctn] == rstone:
            array_tmp[i] = chk_lctn
        elif a[chk_lctn] == stone:
            for n in array_tmp:
                if not n == 0:
                    a[n] = stone
            if np.any(array_tmp!=0):
                flag_l=1
            else:
                flag_l=0
            return a
        else:
            return a


#左上側リバース関数→OK
        
def reverse_lu(a,lctn_num,stone,rstone):
    array_tmp = np.zeros(7,dtype=int)
    max_left = int(lctn_num % 8)
    max_up = int(lctn_num // 8)
    max_chk = min(max_left,max_up)
    global flag_lu
    flag_lu=0 
    for i in range(max_chk):
        chk_lctn = int(lctn_num - i * 9 - 9 )
        if a[chk_lctn] == rstone:
            array_tmp[i] = chk_lctn
        elif a[chk_lctn] == stone:
            for n in array_tmp:
                if not n == 0:
                    a[n] = stone
            if np.any(array_tmp!=0):
                flag_lu=1
            else:
                flag_lu=0
            return a
        else:
            return a

#上側リバース関数→OK
        
def reverse_u(a,lctn_num,stone,rstone):
    array_tmp = np.zeros(7,dtype=int)
    max_up = int(lctn_num // 8)
    max_chk = max_up
    global flag_u
    flag_u=0 
    for i in range(max_chk):
        chk_lctn = int(lctn_num - i * 8 - 8 )
        if a[chk_lctn] == rstone:
            array_tmp[i] = chk_lctn
        elif a[chk_lctn] == stone:
            for n in array_tmp:
                if not n == 0:
                    a[n] = stone
            if np.any(array_tmp!=0):
                flag_u=1
            else:
                flag_u=0
            return a
        else:
            return a

#右上側リバース関数→OK
        
def reverse_ru(a,lctn_num,stone,rstone):
    array_tmp = np.zeros(7,dtype=int)
    max_right = int(7 - (lctn_num % 8))
    max_up = int(lctn_num // 8)
    max_chk = min(max_right,max_up)
    global flag_ru
    flag_ru=0 
    for i in range(max_chk):
        chk_lctn = int(lctn_num - i * 7 - 7 )
        if a[chk_lctn] == rstone:
            array_tmp[i] = chk_lctn
        elif a[chk_lctn] == stone:
            for n in array_tmp:
                if not n == 0:
                    a[n] = stone
            if np.any(array_tmp!=0):
                flag_ru=1
            else:
                flag_ru=0
            return a
        else:
            return a

#リバース関数→OK
def reverse_all(a,lctn_num,stone,rstone):
    reverse_r(a,lctn_num,stone,rstone)
    reverse_rd(a,lctn_num,stone,rstone)
    reverse_d(a,lctn_num,stone,rstone)
    reverse_ld(a,lctn_num,stone,rstone)
    reverse_l(a,lctn_num,stone,rstone)
    reverse_lu(a,lctn_num,stone,rstone)
    reverse_u(a,lctn_num,stone,rstone)
    reverse_ru(a,lctn_num,stone,rstone)
    global flag_sum
    flag_sum=(flag_r + flag_rd + flag_d + flag_ld + flag_l + flag_lu + flag_u + flag_ru)
    return flag_sum

#プレイ関数→OK
def play_pvp():
    turn=1
    while (turn < 61):
        rslt = listen_player(a,turn)
        if rslt == 0:
            print_board(a)
            turn += 1
    else:
        print("ゲーム終了")
        winner_chk(a)



#ゲーム結果判定
def winner_chk(a):
    black_num=np.sum(a == b)
    white_num=np.sum(a == w)
    print("")
    print("☆===========ゲーム結果===========☆")
    print('黒：{0}　白：{1}' .format(black_num,white_num))
    if black_num > white_num:
        print("黒番の勝利です。")
        print("☆===========ゲーム結果===========☆")
        print("")
    elif black_num < white_num:
        print("白番の勝利です。")
        print("☆===========ゲーム結果===========☆")
        print("")
    else:
        print("引き分けです。")
        print("☆===========ゲーム結果===========☆")
        print("")

###実行


a = create_board()
syokika_board(a)
print_board(a)
play_pvp()

