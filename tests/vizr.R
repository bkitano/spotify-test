library(readr)
rhythm <- read_csv("~/Desktop/rhythm.csv", 
                   col_names = FALSE)

waveform <- read_csv("~/Desktop/waveform.csv", 
                   col_names = FALSE)

M <- matrix(waveform[2,])

# Fs Nch <Nzs Zi dz_1 ... dz_Nzs>_1 ... <Nzs Zi dz_1 ... dz_Nzs>_Nch

# Fs: sampling rate (currently 22050)
# Nch: number of chunks (currently 3)
# Nzs: number of zero crossings
# Zi: a zero crossing reference
# dz_n: number of samples to the next zero crossing

Fs <- M[[1]] # the sampling rate (currently 22100)
Nch <- M[[2]] # the number of chunks (currently 3)

size <- length(M) - 2

t <- c(1:size)
y <- M[3:length(M)]

Nzs <- y[1]
Zi <- y[2]
# View(y)

t1_length <- y[[1]]
t1 <- 1:t1_length
chunk_1 <- y[t1]
  
plot(t1[-1], chunk_1[-1])

t2_length <- y[[t1_length + 2]]
t2 <- (t1_length + 3):t2_length
chunk_2 <- y[t2]

plot(t2[-1], chunk_2[-1])

t3_length <- y[[t2_length ]]
t3 <- (t3_length + 3):length(y)
chunk_3 <- y[t3]

plot(t3[-1], chunk_3[-1])



# the local highs there are the Number of Onsets, of which there are 8
# there are 8 channels
# The next element is the initial onset frame, and then idk what the rest is
# technically the number of frames until the next onset