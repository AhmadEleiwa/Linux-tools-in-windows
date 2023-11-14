import sys
args = sys.argv
if len(args) > 1: 
    try:
        file = open(args[1], 'w')
        file.write('')
        file.close()
    except():
        print('no such name ' + args[1])
else:
    print("cat takes filename as an argument ")
 