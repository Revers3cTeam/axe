import math #line:1
import random #line:2
import pygame #line:3
import random #line:4
import tkinter as tk #line:5
from tkinter import messagebox #line:6
from time import sleep #line:7
pygame .init ()#line:8
O1110O01000010Oq1 =530 #line:10
O1110O01000010OO1 =500 #line:11
O1010O01000010OO1 =25 #line:13
O1010O01000010OOO =20 #line:14
O1010O010000O0OOO =(255 ,255 ,255 )#line:15
O1010O0O0000O0OOO =(0 ,255 ,0 )#line:16
n1110O01000010Oq1 =(0 ,0 ,128 )#line:17
O1000O0O0000O0OOO =['J','T','H','f','#','L','Z','*','D',':','7','W','U',':','+','A','#','[','E','F','?','J','J','"','?','x']#line:19
class Cube ():#line:23
    O1010O01000010OOO =20 #line:24
    w =500 #line:25
    def __init__ (OO000O0O0000O0OOO ,OO0OOO0OO000000O0 ,O00OO0O00O00OO000 =1 ,O0OOO000O0OO00OO0 =0 ,OO0OO000O00O00OO0 =(255 ,255 ,0 )):#line:26
        OO000O0O0000O0OOO .pos =OO0OOO0OO000000O0 #line:27
        OO000O0O0000O0OOO .dirnx =O00OO0O00O00OO000 #line:28
        OO000O0O0000O0OOO .dirny =O0OOO000O0OO00OO0 #line:29
        OO000O0O0000O0OOO .color =OO0OO000O00O00OO0 #line:30
    def move (O0OO0O0O0OOOO0000 ,OO0O0O0O0O00O0O00 ,O0O0OOO0OO0O00000 ):#line:32
        O0OO0O0O0OOOO0000 .dirnx =OO0O0O0O0O00O0O00 #line:33
        O0OO0O0O0OOOO0000 .dirny =O0O0OOO0OO0O00000 #line:34
        O0OO0O0O0OOOO0000 .pos =(O0OO0O0O0OOOO0000 .pos [0 ]+O0OO0O0O0OOOO0000 .dirnx ,O0OO0O0O0OOOO0000 .pos [1 ]+O0OO0O0O0OOOO0000 .dirny )#line:35
    def draw (OO0O0O000OOOOOOO0 ,OO00O00OOOOO00000 ,O0000OOOO0O0O00OO =False ):#line:38
        OO00O000OO000OO00 =OO0O0O000OOOOOOO0 .w //OO0O0O000OOOOOOO0 .O1010O01000010OOO #line:39
        OO00O0O0O00OOO00O =OO0O0O000OOOOOOO0 .pos [0 ]#line:40
        OO0O000O000O00000 =OO0O0O000OOOOOOO0 .pos [1 ]#line:41
        pygame .draw .rect (OO00O00OOOOO00000 ,OO0O0O000OOOOOOO0 .color ,(OO00O0O0O00OOO00O *OO00O000OO000OO00 +1 ,OO0O000O000O00000 *OO00O000OO000OO00 +1 ,OO00O000OO000OO00 -2 ,OO00O000OO000OO00 -2 ))#line:43
        if O0000OOOO0O0O00OO :#line:44
            O0000OOO0O0000O00 =OO00O000OO000OO00 //2 #line:45
            OO0OO0O00O0OO0O00 =3 #line:46
            OOO0000O0000OOO00 =(OO00O0O0O00OOO00O *OO00O000OO000OO00 +O0000OOO0O0000O00 -OO0OO0O00O0OO0O00 ,OO0O000O000O00000 *OO00O000OO000OO00 +8 )#line:47
            OO00O0OOOO0OO000O =(OO00O0O0O00OOO00O *OO00O000OO000OO00 +OO00O000OO000OO00 -OO0OO0O00O0OO0O00 *2 ,OO0O000O000O00000 *OO00O000OO000OO00 +8 )#line:48
            pygame .draw .circle (OO00O00OOOOO00000 ,(0 ,0 ,0 ),OOO0000O0000OOO00 ,OO0OO0O00O0OO0O00 )#line:49
            pygame .draw .circle (OO00O00OOOOO00000 ,(0 ,0 ,0 ),OO00O0OOOO0OO000O ,OO0OO0O00O0OO0O00 )#line:50
