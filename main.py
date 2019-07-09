import time

def main():
  n = 0
  while True:
    time.sleep(2)
    file = open("file-%d.txt" % n, "w")
    file.write("Hello")
    file.close()
    n += 1

if __name__ == '__main__':
  main()
