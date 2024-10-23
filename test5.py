def fun1():
    print('Reached fun1')
    
    def fun2():
        #nested definition
        print('Inner avatar')
        
    print ('Outer Avatar')
    fun2()
    
fun1()

print (type(fun1))