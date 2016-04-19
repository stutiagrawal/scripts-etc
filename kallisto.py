import os

if __name__=="__main__":
	f = open("nbl.aa.txt", "r")
	f.readline()
	key = "/home/ubuntu/cghub.key"
	for line in f:
		aa = line.rstrip()
		outdir = "/home/ubuntu/SCRATCH/"
		if not os.path.isdir(outdir):
			os.mkdir(outdir)
		os.system("s3cmd sync -r %s %s" %(os.path.join("s3://inrg_bam_cghub", aa), outdir))
		if os.path.isdir(os.path.join(outdir, aa)):
			os.chdir(os.path.join(outdir, aa))
			for fname in os.listdir(os.path.join(outdir, aa)):
				if fname.endswith("tar"):
					os.system("tar -xvf %s" %(os.path.join(outdir, aa, fname)))
			cmd = "kallisto quant -i /home/ubuntu/SCRATCH/kallisto.grch38.index -o %s --threads 12" %os.path.join("/home/ubuntu/SCRATCH/kallisto_results", aa)			
			for read in os.listdir(os.path.join(outdir, aa)):
				if read.endswith(".fastq.gz"):
					cmd += " %s" %os.path.join(outdir, aa, read)
			os.system(cmd)
			os.system("s3cmd sync %s s3://bioinformatics_scratch/kallisto/" %os.path.join("/home/ubuntu/SCRATCH/kallisto_results", aa))
			os.chdir(outdir)
			os.system("rm -rf %s" %os.path.join(outdir,aa))
