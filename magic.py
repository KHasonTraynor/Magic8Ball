def MagicBall ():
    import random 
    import time
    time.sleep(1.0)
    print("Im looking to the stars")
    with open("magic.txt","r") as f:
        future = f.read()
    time.sleep(1.50)
    print("Hmm, very interesting")
    time.sleep(2.0)
    future = future.strip()
    future = future.split(', ')

    future =print("It seems the answer is \n.......... \n" + (random.choice(future)))
