#code to create a coloured dendrogram of mtcars dataset
#originally taken from : https://rpubs.com/gaston/dendrograms

#number of clusters 
num_clusters = 4
# vector of colors
labelColors = c('red', 'blue', 'darkgreen', 'darkgrey')
d <- dist(as.matrix(mtcars))
hc <- hclust(d)

##########################################################################
hcd <- as.dendrogram(hc)

# cut dendrogram in 4 clusters
clusMember = cutree(hc, num_clusters)
# function to get color labels
colLab <- function(n) {
    if (is.leaf(n)) {
        a <- attributes(n)
        labCol <- labelColors[clusMember[which(names(clusMember) == a$label)]]
        attr(n, "nodePar") <- c(a$nodePar, lab.col = labCol)
    }
    n
}
# using dendrapply
clusDendro = dendrapply(hcd, colLab)
# make plot
plot(clusDendro, main = "mtcars")

###############################################################################

#if branches also need to be coloured
# load code of A2R function
source("http://addictedtor.free.fr/packages/A2R/lastVersion/R/code.R")
# colored dendrogram
op = par(bg = "white")
A2Rplot(hc, k = num_clusters, boxes = FALSE, col.up = "gray50", col.down = labelColors)
