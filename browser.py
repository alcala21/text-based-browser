import os
import sys


nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here
directory = sys.argv[1]
os.makedirs(directory, exist_ok=True)
cache = os.listdir(directory)

while True:
    address = input().replace(".", "_")
    filename = address.split("_")[0]
    if filename in cache:
        with open(os.path.join(directory, filename), "r") as f:
            print(f.read())
    elif address in globals():
        content = globals()[address]
        print(content)
        with open(os.path.join(directory, filename), "w") as f:
            f.write(content)
        cache.append(filename)
    elif address == 'exit':
        break
    else:
        print("Error: Incorrect URL")
