import os

def aggregate(folder):
    fname = os.path.join(folder, "abundance.tsv")
    f = open(fname, "r")
    f.readline()
    aggr = dict()
    for line in f:
        line = line.split()
        ids = line[0].split("|")
        iso = ids[0]
        gene = ids[1]
        if gene not in aggr:
            aggr[gene] = list()
        aggr[gene].append(float(line[4]))
    outname = os.path.join(folder, "abundance.gene.tsv")
    out = open(outname, "w")
    out.write("target_id\test_count\n")
    for gene in aggr:
        out.write("%s\t%s\n" %(gene, sum(aggr[gene])/len(aggr[gene])))

if __name__ == "__main__":
    for f in os.listdir("/home/ubuntu/SCRATCH/kallisto_results/"):
        print f
        f = os.path.join("/home/ubuntu/SCRATCH/kallisto_results/", f)
        aggregate(f)


