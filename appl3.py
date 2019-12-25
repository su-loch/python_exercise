"""
First about string method
"""

bless = " YES, Today is Christmas Day"

if __name__=="__main__":
    print(len(bless))
    print(bless.lower())        #大写
    print(bless.upper())        #小写
    print(bless.strip())        #去除开头空格
    print(bless.replace(" is"," absolutely is"))
    print(bless.split(",")[0])
    print("is" in bless)        # in and not in method