class Snake ():#line:54
    body =[]#line:55
    turns ={}#line:56
    def __init__ (O00O0000OOOO0OOO0 ,O00OO00O0000OO00O ,OO0O000O0O000000O ):#line:58
        O00O0000OOOO0OOO0 .color =O00OO00O0000OO00O #line:60
        O00O0000OOOO0OOO0 .head =Cube (OO0O000O0O000000O )#line:61
        O00O0000OOOO0OOO0 .body .append (O00O0000OOOO0OOO0 .head )#line:62
        O00O0000OOOO0OOO0 .dirnx =0 #line:63
        O00O0000OOOO0OOO0 .dirny =1 #line:64
    def move (O0O0000000000OO00 ):#line:66
        for O0O00O0000O0O00O0 in pygame .event .get ():#line:67
            if O0O00O0000O0O00O0 .type ==pygame .QUIT :#line:68
                pygame .quit ()#line:69
            O0OO0OOOOOO0O0O00 =pygame .key .get_pressed ()#line:70
            for O00OOO000OO0OOO0O in O0OO0OOOOOO0O0O00 :#line:72
                if O0OO0OOOOOO0O0O00 [pygame .K_LEFT ]:#line:73
                    O0O0000000000OO00 .dirnx =-1 #line:74
                    O0O0000000000OO00 .dirny =0 #line:75
                    O0O0000000000OO00 .turns [O0O0000000000OO00 .head .pos [:]]=[O0O0000000000OO00 .dirnx ,O0O0000000000OO00 .dirny ]#line:76
                elif O0OO0OOOOOO0O0O00 [pygame .K_RIGHT ]:#line:77
                    O0O0000000000OO00 .dirnx =1 #line:78
                    O0O0000000000OO00 .dirny =0 #line:79
                    O0O0000000000OO00 .turns [O0O0000000000OO00 .head .pos [:]]=[O0O0000000000OO00 .dirnx ,O0O0000000000OO00 .dirny ]#line:80
                elif O0OO0OOOOOO0O0O00 [pygame .K_UP ]:#line:81
                    O0O0000000000OO00 .dirny =-1 #line:82
                    O0O0000000000OO00 .dirnx =0 #line:83
                    O0O0000000000OO00 .turns [O0O0000000000OO00 .head .pos [:]]=[O0O0000000000OO00 .dirnx ,O0O0000000000OO00 .dirny ]#line:84
                elif O0OO0OOOOOO0O0O00 [pygame .K_DOWN ]:#line:85
                    O0O0000000000OO00 .dirny =1 #line:86
                    O0O0000000000OO00 .dirnx =0 #line:87
                    O0O0000000000OO00 .turns [O0O0000000000OO00 .head .pos [:]]=[O0O0000000000OO00 .dirnx ,O0O0000000000OO00 .dirny ]#line:88
        for OOO0OO0OOO00O00O0 ,OO0OOOO0OOOO00000 in enumerate (O0O0000000000OO00 .body ):#line:90
            OO00OO000O000OO00 =OO0OOOO0OOOO00000 .pos [:]#line:91
            if OO00OO000O000OO00 in O0O0000000000OO00 .turns :#line:92
                OO00OO0O0O0O00OO0 =O0O0000000000OO00 .turns [OO00OO000O000OO00 ]#line:93
                OO0OOOO0OOOO00000 .move (OO00OO0O0O0O00OO0 [0 ],OO00OO0O0O0O00OO0 [1 ])#line:94
                if OOO0OO0OOO00O00O0 ==len (O0O0000000000OO00 .body )-1 :#line:95
                    O0O0000000000OO00 .turns .pop (OO00OO000O000OO00 )#line:96
            else :#line:97
                OO0OOOO0OOOO00000 .move (OO0OOOO0OOOO00000 .dirnx ,OO0OOOO0OOOO00000 .dirny )#line:98
    def reset (OO0O0OO0O000O000O ,OO00O0000O00O000O ):#line:101
        OO0O0OO0O000O000O .head =Cube (OO00O0000O00O000O )#line:102
        OO0O0OO0O000O000O .body =[]#line:103
        OO0O0OO0O000O000O .body .append (OO0O0OO0O000O000O .head )#line:104
        OO0O0OO0O000O000O .turns ={}#line:105
        OO0O0OO0O000O000O .dirnx =0 #line:106
        OO0O0OO0O000O000O .dirny =1 #line:107
    def addCube (O0OO0O0000O0O0OOO ):#line:109
        O0OO0OO000OO00000 =O0OO0O0000O0O0OOO .body [-1 ]#line:110
        O000O0O0OO0OO0O00 ,O000OO0O00OO0O000 =O0OO0OO000OO00000 .dirnx ,O0OO0OO000OO00000 .dirny #line:111
        if O000O0O0OO0OO0O00 ==1 and O000OO0O00OO0O000 ==0 :#line:113
            O0OO0O0000O0O0OOO .body .append (Cube ((O0OO0OO000OO00000 .pos [0 ]-1 ,O0OO0OO000OO00000 .pos [1 ])))#line:114
        elif O000O0O0OO0OO0O00 ==-1 and O000OO0O00OO0O000 ==0 :#line:115
            O0OO0O0000O0O0OOO .body .append (Cube ((O0OO0OO000OO00000 .pos [0 ]+1 ,O0OO0OO000OO00000 .pos [1 ])))#line:116
        elif O000O0O0OO0OO0O00 ==0 and O000OO0O00OO0O000 ==1 :#line:117
            O0OO0O0000O0O0OOO .body .append (Cube ((O0OO0OO000OO00000 .pos [0 ],O0OO0OO000OO00000 .pos [1 ]-1 )))#line:118
        elif O000O0O0OO0OO0O00 ==0 and O000OO0O00OO0O000 ==-1 :#line:119
            O0OO0O0000O0O0OOO .body .append (Cube ((O0OO0OO000OO00000 .pos [0 ],O0OO0OO000OO00000 .pos [1 ]+1 )))#line:120
        O0OO0O0000O0O0OOO .body [-1 ].dirnx =O000O0O0OO0OO0O00 #line:122
        O0OO0O0000O0O0OOO .body [-1 ].dirny =O000OO0O00OO0O000 #line:123
    def draw (OO0O0O00O0000O0O0 ,O0OOOOO0OO00OO0OO ):#line:125
        for O000O0O0O0O00OOOO ,OO0O00O00OOOOOOO0 in enumerate (OO0O0O00O0000O0O0 .body ):#line:126
            if O000O0O0O0O00OOOO ==0 :#line:127
                OO0O00O00OOOOOOO0 .draw (O0OOOOO0OO00OO0OO ,True )#line:128
            else :#line:129
                OO0O00O00OOOOOOO0 .draw (O0OOOOO0OO00OO0OO )#line:130
