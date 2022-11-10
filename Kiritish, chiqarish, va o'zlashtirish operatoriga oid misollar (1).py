#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Begin1
a=int(input('tomonni kiriting:'))
p=4*a
print('kvadratning perimetri:',p)


# In[ ]:


#Begin2
a=int(input('tomonni kiriting:'))
S=pow(a,2)
print('kvadratning yuzasi:',S)


# In[ ]:


#Begin3
a=int(input('tomonni kiriting:'))
b=int(input('tomonni kiriting:'))
S=a*b
P=2*(a+b)
print('tortburchak yuzasi:',S)
print('tortburchak perimetri:',P)


# In[ ]:


#Begin4
d=int(input('diametrni kiriting:'))
pi=3.14
l=pi*d
print('aylana uzunligi:',l)


# In[ ]:


#Begin5
a=int(input('yon tomonni kiriting:'))
V=pow(a,3)
print('kubning xajmi:',V)


# In[ ]:


#Begin6
a=int(input('tomonni kiriting:'))
b=int(input('tomonni kiriting:'))
c=int(input('tomonni kiriting:'))
V=a*b*c
S=2*(a*b+a*c+b*c)
print('parallelipiped xajmi:',V)
print('tola sirti:',S)


# In[ ]:


#Begin7
R=int(input('radiusni kiriting:'))
pi=3.14
S=pi*pow(R,2)
L=2*pi*R
print('doira yuzasi:',S)
print('doira uzunligi:',L)


# In[ ]:


#Begin8
a=int(input('sonni kiriting:'))
b=int(input('sonni kiriting:'))
print('ikki son orta arifmetigi:',(a+b)/2)


# In[ ]:


#Begin9(berilgan sonlar manfiy emas)
a=int(input('sonni kiriting:'))
b=int(input('sonni kiriting:'))
if a<=b or b<=0:
    print('tomonlar faqat musbat boladi')
else:
    print('ikki son orta arifmetigi:',pow((a*b),1/2))


# In[ ]:


#Begin10
a=int(input('sonni kiriting:'))
b=int(input('sonni kiriting:'))
if a==0 or b==0:
    print('sonlar nolga teng bolmasligi kerak')
else:
    print('ularning yigindisi:',a+b)
    print('ularning kopaytmasi:',a*b)
    print('xar birining kvadrati:',pow(a,2),pow(b,2))


# In[ ]:


#Begin11
a=int(input('sonni kiriting:'))
b=int(input('sonni kiriting:'))
if a==0 or b==0:
    print('sonlar nolga teng bolmasligi kerak')
else:
    print('ularning yigindisi:',a+b)
    print('ularning kopaytmasi:',a*b)
    print('xar birining moduli:',abs(a),abs(b))


# In[ ]:


#Begin12
import math
a=int(input('katetlarni kiriting:'))
b=int(input('katetlarni kiriting:'))
c=math.sqrt(pow(a,2)+pow(b,2))
P=a+b+c
print('gipotenuza:',c)
print('perimetri:',P)


# In[ ]:


#Begin13
R_1=int(input('radiusni kiriting:'))
R_2=int(input('radiusni kiriting:'))
pi=3.14
S_1=pi*pow(R_1,2)
S_2=pi*pow(R_2,2)
S=abs(S_1-S_2)
print('birinchi doira yuzasi:',S_1)
print('ikkinchi doira yuzasi:',S_2)
print('yuzalar ayirmasi:',S)


# In[ ]:


#Begin14
L=int(input('aylana uzunligini kiriting:'))
pi=3.14
R=L/(2*pi)
S=pi*pow(R,2)
print('aylana radiusi:',R)
print('yuzasi:',S)


# In[ ]:


#Begin15
S=int(input('yuzani kiriting:'))
R=math.sqrt(S/pi)
D=2*R
print('radius:',R)
print('diametri:',D)


# In[ ]:


#Begin16
x_1=6
x_2=56
l=abs(x_2-x_1)
print('son oqidagi ikki nuqta orasidagi masofa:',l)


# In[ ]:


#Begin17
A=int(input('nuqtani kiriting:'))
B=int(input('nuqtani kiriting:'))
C=int(input('nuqtani kiriting:'))
AC=C-A
BC=C-B
print('AC kesma uzunligi:',AC)
print('BC kesma uzunligi:',BC)
print('kesmalar yigindisi:',AC+BC)


# In[ ]:


#Begin18
A=int(input('nuqtani kiriting:'))
B=int(input('nuqtani kiriting:'))
C=int(input('nuqtani kiriting:'))
AC=C-A
BC=abs(C-B)
print('AC kesma uzunligi:',AC)
print('BC kesma uzunligi:',BC)
print('kesmalar kopaytmasi:',AC*BC)


# In[ ]:


#Begin19
a_1=(0,4)
a_2=(6,4)
a_3=(0,0)
a_4=(6,0)
A=6
B=4
print('perimetri:',2*(A+B))
print('yuzasi',A*B)


# In[ ]:


#Begin20
x_1=int(input('nuqtani kiriting:'))
x_2=int(input('nuqtani kiriting:'))
y_1=int(input('nuqtani kiriting:'))
y_2=int(input('nuqtani kiriting:'))
d=math.sqrt(pow((x_2-x_1),2)+pow((y_2-y_1),2))
print('ikki nuqta orasidagi masofa:',d)


# In[ ]:


