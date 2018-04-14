from internal import process
from internal import calculate

def main():
    load_obj = process.ProcessFile()
    #load_obj.load_bacteria()
    #load_obj.load_sites()
    obj = calculate.Calculations()
    # obj.generate_line_graph()
    # obj.generate_bar_graph()
    print("Enter a site name to get average data: ")
    s = input()
    print (obj.site(s, "W") )
    print (obj.site(s, "D") )

if __name__ == "__main__":
    main()