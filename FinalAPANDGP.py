def ArithmeticSeries(sq):
    diff=sq[1]-sq[0]
    for i in range(len(sq)-1):
        if not (sq[i+1]-sq[i]==diff):
            print("not airthmatic series")
            return False
            
                
        
    print("*********************************************")       
    print('Find the Sum of Series: PRESS 1 ')
    print('Find the term of the Series : PRESS 2 ')
    print("Find the value of given term : press 3 ")
    print("*********************************************") 
    sm=int(input('Press : '))
    if sm==1:
        n=int(input('Sum upto Series: '))
        a=sq[0]*2
        n1=n-1
        n2=n/2
                    # Sn=n
        Sn=(n2*(a+(n1)*diff))
        print('The Sum of given Series : ',Sn)
        print('======================================================')
    elif sm==2:
        tn=int(input('Term of given Series : '))  
        a1=sq[0]
        n3=tn-1
                    #t1=tn
        t1= (a1+(n3)*diff)
        print('The Trem',tn, 'of the given Series :  ',t1)
        print('======================================================')
    elif(sm==3):
        tn=int(input("enter value of Tn :"))
        a=sq[0]
        d=sq[1]-sq[0]
        N = ((tn - a)/d)+1
        print("The value of 'n' is : ",N)


def GeometricSeries(sq):
    r=(sq[1]/sq[0])
    for j in range(len(sq)-1):
        if not (sq[j+1]/sq[j]==r):
            print('This is not a Geometric Series')
            return False
          
        
    print("*********************************************")         
    print('Find the Sum of Series: PRESS 3 ')
    print('Find the term of the Series : PRESS 4 ')
    print("Find sum of infinity press 5 :")
    print("*********************************************") 
    gm=int(input('Press : '))
    if gm==3:
        n=int(input('Sum upto Series: '))
        a=sq[0]
        if (r<1):
            n1=1-r
            n2=(1-(r**n))
            Sn=a*(n2)
            sn=Sn/n1
           
            print('The Sum of given Series : ',sn)
        elif(r>1):
            n1=r-1
            n2=((r**n)-1)
            Sn=((a*(n2))/(n1))
           
            print('The Sum of given Series : ',Sn)

    elif gm==4:
        tn=int(input('Term of given Series : '))  
        a1=sq[0]
        n3=tn-1
        t1=((a1)*(r**n3))
        print('The Trem',tn, 'of the given Series :  ',t1)
        print('======================================================')
    elif gm==5:
        a=sq[0]
        inf=a/(1-r)
        print("sum of infinity is : ",inf)                  
    



try:
    print("**************************************************")
    print("AIRTHMATIC & GEOMATRIC SERIES")
    print("**************************************************")
    selseries=int( input("PRESS 1 FOR AIRTHMATIC SERIES & 2 FOR GEOMATRIC SERIES :"))
    sq=[int(s) for s in input("Enter the Series:  ").split()]
    if selseries==1:
        ArithmeticSeries(sq)
    elif selseries==2:
        GeometricSeries(sq)
    else:
        print("kindly try again")
except:
    print("something went wrong")
    print(Exception)
    

