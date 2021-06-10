def shell():
    run=True
    while run:
        code=input(">>>")
        if code=="exit();":
            run=False
        try:
            end=eval(code)
            if end:print(end)
        except:
            try:
                exec(code)
            except Exception as e:
                print("Error:"+e)
shell()                
