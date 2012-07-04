from rpy import *

def plot_pca(filename):
    r("""data <- read.delim('%s', header=FALSE, sep=" ", nrows=5000)""" \
      % (filename,))

    r("""pca <- prcomp(data, scale=FALSE, center=FALSE)""")
    r("""pairs(pca$x[,1:3], pch=20)""")

plot_pca('vectors.txt')
