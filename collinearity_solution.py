x_nocollinearity = predictors.drop(['dewtemp_F','wind_mph','wind_dir','windgust_dir','SOLIN_Wm2','prec_occur'],axis=1)

x_train_bal, y_train_bal, x_test_bal, y_test_bal = dataprep_pipeline(x_nocollinearity, y, verbose=False)

# Using the same Random Forest classifier as above, just changing the training data.
forest_nocollinearity = RandomForestClassifier(n_estimators=10, max_depth=2);
forest_nocollinearity.fit(x_train_bal, y_train_bal);

# Compare to training predictions to assess overfitting
print("Training data metrics:")
pred_train= forest_nocollinearity.predict(x_train_bal)
bin_metrics(y_train_bal,pred_train);

# Use testing data and test predictions to calculate metrics
print(" ")
print("Testing data metrics:")
pred_test= forest_nocollinearity.predict(x_test_bal)
bin_metrics(y_test_bal, pred_test)
plot_cm(y_test_bal, pred_test)

# Re-assess feature importance
pd.DataFrame(forest_nocollinearity.feature_importances_,
           index = x_nocollinearity.columns, 
           columns=['importance']).sort_values('importance', ascending=False)