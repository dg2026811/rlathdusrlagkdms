Web VPython 3.2
sphere(opacity=1, pos=vec(-3,3,-1),radius=5,color=vec(190/255,164/255,60/255))
sphere(opacity=1, pos=vec(-1,5,3),radius=1,color=vec(255/255,255/255,255/255))
sphere(opacity=1, pos=vec(1,5,1.5),radius=1,color=vec(255/255,255/255,255/255))
sphere(opacity=1, pos=vec(2,5,2),radius=0.3,color=vec(0/255,0/255,0/255))
sphere(opacity=1, pos=vec(0,5,4),radius=0.3,color=vec(0/255,0/255,0/255))
sphere(opacity=1, pos=vec(-3,3,-1),radius=5,color=vec(190/255,164/255,60/255))
sphere(opacity=1, pos=vec(15,-2,-4),radius=1.5,color=vec(190/255,164/255,60/255))
box(opacity=1,size=vec(15,-2,-2),pos=vec(6,-2,-4),color=vec(255/255,0/255,0/255))
box(opacity=1,size=vec(40,20,2),pos=vec(40,0,-4),color=vec(255/255,255/255,255/255))
box(opacity=1,size=vec(10,13,5),pos=vec(-2,-7,-4),color=vec(255/255,0/255,0/255))
label(text= '1번 문제) 이것은 동물인가요?', pos=vec(40,0,0))
while True :
    rate(100)
    k = keysdown()
    if 'left'  in k:
       b.pos.x = b.pos.x -1
    if 'right' in k: 
       b.pos.x = b.pos.x +1
    if 'up' in k:
       b.pos.y = b.pos.y +1
    if 'down' in k: 
       b.pos.y = b.pos.y -1
       label(text= '2번 문제) 이것은 사람인가요?', pos=vec(40,0,0))


       
       
       
