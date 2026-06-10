Web VPython 3.2
left_eye_white = sphere(opacity=1, pos=vec(-1,5,3),radius=1,color=vec(255/255,255/255,255/255))
left_eye_pupil = sphere(opacity=1, pos=vec(0,5,4),radius=0.3,color=vec(0/255,0/255,0/255))
right_eye_white = sphere(opacity=1, pos=vec(1,5,1.5),radius=1,color=vec(255/255,255/255,255/255))
right_eye_pupil = sphere(opacity=1, pos=vec(2,5,2),radius=0.3,color=vec(0/255,0/255,0/255))      
head = sphere(opacity=1, pos=vec(-3,3,-1),radius=5,color=vec(190/255,164/255,60/255))
hand = sphere(opacity=1, pos=vec(15,-2,-4),radius=1.5,color=vec(190/255,164/255,60/255))
body = box(opacity=1,size=vec(15,-2,-2),pos=vec(6,-2,-4),color=vec(255/255,0/255,0/255))
box(opacity=1,size=vec(40,20,2),pos=vec(40,0,-4),color=vec(255/255,255/255,255/255))
arm = box(opacity=1,size=vec(10,13,5),pos=vec(-2,-7,-4),color=vec(255/255,0/255,0/255))
man = compound([left_eye_white, left_eye_pupil, head, right_eye_white, right_eye_pupil, hand, body, arm ])


q = label(text= '1번 문제) 이것은 동물인가요?', pos=vec(40,0,0))
while True :
    rate(100)
    k = keysdown()
    if 'y' in k :
        q.text = '땡!! 아닙니다!!'
    if 'n' in k : 
        q.text = '정답입니다!!'
        sleep(1)
    q.text= '2번 문제) 이것은 음식 인가요?'
    if 'left' in k :
        man.pos.x = man.pos.x - 0.1
    
  
       
       
       
