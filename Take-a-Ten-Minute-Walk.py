# You live in the city of Cartesia where all roads are laid out in a perfect grid. 
# You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. 
# The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends 
# you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). 
# You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, 
# so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) 
# and will, of course, return you to your starting point. Return false otherwise.
# Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). 
# It will never give you an empty array (that's not a walk, that's standing still!).

def is_valid_walk(walk):
    #determine if walk is valid
    ns, ew = 0, 0 #two variable and initialize to 0 to track our walk, ns (North-South) and ew (East-West)
    if len(walk) == 10: #True
        for i in walk:
            if i == 'n': ns+=1 #if we move in n direction then ns += 1
            if i == 's': ns-=1 #if we move in s direction (coming back) then ns -= 1
            if i == 'w': ew+=1 #if we move in e direction then ew += 1
            if i == 'e': ew-=1 #if we move in w direction (coming back) then ew -= 1
    else:
        return False
    return ns == 0 and ew == 0 #finally we will check we returned to our same position or not

#some test cases for you...
is_valid_walk(['n','s','n','s','n','s','n','s','n','s']) #should return True
#is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']) #should return False
#is_valid_walk(['w']) #should return False
#is_valid_walk(['n','n','n','s','n','s','n','s','n','s']) #should return False