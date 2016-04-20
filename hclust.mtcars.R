#code to make coloured heirarchical clustering for the mtcars dataset.
#reference: https://rpubs.com/gaston/dendrograms. This link is the original source for the following code, which is basically the same code.

d <- dist(as.matrix(mtcars))
hc <- hclust(d)
hcd <- as.dendrogram(hc)
# vector of colors labelColors = c('red', 'blue', 'darkgreen', 'darkgrey',
# 'purple')
labelColors = c("#CDB380", "#036564", "#EB6841", "#EDC951")
# cut dendrogram in 4 clusters
clusMember = cutree(hc, 4)
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
