library('dplyr')
airports#install.packages("nycflights13")
library('nycflights13')
airports
airlines
flights
planes
weather
unique(weather$origin)
unique(airports$faa)
unique(airports$tzone)
airports_data <- as.data.frame(airports)
planes_data <- as.data.frame(planes)
airports_data
write.csv(airports_data,"/Users/edwu/Desktop/UCI/LexisNexis Interview Project/airports.csv", row.names = FALSE)
write.csv(planes_data,"/Users/edwu/Desktop/UCI/LexisNexis Interview Project/planes.csv", row.names = FALSE)
unique(weather$month)
unique(planes$speed)