def redrawWindow ():#line:134
	global win #line:135
	global O1000O0O0000O0OOO #line:136
	win .fill ((0 ,0 ,0 ))#line:137
	drawGrid (O1110O01000010Oq1 ,O1010O01000010OOO ,win )#line:138
	s .draw (win )#line:139
	snack .draw (win )#line:140
	O000O0OOOO0OO00O0 =pygame .font .SysFont('arial', 40)#line:141
	O000OO00O0OOO0OOO =O000O0OOOO0OO00O0 .render ("".join (O1000O0O0000O0OOO ),True ,O1010O0O0000O0OOO )#line:142
	O0O000O00O0O00000 =O000OO00O0OOO0OOO .get_rect ()#line:143
	win .blit (O000OO00O0OOO0OOO ,O0O000O00O0O00000 )#line:144
	pygame .display .update ()#line:145
	pass #line:146
def drawGrid (OO0OOO0OO00O00OO0 ,OO000OOO0O0OOOO00 ,OOOOOOOO0000OO0OO ):#line:150
    OOO0OOOOOO0OOO000 =OO0OOO0OO00O00OO0 //OO000OOO0O0OOOO00 #line:151
    O000O00OO0000000O =0 #line:153
    O0000000000O00O0O =0 #line:154
    for OO00O0O00O0000OO0 in range (OO000OOO0O0OOOO00 ):#line:155
        O000O00OO0000000O =O000O00OO0000000O +OOO0OOOOOO0OOO000 #line:156
        O0000000000O00O0O =O0000000000O00O0O +OOO0OOOOOO0OOO000 #line:157
        pygame .draw .line (OOOOOOOO0000OO0OO ,(0 ,0 ,0 ),(O000O00OO0000000O ,0 ),(O000O00OO0000000O ,OO0OOO0OO00O00OO0 ))#line:159
        pygame .draw .line (OOOOOOOO0000OO0OO ,(0 ,0 ,0 ),(0 ,O0000000000O00O0O ),(OO0OOO0OO00O00OO0 ,O0000000000O00O0O ))#line:160
