from lib import routine

def main():
    mr = routine.Routine('./save.txt')
    mr.save()
    mr.search('i')
    mr.show()

if __name__ == '__main__':
    main()
