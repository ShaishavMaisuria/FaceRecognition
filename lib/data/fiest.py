words=int(input("please put the words"))
total=0.0
if words<=50:
    total+=words*0.10
if words>50 and words <300:
    total+=words*0.08
if words>=300:
    total += words * 0.10
    total += words * 0.08
    total=total*0.10
print("the total value is",total)