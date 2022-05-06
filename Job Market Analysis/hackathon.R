library(fpp3)
library(ggplot2)
library(gganimate)
#install.packages('gganimate')
#install.packages('gapminder')
library(gapminder)
dat <- read.csv("employment_backup.csv")
str(dat)
names(dat)
#ESTABS_ENTRY, ESTABS_EXIT, JOB_CREATION, JOB_DESTRUCTION
#
#  For ESTABS_ENTRY
#
dat1 <- dat[c('YEAR','ESTABS_ENTRY')]
str(dat1)


dat1 <- ts(dat1[,2], start = 1978, frequency = 1)

dat1_ts <- as_tsibble(dat1)


names(dat1_ts)[2] <- "ESTABS_ENTRY"


autoplot(dat1_ts)
ACF(dat1_ts, lag_max = 20)
autoplot(ACF(dat1_ts, lag_max = 20))
autoplot(PACF(dat1_ts, lag_max = 20))
features(dat1_ts, ESTABS_ENTRY, ljung_box, lag = 1, dof = 0)
#  The Box-Pierce or Ljung-Box test for autocorrelation
#  Ho:  Data are uncorrelated in time
#  Ha:  Data are correlated in time
#  "when p is low, reject null hypothesis"
# the ESTABS_ENTRY series don't have significant correlation with time.

fit_1 <- model(dat1_ts, ARIMA(ESTABS_ENTRY))
report(fit_1)
augment(fit_1)
aug_1 <- augment(fit_1)
aug_1$.resid
forc_1 <- forecast(fit_1,  h = '4 years' )
autoplot(forc_1, dat1_ts) + 
  labs(x = "Year", y = "Establish Added", title = "Establishment Entry 4 Year Prediction")
forc_1
#
#  For ESTABS_EXIT
#
dat2 <- dat[c('YEAR','ESTABS_EXIT')]
str(dat2)


dat2 <- ts(dat2[,2], start = 1978, frequency = 1)


dat2_ts <- as_tsibble(dat2)


names(dat2_ts)[2] <- "ESTABS_EXIT"


autoplot(dat2_ts)
ACF(dat2_ts, lag_max = 20)
autoplot(ACF(dat2_ts, lag_max = 20))
autoplot(PACF(dat2_ts, lag_max = 20))
features(dat2_ts, ESTABS_EXIT, ljung_box, lag = 1, dof = 0)
#  The Box-Pierce or Ljung-Box test for autocorrelation
#  Ho:  Data are uncorrelated in time
#  Ha:  Data are correlated in time
#  "when p is low, reject null hypothesis"
# the ESTABS_EXIT series don't have significant correlation with time.

fit_2 <- model(dat2_ts, ARIMA(ESTABS_EXIT))
report(fit_2)
augment(fit_2)
aug_2 <- augment(fit_2)
aug_2$.resid
forc_2 <- forecast(fit_2, h = '4 years')
autoplot(forc_2, dat2_ts) +
  labs(x = "Year", y = "Establishments Removed", title = " Establishment Exit 4 Year Prediction")

#
#  For JOB_CREATION
#
dat3 <- dat[c('YEAR','JOB_CREATION')]
str(dat3)


dat3 <- ts(dat3[,2], start = 1978, frequency = 1)


dat3_ts <- as_tsibble(dat3)


names(dat3_ts)[2] <- "JOB_CREATION"


autoplot(dat3_ts)
ACF(dat3_ts, lag_max = 20)
autoplot(ACF(dat3_ts, lag_max = 20))
autoplot(PACF(dat3_ts, lag_max = 20))
features(dat3_ts, JOB_CREATION, ljung_box, lag = 1, dof = 0)
#  The Box-Pierce or Ljung-Box test for autocorrelation
#  Ho:  Data are uncorrelated in time
#  Ha:  Data are correlated in time
#  "when p is low, reject null hypothesis"
# the JOB_CREATION series don't have significant correlation with time.

fit_3 <- model(dat3_ts, ARIMA(JOB_CREATION))
report(fit_3)
augment(fit_3)
aug_3 <- augment(fit_3)
aug_3$.resid
forc_3 <- forecast(fit_3, h = '4 years')
autoplot(forc_3, dat3_ts) +
  labs(x = "Year", y = "Jobs Created", title = "Job Creation 4 Year Prediction")



#
#  For JOB_DESTRUCTION
#
dat4 <- dat[c('YEAR','JOB_DESTRUCTION')]
str(dat4)


dat4 <- ts(dat4[,2], start = 1978, frequency = 1)


dat4_ts <- as_tsibble(dat4)


names(dat4_ts)[2] <- "JOB_DESTRUCTION"


autoplot(dat4_ts)
ACF(dat4_ts, lag_max = 20)
autoplot(ACF(dat4_ts, lag_max = 20))
autoplot(PACF(dat4_ts, lag_max = 20))
features(dat4_ts, JOB_DESTRUCTION, ljung_box, lag = 1, dof = 0)
#  The Box-Pierce or Ljung-Box test for autocorrelation
#  Ho:  Data are uncorrelated in time
#  Ha:  Data are correlated in time
#  "when p is low, reject null hypothesis"
# the JOB_DESTRUCTION series don't have significant correlation with time.

fit_4 <- model(dat4_ts, ARIMA(JOB_DESTRUCTION))
report(fit_4)
augment(fit_4)
aug_4 <- augment(fit_4)
aug_4$.resid
forc_4 <- forecast(fit_4, h = '4 years')
autoplot(forc_4, dat4_ts) +
  labs(x = "Year", y = "Jobs Removed", title = "Job Destruction 4 Year Prediction")


dat1_train_ts
dat1
#dat_plot <- dat[c('YEAR','ESTABS_ENTRY','ESTABS_EXIT', 'JOB_CREATION', 'JOB_DESTRUCTION')]

library("tidyverse")
dat1_plot <- dat[c('YEAR','ESTABS_ENTRY','ESTABS_EXIT')]
str(dat1_plot)
df1 <- dat1_plot %>%
  select(YEAR, ESTABS_ENTRY, ESTABS_EXIT) %>%
  gather(key = "Legend", value = "value", -YEAR)

str(df1)

p1 <- ggplot(df1, aes(x = YEAR, y = value)) + 
  geom_line(aes(color = Legend)) + 
  scale_color_manual(values = c("black", "royalblue1"))+
  labs(x = "Year", y = "Number of Establishments", title = "ESTABS_ENTRY vs ESTABS_EXIT")
p1
p1 + 
  transition_reveal(YEAR)

################
dat2_plot <- dat[c('YEAR','JOB_CREATION','JOB_DESTRUCTION')]
str(dat2_plot)
df2 <- dat2_plot %>%
  select(YEAR, JOB_CREATION, JOB_DESTRUCTION) %>%
  gather(key = "Legend", value = "value", -YEAR)



p2 <- ggplot(df2, aes(x = YEAR, y = value)) + 
  geom_line(aes(color = Legend)) + 
  scale_color_manual(values = c("black", "royalblue1"))+
  labs(x = "Year", y = "Number of Jobs", title = "JOB_CREATION vs JOB_DESTRUCTION")
p2
p2 + 
  transition_reveal(YEAR)

library(corrplot)
str(dat)

corrplot(cor(dat[,6:29]),method = 'number')
