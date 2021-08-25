import argparse
import os 

parser = argparse.ArgumentParser(prog='exercise 2')
requiredName=parser.add_argument_group('required arguments')
requiredName.add_argument('-folder', '--folder', help='Folder of the script files', required=True)
args = parser.parse_args()

if __name__ == '__main__':
    folder = args.folder
    scripts= {}
    # for each file in folder
    for file in os.listdir(folder):
        # open file and read the first line
        with open(folder+file, encoding="utf8") as f:
            line=f.readline()
            # if key is already in dict, increment the value else set value to 1
            if line in scripts.keys():
                scripts[line]+=1
            else:
                scripts[line]=1
    # print the result 
    for el, value in scripts.items():
        print(f'{value} {el}')
