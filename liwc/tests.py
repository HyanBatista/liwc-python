from liwc.liwc import LIWC

def main():
    lwic = LIWC('data/LIWC2007_Portugues_win.dic')
    categories = lwic('parapeito')
    print(categories)
    for k, v in lwic.category_mapping.items():
        for c in categories:
            if c == v:
                print(k)

if __name__ == '__main__':
    main()