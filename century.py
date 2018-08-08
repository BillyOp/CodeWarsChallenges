from datetime import timedelta, date

def main():
    print(centuryFromYear(1))

def centuryFromYear(year):
    # first century from the year
    # 1 - 100 : 101 - 200
    # get year x | xx | xxx | xxxx
    if len(str(year)) == 1 or len(str(year)) == 2:
        return 1



if __name__=="__main__":
    main()
