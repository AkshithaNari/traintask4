t1_lgt=int(input("train1 length in m:"))
t2_lgt=int(input("train2 length in m:"))
t_s1=int(input("train1 speed in kmph: "))
t_s2=int(input("train2 speed in kmph: "))
total_length=t1_lgt+t2_lgt
rs=(t_s1+t_s2)*5/18
t=total_length/rs
print("time taken by the 1st train to cross 2nd train:",t)
