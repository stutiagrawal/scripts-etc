import argparse
import os

def is_mutation(filename):
    f = open(filename, "r")
    header = f.readline()
    mutation_count = [0]*24
    for line in f:
        line = line.split("\t")
        chromosome = line[1]
        seg_mean = line[5]
        if float(seg_mean) < -0.1 or float(seg_mean) > 0.1:
            if chromosome == "X" or chromosome == "x":
                position = 22
            elif chromosome == "Y" or chromosome == "y":
                position = 23
            else:
                position = int(chromosome) - 1
            mutation_count[position] = 1
    return(sum(mutation_count))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mutation count")
    parser.add_argument("--dirname", default=None, help="path to directory conatining seg files")
    parser.add_argument("--filename", default=None, help="path to seg file")

    args = parser.parse_args()

    if not args.filename == None:
        if not os.path.isfile(args.filename):
            raise Exception("Cannot find file: %s" %args.filename)
        print "%s\t%s" %(args.filename, is_mutation(args.filename))

    if not args.dirname == None:
        if not os.path.isdir(args.dirname):
            raise Exception("Cannot find directory: %s" %args.dirname)
        for filename in os.listdir(args.dirname):
            filename = os.path.join(args.dirname, filename)
            print "%s\t%s" %(filename, is_mutation(filename))