#Begin21
import math
x_1=int(input('nuqtani kiriting:'))
x_2=int(input('nuqtani kiriting:'))
y_1=int(input('nuqtani kiriting:'))
y_2=int(input('nuqtani kiriting:'))
x_3=int(input('nuqtani kiriting:'))
y_3=int(input('nuqtani kiriting:'))
a=math.sqrt(pow((x_1-y_1),2))
b=math.sqrt(pow((x_2-y_2),2))
c=math.sqrt(pow((x_3-y_3),2))
p=(a+b+c)*0.5
s=p*(p-a)*(p-b)*(p-c)
S=math.sqrt(s)
print(p)
print(S)


# In[ ]:


#Begin22
A=int(input('nuqtani kiriting:'))
B=int(input('nuqtani kiriting:'))
A,B=B,A
print(A)
print(B)


# In[ ]:


#Begin23
A=int(input('nuqtani kiriting:'))
B=int(input('nuqtani kiriting:'))
C=int(input('nuqtani kiriting:'))
A,B=B,A
B,C=C,B
print(A,B,C)


# In[ ]:


#Begin24
A=int(input('nuqtani kiriting:'))
B=int(input('nuqtani kiriting:'))
C=int(input('nuqtani kiriting:'))
A,C=C,A
B,C=C,B
print(A,B,C)


# In[ ]:


#Begin25
x=int(input('sonni kiriting:'))
y=3*pow(x,6)-6*pow(x,2)-7
print(y)


# In[ ]:


#Begin26
x=int(input('sonni kiriting:'))
y=4*(pow((x-3),6))-7*(pow((x-3),3))+2
print(y)
    


# In[ ]:


#Begin27
A=int(input('sonni kiriting:'))
print(pow(A,2))
print(pow(A,4))
print(pow(A,8))


# In[ ]:


#Begin28
A=int(input('sonni kiriting:'))
print(pow(A,2))
print(pow(A,3))
print(pow(A,5))
print(pow(A,10))
print(pow(A,15))


# In[ ]:


#Begin29
a=int(input('gradusni kiriting:'))
print('radian olchovi:',a*pi/180)


# In[ ]:


#Begin30
pi=180
print(3*pi/2)


# In[ ]:


#Begin31
T_F=int(input('Farangeytni kiriting:'))
T_C=(T_F-32)*5/9
print(T_C)


# In[ ]:


#Begin32
T_C=int(input('Selsiyni kiriting:'))
T_F=(T_C-32)*5/9
print(T_F)


# In[2]:


#Begin33
x=int(input('massani kiriting:'))
A=int(input('narxni kiriting:'))
y=int(input('soralayotgan massani kiriting:'))
print('1_kg konfet narxi:',A/x)
print('y_kg konfet narxi:',y*A/x)


# In[6]:


#Begin34
x=int(input('massani kiriting:'))
A=int(input('narxni kiriting:'))
y=int(input('massani kiriting:'))
B=int(input('narxni kiriting:'))
print('1_kg shokolad narxi:',A/x)
print('1_kg konfet narxi:',B/y)
print('1_kg shokolad narxi 1_kg konfet narxi farqi:',abs(A/x-(B/y)))


# In[8]:


#Begin35
V=int(input('qayiqning tezligini kiriting:'))
U=int(input('oqimning tezligini kiriting:'))
T_1=int(input('oqim boyicha xarakatlanish vaqti:'))
T_2=int(input('oqimga qarshi vaqti:'))
S=V*T_1-U*T_2
print('Qayiqning yurgan yoli:',S)


# In[9]:


#Begin36
s=int(input('ular orasidagi dastlabki masofani kiriting:'))
v_1=int(input('birinchi mashina tezligi:'))
v_2=int(input('ikkinchi mashina tezligi:'))
t=int(input('soralayotgan vaqtni kiriting:'))
S=t*(v_1+v_2)+s
print('t soatdan keyin ular orasidagi masofa:',S)


# In[10]:


#Begin37
s=int(input('ular orasidagi dastlabki masofani kiriting:'))
v_1=int(input('birinchi mashina tezligi:'))
v_2=int(input('ikkinchi mashina tezligi:'))
t=int(input('soralayotgan vaqtni kiriting:'))
S=t*(v_1+v_2)-s
print('t soatdan keyin ular orasidagi masofa:',S)


# In[14]:


#Begin38
A=int(input('koefitsietni kiriting:'))
B=int(input('koefitsietni kiriting:'))
if A!=0:
    print('tenglama yechimi:',-B/A)
else:
    print('yechim mavjud emas')


# In[16]:


#Begin39
import math
A=int(input('koefitsietni kiriting:'))
B=int(input('koefitsietni kiriting:'))
C=int(input('koefitsietni kiriting:'))
D=pow(B,2)-4*A*C
x_1=(-B+math.sqrt(D)/2*A)
x_2=(-B-math.sqrt(D)/2*A)
if A!=0:
    print(x_1)
    print(x_2)
else:
    print('yechim mavjud emas')
    


# In[17]:


#Begin40
A_1=int(input('koefitsietni kiriting:'))
B_1=int(input('koefitsietni kiriting:'))
C_1=int(input('koefitsietni kiriting:'))
A_2=int(input('koefitsietni kiriting:'))
B_2=int(input('koefitsietni kiriting:'))
C_2=int(input('koefitsietni kiriting:'))
D=(A_1*B_2-A_2*B_1)
x=(C_1*B_2-C_2*B_1)/D
y=(A_1*C_2-A_2*C_1)
print(x)
print(y)


# In[ ]:


Asosiy yangiliklar
1. Sonlarning moduli  abs(a)
2. Ildiz ifodasi 
    import math
    math.sqrt(a)
3. 3 ta sonni qiymatlarini ozaro almashtirish uchun ikki  marta swap qilish kerak
     A,B=B,A
    B,C=C,A

