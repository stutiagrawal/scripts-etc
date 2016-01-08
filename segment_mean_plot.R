#Compute the graph of the segment means for a patient.
setwd("/Users/stuti/Data/NBL/cnv")
#read in the data file. This file has headers and it is tab separated.
data <- read.table("TARGET-30-PAISNS.txt", header=T, sep="\t")
#Check the contents of the file using the head command.
head(data)
#Select the rows which correspond to chromosome 1
w <- which(data$Chromosome == 1)
#Subset the table on those rows, i.e. select all the columns for those rows.
d <- data[w,]
#Define two new numeric vectors
x <- numeric()
y <- numeric()
#Read in all the data in these two vectors
for(i in 1:nrow(d)){
    x <- c(x, d$Start[i], d$End[i])
    y <- c(y, d$Segment.Mean[i], d$Segment.Mean[i])
}
#Plot these points
plot(x, y)
#draw segments from point to point
s <- seq(length(x) - 1) #one less than the data
s <- s[-length(s)] #drop the last column
segments(x[s], y[s], x[s+2], y[s+2], col="pink")

