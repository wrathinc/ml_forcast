def main():
    keyandvalue({"douge":23})
    

def keyandvalue(x):
    names = {"andy":34,"katie":27,"drew":30,"doug":24}
    age = (233,34,53,13,65)
    test = map(keyandvalue,names)
    namesDict = dict(test) 
    print(namesDict)

if __name__ == "__main__":
    main()
    pass