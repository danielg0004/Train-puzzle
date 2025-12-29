from train import Train

# O(n^2) solution to the puzzle

def slow_algorithm(train: Train) -> int:
  train.turn_on()
  
  length = 0
  
  while True:
    length+=1
    for _ in range(length):
        train.move_forward()
        train.turn_off()
       
    for _ in range(length):
        train.move_backward()
        
    if train.read_light() == False:
        return length
    
# O(n) solution

def fast_algorithm(train: Train) -> int:
    
    s = 0
    while not check_bounded(2**s, train):
        s += 1
    
    for _ in range(2**s):
        train.turn_off()
        train.move_forward()
    
    for _ in range(1 + 2**s):
        train.move_backward()
    
    train.turn_on()
    train.move_forward()
    
    length = 1
    
    while not train.read_light():
        length += 1
        train.move_forward()
        
    return length

# Helper function that returns whether i <= n, where n is the length of the list
def check_bounded(i: int, train: Train) -> bool:
    train.move_backward()
    train.turn_off()
    train.move_forward()
    
    for _ in range(i-1):
        train.turn_on()
        train.move_forward()
    
    for _ in range(i):
        train.move_backward()
    
    res = train.read_light()
    
    train.move_forward()
    
    return res