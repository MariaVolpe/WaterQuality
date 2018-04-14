from internal import process
from internal import calculate

def main():
    load_obj = process.ProcessFile()
    #load_obj.load_bacteria()
    #load_obj.load_sites()
    obj = calculate.Calculations()

if __name__ == "__main__":
    main()