def randomSnack (O0000O0OO00O00OOO ,OO0OOOO00OO0O000O ):#line:164
    O00OOO0OOOO0OOOOO =OO0OOOO00OO0O000O .body #line:165
    while True :#line:167
        OO0OOOO000OOO0OOO =random .randrange (1 ,O0000O0OO00O00OOO -1 )#line:168
        O0O000O0O00OOOOOO =random .randrange (1 ,O0000O0OO00O00OOO -1 )#line:169
        if len (list (filter (lambda OO00O00OO00O00OO0 :OO00O00OO00O00OO0 .pos ==(OO0OOOO000OOO0OOO ,O0O000O0O00OOOOOO ),O00OOO0OOOO0OOOOO )))>0 :#line:170
               continue #line:171
        else :#line:172
               break #line:173
    return (OO0OOOO000OOO0OOO ,O0O000O0O00OOOOOO )#line:175
def main ():#line:178
    try:
    	global s ,snack ,win ,O1110O01000010OO1s #line:179
    	win =pygame .display .set_mode ((O1110O01000010Oq1 ,O1110O01000010OO1 ))#line:180
    	pygame .display .set_caption ('SNEAKY PETE')#line:181
    	s =Snake ((255 ,0 ,0 ),(10 ,10 ))#line:183
    	s .addCube ()#line:184
    	snack =Cube (randomSnack (O1010O01000010OOO ,s ),(0 ,255 ,0 ))#line:185
    	OO00OO0O0O00OO0O0 =pygame .time .Clock ()#line:186
    	OOOOOOO0O00O0O00O =1 #line:187
    	OO0000OOOOOOOOOO0 =-1 #line:188
    	global O1000O0O0000O0OOO #line:189
    	O0O0O00O0O00OO00O =[]#line:190
    	for OOO0O00O00OOO0O00 in range (1 ,27 ):#line:191
    		O0O0O00O0O00OO00O .append ((19 *OOO0O00O00OOO0O00 )%26 )#line:192
    	while True :#line:193
    		pygame .time .delay (50 )#line:194
    		OO00OO0O0O00OO0O0 .tick (10 +len (s .body ))#line:195
    		s .move ()#line:196
    		OO00OO0OOOOOOO000 =s .head .pos #line:197
    		if OO00OO0OOOOOOO000 [0 ]>=20 or OO00OO0OOOOOOO000 [0 ]<0 or OO00OO0OOOOOOO000 [1 ]>=20 or OO00OO0OOOOOOO000 [1 ]<0 :#line:198
    			O1000O0O0000O0OOO =['J','T','H','f','#','L','Z','*','D',':','7','W','U',':','+','A','#','[','E','F','?','J','J','"','?','x']#line:200
    			OO0000OOOOOOOOOO0 =-1 #line:201
    			s .reset ((10 ,10 ))#line:202
    		if s .body [0 ].pos ==snack .pos :#line:204
    			s .addCube ()#line:205
    			snack =Cube (randomSnack (O1010O01000010OOO ,s ),(0 ,255 ,0 ))#line:206
    			if (19 *OOOOOOO0O00O0O00O )==len (s .body ):#line:208
    				if OO0000OOOOOOOOOO0 ==-(len (O1000O0O0000O0OOO )+1 ):#line:209
    					while True :#line:210
    						for OO0OOO0O00O0O0000 in pygame .event .get ():#line:211
    							if OO0OOO0O00O0O0000 .type ==pygame .QUIT :#line:212
    								pygame .quit ()#line:213
    								quit ()#line:214
    						OO00OO0O0O00OO0O0 .tick (15 )#line:215
    				OOOOOOO0O00O0O00O +=1 #line:216
    				O1000O0O0000O0OOO [OO0000OOOOOOOOOO0 ]=chr (ord (O1000O0O0000O0OOO [OO0000OOOOOOOOOO0 ])^((19 *(27 +OO0000OOOOOOOOOO0 ))%26 +5 ))#line:217
    				OO0000OOOOOOOOOO0 -=1 #line:218
    		for O0OO00O0O0O0OO000 in range (len (s .body )):#line:219
    		    if s .body [O0OO00O0O0O0OO000 ].pos in list (map (lambda OO0OOOOO000O0OO00 :OO0OOOOO000O0OO00 .pos ,s .body [O0OO00O0O0O0OO000 +1 :])):#line:220
    		        O1000O0O0000O0OOO =['J','T','H','f','#','L','Z','*','D',':','7','W','U',':','+','A','#','[','E','F','?','J','J','"','?','x']#line:222
    		        OO0000OOOOOOOOOO0 =-1 #line:223
    		        s .reset ((10 ,10 ))#line:224
    		        break #line:225
    		redrawWindow ()#line:227
    except:
        pass
main ()#line:229
