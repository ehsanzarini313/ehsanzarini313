# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 14:58:15 2021

@author: ehsan
"""

def player (check_board,color):
    red_pos = []
    blu_pos = []
    for i in range(8):
        for j in range(8):
            if check_board[j][i]==1 or check_board[j][i]==11:
                        move_blu = (j , i)
                        blu_pos.append(move_blu)
    print('blu_pos =' , blu_pos)
    
    for x in range(8):
        for y in range(8):
            if check_board[y][x]==2 or check_board[y][x]==22:
                move_red = (y , x)
                red_pos.append(move_red)
    print('red_pos =' , red_pos)
    
    if color == 'b':
        import random
        while True:
            a = random.choice(blu_pos)
            print( 'a =' , a )
            if check_board[a[0]][a[1]] == 11 :

                king_list = [(a[0]+1 ,a[1]+1) ,(a[0]+1,a[1]-1) , (a[0]-1 , a[1]-1) , (a[0]-1,a[1]+1)]
                king_list1 = []
                for i  in king_list:
                    if i[0] > 7 or i[0] < 0 or i[1] > 7 or i[1] < 0 :
                        king_list1.append(i)
                print(king_list , 'king_list')
                print(king_list1 , 'king_list1')
                print('blue' , blu_pos)

                b = random.choice(king_list)
                print(b , 'b')
                if b in king_list1:
                    continue
                elif check_board[b[0]][b[1]] == 0 :
                    movv = [a , b ]
                    print('movv' ,movv )
                    return(movv)
                else:
                    if b in blu_pos:
                        continue
                    if b in red_pos:
                        if b == king_list[0]:
                            b2 =(b[0]+1 , b[1]+1)
                            if 0<=b2[0] <= 7 and  0<=b2[1] <= 7:
                                if check_board[b2[0]][b2[1]] == 0:
                                    b3 = (b2[0]+1 ,b2[1]+1)
                                    if 0<=b3[0] <= 7 and  0<=b3[1] <= 7:
                                        if check_board[b3[0]][b3[1]] == 2 or check_board[b3[0]][b3[1]] == 22:
                                            b4 = (b3[0]+1 , b3[1]+1)
                                            if 0<=b4[0] <= 7 and  0<=b4[1] <= 7:
                                                if check_board[b4[0]][b4[1]] == 0:
                                                    gold_mov = [a , b4]
                                                    print('gold-move'  , gold_mov)
                                                    return(gold_mov)
                                                else:
                                                     mov_3=[a,b2]
                                                     print('king_mov_3' , mov_3)
                                                     return(mov_3)
                                            else:
                                                 mov_3=[a,b2]
                                                 print('king_mov_3' , mov_3)
                                                 return(mov_3)
                                        else:
                                            mov_2=[a,b2]
                                            print('king_mov_2' , mov_2)
                                            return(mov_2)
                                    else:  
                                        mov_1=[a,b2]
                                        print('king_mov_1' , mov_1)
                                        return(mov_1)
                                else:
                                    continue
                            else:
                                continue
                        elif b == king_list[1]:
                           b2 = (b[0]+1 , b[1]-1)
                           if 0<=b2[0] <= 7 and  0<=b2[1] <= 7:
                               if check_board[b2[0]][b2[1]] == 0 :
                                   b3 = (b2[0]+1 , b2[1]-1)
                                   if 0<=b3[0] <= 7 and  0<=b3[1] <= 7:
                                       if check_board[b3[0]][b3[1]] == 2 or check_board[b3[0]][b3[1]] == 22 :
                                           b4 = (b3[0]+1 , b3[1]-1)
                                           if 0<=b4[0] <= 7 and  0<=b4[1] <= 7:
                                               if check_board[b4[0]][b4[1]] == 0 :
                                                   gold_mov2 = [a , b4]
                                                   print('gold_mov2' , gold_mov2)
                                                   return(gold_mov2)
                                               else:
                                                   mov_1 = [a , b2]
                                                   print('mov_1112' , mov_1)
                                                   return(mov_1)
                                           else:
                                               mov_1 = [a , b2]
                                               print('mov_1112' , mov_1)
                                               return(mov_1)
                                               
                                       else:
                                           mov_1 = [a , b2]
                                           print('mov_1112' , mov_1)
                                           return(mov_1)
                               
                                   else:
                                       mov_1 = [a , b2]
                                       print('mov_111' , mov_1)
                                       return(mov_1)
                               else:
                                   continue
                           else:
                               continue
                        elif b == king_list[2]:
                            b2 = (b[0]-1 , b[1]-1)
                            if 0<=b2[0] <= 7 and  0<=b2[1] <= 7:
                                if check_board[b2[0]][b2[1]]  == 0 :
                                    b3 = (b2[0]-1 , b2[1]-1 )
                                    if 0<=b3[0] <= 7 and  0<=b3[1] <= 7:
                                        if check_board[b3[0]][b3[1]] == 2 or check_board[b3[0]][b3[1]] == 22 :
                                            b4 = ( b3[0]-1 , b3[1]-1)
                                            if 0<=b4[0] <= 7 and  0<=b4[1] <= 7:
                                                if check_board[b4[0]][b4[1]] == 0 :
                                                    gold_mov3=[a , b4]
                                                    print('gold_mov3' , gold_mov3)
                                                    return(gold_mov3)
                                    
                                                else:
                                                    mov_1 = [a , b2]
                                                    print('mov_1112 '  , mov_1)
                                                    return(mov_1)
                                           
                                            
                                           
                                            else:
                                                mov_1 = [a , b2]
                                                print('mov_111 '  , mov_1)
                                                return(mov_1)
                                          
                                        else:
                                            mov_1 = [a , b2]
                                            print('mov_11 '  , mov_1)
                                            return(mov_1)
                                    else:
                                        mov_1 = [a , b2]
                                        print('mov_1 '  , mov_1)
                                        return(mov_1)
                                else:
                                    continue
                            else:
                                continue
                        else:
                            b2 = (b[0]-1 , b[1]+1)
                            if 0<=b2[0] <= 7 and  0<=b2[1] <= 7:
                                if check_board[b2[0]][b2[1]] == 0:
                                    b3=(b2[0]-1 , b2[1]+1)
                                    if 0<=b3[0] <= 7 and  0<=b3[1] <= 7:
                                        if check_board[b3[0]][b3[1]] == 2 or check_board[b3[0]][b3[1]] == 22 :
                                            b4 = (b3[0]-1 , b3[1]+1)
                                            if 0<=b3[0] <= 7 and  0<=b3[1] <= 7:
                                                if check_board[b4[0]][b4[1]] == 0 :
                                                    gold_mov4 = (a , b4)
                                                    print('gold_mov4'  , gold_mov4)
                                                    return(gold_mov4)
                                                else:
                                                     mov_1 = [a , b2]
                                                     print('mov_1112 '  , mov_1)
                                                     return(mov_1)
                                            else:
                                                mov_1 = [a , b2]
                                                print('mov_111 '  , mov_1)
                                                return(mov_1)
                                        
                                        else :
                                            mov_1 = [a , b2]
                                            print('mov_11'  , mov_1)
                                            return(mov_1)
                                    else :
                                         mov_1 = [a , b2]
                                         print('mov_1 '  , mov_1)
                                         return(mov_1)
                                else:
                                    continue
                            else:
                                continue
            if 0 < a[1] < 7 :
                
                b = [(a[0]+1 , a[1]+1) ,(a[0]+1 ,a[1]-1)]
                kik_list = []
#                m = random.choice(b)
#                print( 'm = ' , m)
                for m in b : 
                        if m in blu_pos:
                                continue
                            
                        elif m in red_pos:
                             
                            
                            if m[1]==a[1]+1:
                                k1= (m[0]+1 , m[1]+1)
                                
                                if k1 in red_pos:
                                    continue
                                else:
                                    move_k1= [a , k1]
                                    print('move_k1=',move_k1)
                                    if 0<=k1[0] <= 7 and  0<=k1[1] <= 7:
                                        if check_board[k1[0]][k1[1]]==0 :
                                           kik_list.append(move_k1)
                                        else:
                                           continue
                                    else:
                                        continue
                                
                            else:
                                
                                k2=(m[0]+1,m[1]-1)
                                move_k2 = [a ,k2]
                                
                                if k2 in red_pos :
                                    
                                    continue
                                
                                elif k2[0]>7 or k2[1]>7 or k2[1]<0:
                                    
                                    continue
                                elif move_k2 in red_pos or blu_pos:
                                    continue
                                else:
                                    
                                    move_k2 = [a ,k2]
                                    
                                    print('move k2 =' , move_k2)
                                    if 0<=k2[0] <= 7 and  0<=k2[1] <= 7 :
                                         kik_list.append(move_k2)
                                    else:
                                        continue
                                
                             
                        else:
                                mo =[a,m]
                                
                                print(mo , '1')
                                if 0<=m[0] <= 7 and  0<=m[1] <= 7 :
                                  kik_list.append(mo)
                                else:
                                    continue
                if len(kik_list)  != 0 :
                     mov = random.choice(kik_list)
                     print('kik_list' , kik_list , mov)
                     return(mov)
                else:
                     continue
                                
                                
                                
                                
                                
                                
                                
                                
                
            elif a[1] == 0 :
                
                    n = (a[0]+1 , a[1]+1)
                    if n in red_pos:
                        n2=(n[0]+1,n[1]+1)
                        if 0<=n2[0] <= 7 and  0<=n2[1] <= 7:
                            if check_board[n2[0]][n2[1]] ==0 and -1 <n2[0]<8 and -1 <n2[1]<8:
                                n3 = (n2[0]+1 ,n2[1]+1)
                                if check_board[n3[0]][n3[1]] ==2 or check_board[n3[0]][n3[1]] ==2 and -1 <n3[0]<8 and -1 <n3[1]<8:
                                    n4 =(n3[0]+1 , n3[1]+1)
                                    if check_board[n4[0]][n4[1]] == 0 and -1 <n4[0]<8 and -1 <n4[1]<8:
                                        mov_1 =[a , n4]
                                        print('n4 = ' ,n4)
                                        if 0<=n4[0] <= 7 and  0<=n4[1] <= 7:
                                          return(mov_1)
                                        else:
                                            continue
                                    else:
                                        print('n2 =' ,n2)
                                        mov_2=[a , n2]
                                        if 0<=i[0] <= 7 and  0<=i[1] <= 7:
                                          return(mov_2)
                                        else:
                                            continue
                                else:
                                    print('n2 = ' , n2)
                                    mov_3 =[a , n2]
                                    if 0<=n2[0] <= 7 and  0<=n2[1] <= 7 :
                                      return(mov_3)
                                    else:
                                        continue
                            else:
                                 continue
                        else:
                            continue
                                
                    mo = [a,n]
                    
                    if n in blu_pos:
                         
                            continue
                    else:
                        if 0<=n[0] <= 7 and  0<=n[1] <= 7:
                           return(mo)
                           print(mo ,'2')
                        else:
                            continue
 
            elif a[1] == 7 :
                
                    n = (a[0]+1 , a[1]-1)
                    print( ' n  = ' , n)
                    
                    if n in blu_pos:
                        
                        continue
                    elif n in red_pos:
                        n1 = (n[0]+1 , n[1]-1)
                        if check_board[n1[0]][n1[1]] == 0 and -1 <n1[0]<8 and -1 <n1[1]<8:
                            n2 = (n1[0]+1 , n1[1]-1)
                            if 0<=n2[0] <= 7 and  0<=n2[1] <= 7:
                                    if check_board[n2[0]][n2[1]] == 1 or check_board[n2[0]][n2[1]] == 11 and -1 <n2[0]<8 and -1 <n2[1]<8:
                                        mov_1 = [a , n1]
                                        print('mov_1 = ' , mov_1)
                                        if 0<=n1[0] <= 7 and  0<=n1[1] <= 7:
                                          return(mov_1)
                                        else:
                                            continue
                                    elif check_board[n2[0]][n2[1]] == 2 or check_board[n2[0]][n2[1]] == 22 and -1 <n2[0]<8 and -1 <n2[1]<8 :
                                        n3 = (n2[0]+1 , n2[1]-1)
                                        if check_board[n3[0]][n3[1]] == 0 and -1 <n3[0]<8 and -1 <n3[1]<8:
                                            mov_2 = [a , n3]
                                            print('mov_2 = ' , mov_2)
                                            if 0<=n3[0] <= 7 and  0<=n3[1] <= 7:
                                                return(mov_2)
                                            else:
                                                continue
                                        else :
                                            mov_1 = [a , n1]
                                            print('mov_1_2 = ' , mov_1)
                                            if 0<=n1[0] <= 7 and  0<=n1[1] <= 7:
                                                return(mov_1)
                                            else:
                                                continue  
                            else:
                                return([a , n1])
                        else:
                            continue
                            
     
                    else:
                        mo = [a , n ]
                        print(mo , '3')  
                        if 0<=n[0] <= 7 and  0<=n[1] <= 7:
                           return(mo)
                        else:
                           continue
    if color == 'r':
        import random
        while True:
            a = random.choice(red_pos)
            print( 'a =' , a )
            if check_board[a[0]][a[1]] == 22 :

                king_list = [(a[0]+1 ,a[1]+1) ,(a[0]+1,a[1]-1) , (a[0]-1 , a[1]-1) , (a[0]-1,a[1]+1)]
                king_list1 = []
                for i  in king_list:
                    if i[0] > 7 or i[0] < 0 or i[1] > 7 or i[1] < 0 :
                        king_list1.append(i)
                print(king_list , 'king_list')
                print(king_list1 , 'king_list1')
                print('blue' , blu_pos)

                b = random.choice(king_list)
                print(b , 'b')
                if b in king_list1:
                    continue
                elif check_board[b[0]][b[1]] == 0 :
                    movv = [a , b ]
                    print('movv' ,movv )
                    return(movv)
                else:
                    if b in red_pos:
                        continue
                    if b in blu_pos:
                        if b == king_list[0]:
                            b2 =(b[0]+1 , b[1]+1)
                            if 0<=b2[0] <= 7 and  0<=b2[1] <= 7:
                                if check_board[b2[0]][b2[1]] == 0:
                                    b3 = (b2[0]+1 ,b2[1]+1)
                                    if 0<=b3[0] <= 7 and  0<=b3[1] <= 7:
                                        if check_board[b3[0]][b3[1]] == 1 or check_board[b3[0]][b3[1]] == 11:
                                            b4 = (b3[0]+1 , b3[1]+1)
                                            if 0<=b4[0] <= 7 and  0<=b4[1] <= 7:
                                                if check_board[b4[0]][b4[1]] == 0:
                                                    gold_mov = [a , b4]
                                                    print('gold-move'  , gold_mov)
                                                    return(gold_mov)
                                                else:
                                                     mov_3=[a,b2]
                                                     print('king_mov_3' , mov_3)
                                                     return(mov_3)
                                            else:
                                                 mov_3=[a,b2]
                                                 print('king_mov_3' , mov_3)
                                                 return(mov_3)
                                        else:
                                            mov_2=[a,b2]
                                            print('king_mov_2' , mov_2)
                                            return(mov_2)
                                    else:  
                                        mov_1=[a,b2]
                                        print('king_mov_1' , mov_1)
                                        return(mov_1)
                                else:
                                    continue
                            else:
                                continue
                        elif b == king_list[1]:
                           b2 = (b[0]+1 , b[1]-1)
                           if 0<=b2[0] <= 7 and  0<=b2[1] <= 7:
                               if check_board[b2[0]][b2[1]] == 0 :
                                   b3 = (b2[0]+1 , b2[1]-1)
                                   if 0<=b3[0] <= 7 and  0<=b3[1] <= 7:
                                       if check_board[b3[0]][b3[1]] == 1 or check_board[b3[0]][b3[1]] == 11 :
                                           b4 = (b3[0]+1 , b3[1]-1)
                                           if 0<=b4[0] <= 7 and  0<=b4[1] <= 7:
                                               if check_board[b4[0]][b4[1]] == 0 :
                                                   gold_mov2 = [a , b4]
                                                   print('gold_mov2' , gold_mov2)
                                                   return(gold_mov2)
                                               else:
                                                   mov_1 = [a , b2]
                                                   print('mov_1112' , mov_1)
                                                   return(mov_1)
                                           else:
                                               mov_1 = [a , b2]
                                               print('mov_1112' , mov_1)
                                               return(mov_1)
                                               
                                       else:
                                           mov_1 = [a , b2]
                                           print('mov_1112' , mov_1)
                                           return(mov_1)
                               
                                   else:
                                       mov_1 = [a , b2]
                                       print('mov_111' , mov_1)
                                       return(mov_1)
                               else:
                                   continue
                           else:
                               continue
                        elif b == king_list[2]:
                            b2 = (b[0]-1 , b[1]-1)
                            if 0<=b2[0] <= 7 and  0<=b2[1] <= 7:
                                if check_board[b2[0]][b2[1]]  == 0 :
                                    b3 = (b2[0]-1 , b2[1]-1 )
                                    if 0<=b3[0] <= 7 and  0<=b3[1] <= 7:
                                        if check_board[b3[0]][b3[1]] == 1 or check_board[b3[0]][b3[1]] == 11 :
                                            b4 = ( b3[0]-1 , b3[1]-1)
                                            if 0<=b4[0] <= 7 and  0<=b4[1] <= 7:
                                                if check_board[b4[0]][b4[1]] == 0 :
                                                    gold_mov3=[a , b4]
                                                    print('gold_mov3' , gold_mov3)
                                                    return(gold_mov3)
                                    
                                                else:
                                                    mov_1 = [a , b2]
                                                    print('mov_1112 '  , mov_1)
                                                    return(mov_1)
                                           
                                            
                                           
                                            else:
                                                mov_1 = [a , b2]
                                                print('mov_111 '  , mov_1)
                                                return(mov_1)
                                          
                                        else:
                                            mov_1 = [a , b2]
                                            print('mov_11 '  , mov_1)
                                            return(mov_1)
                                    else:
                                        mov_1 = [a , b2]
                                        print('mov_1 '  , mov_1)
                                        return(mov_1)
                                else:
                                    continue
                            else:
                                continue
                        else:
                            b2 = (b[0]-1 , b[1]+1)
                            if 0<=b2[0] <= 7 and  0<=b2[1] <= 7:
                                if check_board[b2[0]][b2[1]] == 0:
                                    b3=(b2[0]-1 , b2[1]+1)
                                    if 0<=b3[0] <= 7 and  0<=b3[1] <= 7:
                                        if check_board[b3[0]][b3[1]] == 1 or check_board[b3[0]][b3[1]] == 11 :
                                            b4 = (b3[0]-1 , b3[1]+1)
                                            if 0<=b3[0] <= 7 and  0<=b3[1] <= 7:
                                                if check_board[b4[0]][b4[1]] == 0 :
                                                    gold_mov4 = (a , b4)
                                                    print('gold_mov4'  . gold_mov4)
                                                    return(gold_mov4)
                                                else:
                                                     mov_1 = [a , b2]
                                                     print('mov_1112 '  , mov_1)
                                                     return(mov_1)
                                            else:
                                                mov_1 = [a , b2]
                                                print('mov_111 '  , mov_1)
                                                return(mov_1)
                                        
                                        else :
                                            mov_1 = [a , b2]
                                            print('mov_11'  , mov_1)
                                            return(mov_1)
                                    else :
                                         mov_1 = [a , b2]
                                         print('mov_1 '  , mov_1)
                                         return(mov_1)
                                else:
                                    continue
                            else:
                                continue
                
            if 0 < a[1] < 7 :
                
                b = [(a[0]-1 , a[1]+1) ,(a[0]-1 ,a[1]-1)]
                kik_list = []
#                m = random.choice(b)
#                print( 'm = ' , m)
                for m in b:
                        if m in red_pos:
                                continue
                            
                        elif m in blu_pos:
                             
                            
                            if m[1]==a[1]+1:
                                k1= (m[0]-1 , m[1]+1)
                                
                                if k1 in blu_pos:
                                    continue
                                else:
                                    move_k1= [a , k1]
                                    print('move_k1=',move_k1)
                                    if 0<=k1[0] <= 7 and  0<=k1[1] <= 7:
                                        if check_board[k1[0]][k1[1]]==0 :
                                           kik_list.append(move_k1)
                                        else:
                                           continue
                                    else:
                                        continue
                                
                            else:
                                
                                k2=(m[0]-1,m[1]-1)
                                move_k2 = [a ,k2]
                                
                                if k2 in red_pos :
                                    
                                    continue
                                
                                elif k2[0]>7 or k2[1]>7 or k2[1]<0:
                                    
                                    continue
                                elif move_k2 in red_pos or blu_pos:
                                    continue
                                else:
                                    
                                    move_k2 = [a ,k2]
                                    
                                    print('move k2 =' , move_k2)
                                    if 0<=k2[0] <= 7 and  0<=k2[1] <= 7 :
                                         kik_list.append(move_k2)
                                    else:
                                        continue
                                
                             
                        else:
                                mo =[a,m]
                                
                                print(mo , '1')
                                if 0<=m[0] <= 7 and  0<=m[1] <= 7 :
                                  kik_list.append(mo)
                                else:
                                    continue
                if len(kik_list)  != 0 :
                     mov = random.choice(kik_list)
                     print('kik_list' , kik_list , mov)
                     return(mov)
                else:
                     continue
            elif a[1] == 0 :
                
                    n = (a[0]-1 , a[1]+1)
                    if n in blu_pos:
                        n2=(n[0]-1,n[1]+1)
                        if 0<=n2[0] <= 7 and  0<=n2[1] <= 7:
                            if check_board[n2[0]][n2[1]] ==0 and -1 <n2[0]<8 and -1 <n2[1]<8:
                                n3 = (n2[0]-1 ,n2[1]+1)
                                if 0<=n3[0] <= 7 and  0<=n3[1] <= 7:
                                    if check_board[n3[0]][n3[1]] ==2 or check_board[n3[0]][n3[1]] ==2 and -1 <n3[0]<8 and -1 <n3[1]<8:
                                        n4 =(n3[0]-1 , n3[1]+1)
                                        if 0<=n4[0] <= 7 and  0<=n4[1] <= 7:
                                            if check_board[n4[0]][n4[1]] == 0 and -1 <n4[0]<8 and -1 <n4[1]<8:
                                                mov_1 =[a , n4]
                                                print('n4 = ' ,n4)
                                                if 0<=n4[0] <= 7 and  0<=n4[1] <= 7:
                                                  return(mov_1)
                                                else:
                                                    continue
                                            else:
                                                print('n2 =' ,n2)
                                                mov_2=[a , n2]
                                                if 0<=i[0] <= 7 and  0<=i[1] <= 7:
                                                  return(mov_2)
                                                else:
                                                    continue
                                        else:
                                            mov_4 = [a,n2]
                                            print('mov_4' , mov_4)
                                            return(mov_4)
                                    else:
                                        print('n2 = ' , n2)
                                        mov_3 =[a , n2]
                                        if 0<=n2[0] <= 7 and  0<=n2[1] <= 7 :
                                          return(mov_3)
                                        else:
                                            continue
                                else:
                                    mov_3 = [a,n2]
                                    print('mov_3' , mov_3)
                                    return(mov_3)
                                        
                            else:
                                 continue
                        else:
                            continue
                                
                    mo = [a,n]
                    
                    if n in red_pos:
                         
                            continue
                    else:
                        if 0<=n[0] <= 7 and  0<=n[1] <= 7:
                           return(mo)
                           print(mo ,'2')
                        else:
                            continue

            elif a[1] == 7 :
                
                    n = (a[0]-1 , a[1]-1)
                    print( ' n  = ' , n)
                    
                    if n in red_pos:
                        
                        continue
                    elif n in blu_pos:
                        n1 = (n[0]-1 , n[1]-1)
                        if check_board[n1[0]][n1[1]] == 0 and -1 <n1[0]<8 and -1 <n1[1]<8:
                            n2 = (n1[0]-1 , n1[1]-1)
                            if 0<=n2[0] <= 7 and  0<=n2[1] <= 7:
                                    if check_board[n2[0]][n2[1]] == 2 or check_board[n2[0]][n2[1]] == 22 and -1 <n2[0]<8 and -1 <n2[1]<8:
                                        mov_1 = [a , n1]
                                        print('mov_1 = ' , mov_1)
                                        if 0<=n1[0] <= 7 and  0<=n1[1] <= 7:
                                          return(mov_1)
                                        else:
                                            continue
                                    elif check_board[n2[0]][n2[1]] == 1 or check_board[n2[0]][n2[1]] == 11 and -1 <n2[0]<8 and -1 <n2[1]<8 :
                                        n3 = (n2[0]-1 , n2[1]-1)
                                        if 0<=n3[0] <= 7 and  0<=n3[1] <= 7:
                                            if check_board[n3[0]][n3[1]] == 0 and -1 <n3[0]<8 and -1 <n3[1]<8:
                                                mov_2 = [a , n3]
                                                print('mov_2 = ' , mov_2)
                                                if 0<=n3[0] <= 7 and  0<=n3[1] <= 7:
                                                    return(mov_2)
                                                else:
                                                    continue
                                            else :
                                                mov_1 = [a , n1]
                                                print('mov_1_2 = ' , mov_1)
                                                if 0<=n1[0] <= 7 and  0<=n1[1] <= 7:
                                                    return(mov_1)
                                                else:
                                                    continue  
                                        else:
                                            mov_5 = [a,n1]
                                            print(mov_5 , 'mov_5')
                                            return(mov_5)
                                            
                                                
                            else:
                                return([a , n1])
                        else:
                            continue
                            
     
                    else:
                        mo = [a , n ]
                        print(mo , '3')  
                        if 0<=n[0] <= 7 and  0<=n[1] <= 7:
                           return(mo)
                        else:
                           continue                    

def team_name():
	# write your team name
	name='phyton_group'
	return name