students=[]
students= ["ashu",'23',"dive"]
try:
    del students[3]
except:
    print("list out of index")
finally:
    print("by default")
    