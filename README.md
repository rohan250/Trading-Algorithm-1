# Trading-Algorithm-1
# Using XGBoost Regressor algorithm to program a trading strategy 
 # Training the AI on data on various technical indicators about 30 coarse equities to build a predictor for time series data on 30 fine equities  

# The data will be split into two sets where 70% of the data will be used to train the program and the remaining 30% will be used to test the strength of the prediction algorithm 
# The technical indicators used to code the algorithm are: 
#1: Relative Strength Index (RSI) 
#2: Average True Range (ATR) 
#3: Average Directional Index (ADX) 
#4: Market Percentage Change (MPC)

# The program can be trained on only one of these indicators, but that increases the chances of false or faulty signals being used to generate predictions. By using a range of indicators, as I will do here, I can ensure that the program incorporates numerous facets to calculate stock strength and value. 
# Here, the tradeoff is efficiency versus accuracy: using a number of signals to generate predictions means that it will take longer to train the program, but we should find a corresponding increase in prediction accuracy to compensate for the efficiency loss. 
# The use of a relatively large sample size (30% of the total dataset) to test prediction accuracy will allow us to test whether the increase in accuracy is indeed sufficient to compensate for the efficiency loss. 
