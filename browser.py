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


class Browser:

    def __init__(self):
        self.directory = sys.argv[1]
        os.makedirs(self.directory, exist_ok=True)
        self.cache = os.listdir(self.directory)
        self.address = None
        self.filename = None
        self.stack = []

    def run(self):
        while True:
            self.address = input().replace(".", "_")
            self.filename = self.address.split("_")[0]

            if self.filename in self.cache:
                self.print()
                self.stack.append(self.filename)
            elif self.address in globals():
                content = globals()[self.address]
                print(content)
                self.save(content)
                self.stack.append(self.filename)
            elif self.address == "exit":
                break
            elif self.address == "back":
                if len(self.stack) >= 2:
                    self.stack.pop()
                    self.filename = self.stack.pop()
                    self.print()
            else:
                print("Error: Incorrect URL")

    def print(self):
        with open(os.path.join(self.directory, self.filename), "r") as f:
            print(f.read())

    def save(self, content):
        with open(os.path.join(self.directory, self.filename), "w") as f:
            f.write(content)


bw = Browser()
bw.run()
