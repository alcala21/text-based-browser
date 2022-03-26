import os
import sys
import requests


class Browser:

    def __init__(self):
        self.directory = sys.argv[1]
        os.makedirs(self.directory, exist_ok=True)
        self.cache = os.listdir(self.directory)
        self.filename = None
        self.stack = []

    def run(self):
        while True:
            value = input()

            if value == "exit":
                break

            if value == "back":
                if len(self.stack) >= 2:
                    self.stack.pop()
                    self.filename = self.stack.pop()
                else:
                    continue
            else:
                self.filename = value

            if self.filename in self.cache:
                self.print()
                self.stack.append(self.filename)
                continue

            try:
                page = requests.get("http://" + self.filename)
                if page.status_code == 200:
                    self.print_and_save(page.text)
                    self.stack.append(self.filename)
                else:
                    raise requests.exceptions.ConnectionError
            except requests.exceptions.ConnectionError:
                print("Error: Incorrect URL")

    def print(self):
        with open(os.path.join(self.directory, self.filename), "r", encoding='UTF-8') as f:
            print(f.read())

    def print_and_save(self, content):
        print(content)
        with open(os.path.join(self.directory, self.filename), "w", encoding='UTF-8') as f:
            f.write(content)
        self.cache.append(self.filename)


bw = Browser()
bw.run()
