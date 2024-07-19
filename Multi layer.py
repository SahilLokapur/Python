import math
x0=float(input("Enter the value of input X0: "))
x1=float(input("Enter the value of input X1: "))
x2=float(input("Enter the value of input X2: "))
x3=float(input("Enter the value of input X3: "))
x4=float(input("Enter the value of input X4: "))

yn=float(input("Enter the value of Output Yn:"))

alpha = float(input("Enter the value of learning rate: "))

w15 = float(input("Enter weight w15: "))
w16 = float(input("Enter weight w16: "))

w25 = float(input("Enter weight w25: "))
w26 = float(input("Enter weight w26: "))

w35 = float(input("Enter weight w35: "))
w36 = float(input("Enter weight w36: "))

w45 = float(input("Enter weight w45: "))
w46 = float(input("Enter weight w46: "))

w57 = float(input("Enter weight w57: "))
w67 = float(input("Enter weight w67: "))

b5 = float(input("Enter bias b5: "))
b6 = float(input("Enter bias b6: "))
b7 = float(input("Enter bias b7: "))
th=float(input("Enter the value of threshold: "))
epochs=1

def forward_pass(x1,x2,x3,x4,x0,yn,w15,w16,w25,w26,w35,w36,w45,w46,w57,w67,b5,b6,b7,epochs):
    i5=x1*w15+x2*w25+x3*w35+x4*w45+x0*b5
    o5=(1/(1+math.exp(-i5)))
    i6=x1*w16+x2*w26+x3*w36+x4*w46+x0*b6
    o6=(1/(1+math.exp(-i6)))
    i7=o5*w57+o6*w67+x0*b7
    o7=(1/(1+math.exp(-i7)))
    error=yn-o7
    print("value of i5 and o5 is:",i5,o5,sep="\t\t")
    print("value of i6 and o6 is:",i6,o6,sep="\t\t")
    print("value of i7 and o7 is:",i7,o7,sep="\t\t")
    print("The error value is:",error)
    if(error<=th):
        print("The error value is tolerable")
        print("The number of iterations required are:",epochs)
    else:
        print("The error value is not tolerable,update the weights and bias")
        epochs = epochs + 1
        backward_pass(o5, o6, o7, w57, w67, yn, x1, x2, x3, x4, x0, w15, w16, w25, w26, w35, w36, w45, w46, b5, b6, b7,epochs)

    return o5,o6,o7,epochs


def backward_pass(o5, o6, o7, w57, w67, yn, x1, x2, x3, x4, x0, w15, w16, w25, w26, w35, w36, w45, w46, b5, b6, b7,epochs):
    e7=o7*(1-o7)*(1-o7)
    e6=o6*(1-o6)*e7*w67
    e5=o5*(1-o5)*e7*w57
    print("the error at each nodes is:",e7,e6,e5)
    w15=w15+alpha*e5*1
    w16=w16+alpha*e6*1
    w25=w25+alpha*e5*1
    w26=w26+alpha*e6*1
    w35=w35+alpha*e5*0
    w36=w36+alpha*e6*0
    w45=w45+alpha*e5*1
    w46=w46+alpha*e6*1
    w57=w57+alpha*e7*o5
    w67=w67+alpha*e7*o6
    print("the updated weights are:",w15,w16,w25,w26,w35,w36,w45,w46,w57,w67)
    b5=b5+alpha*e5
    b6 = b6 + alpha * e6
    b7 = b7 + alpha * e7
    print("the updated bias are:",b5,b6,b7,"\n")
    forward_pass(x1,x2,x3,x4,x0,yn,w15,w16,w25,w26,w35,w36,w45,w46,w57,w67,b5,b6,b7,epochs)
forward_pass(x1,x2,x3,x4,x0,yn,w15,w16,w25,w26,w35,w36,w45,w46,w57,w67,b5,b6,b7,epochs)