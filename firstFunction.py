def funcy():
    print("Oh man, you just called a function!!!");

#funcy();

def DisplayRoom(text, actions):
    print(text + '\n');
    if actions is not None:
        print('Available Actions:');
        for act in actions:
            print('> ' + act);
DisplayRoom("You are in a Blank Room", None);
DisplayRoom("You are in a Normal Room", ['Go somewhwere else','Search around','Do the Hokey Pokey']);

def GenFibbonacciNumber(sequenceDepth): # Ah, the 'ol fibbonacci number generator
    try:
        int(sequenceDepth);
    except:
        return None;
    
    if sequenceDepth <= 0:
        return None;
    elif sequenceDepth == 1:
        return 0;
    elif sequenceDepth == 2:
        return 1;
    else:
        fib1 = 0;
        fib2 = 1;
        result = 0;
        for i in range(sequenceDepth - 2):
            result = fib1 + fib2;
            fib1 = fib2;
            fib2 = result;
        return result;

for i in range(100):
    print(str(GenFibbonacciNumber(i+1)));

def MixedFunction(num, streeng):
    print(str(num + 1));
    print(streeng);

MixedFunction(4, "hello");
