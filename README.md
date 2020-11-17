This module is used to get metrics of Machine Learning/Deep Learning Models.It consists of all sklearn.metrics and stats module methods.Using this module you can also use all all different distances obtained in metrics.pairwise.cosine_distance etc.

from sklearning.metrics import *

y_test = [0,1,2,3,4]

y_pred = [0,1,2,3,5]

#Root Mean Squared Error

rmse = rootMeanSquaredError(y_test,y_pred)

print(rmse)

o/p:0.4472135954999579



#Regressor Summary

summary = regressorSummary(y_test,y_pred)

print(summary)

o/p:

<class 'statsmodels.iolib.summary.Summary'>
"""
                                 OLS Regression Results                                
=======================================================================================
Dep. Variable:                      y   R-squared (uncentered):                   0.988
Model:                            OLS   Adj. R-squared (uncentered):              0.985
Method:                 Least Squares   F-statistic:                              330.3
Date:                Tue, 17 Nov 2020   Prob (F-statistic):                    5.39e-05
Time:                        21:56:13   Log-Likelihood:                         -1.1657
No. Observations:                   5   AIC:                                      4.331
Df Residuals:                       4   BIC:                                      3.941
Df Model:                           1                                                  
Covariance Type:            nonrobust                                                  
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
x1             1.1333      0.062     18.174      0.000       0.960       1.306
==============================================================================
Omnibus:                          nan   Durbin-Watson:                   1.724
Prob(Omnibus):                    nan   Jarque-Bera (JB):                0.615
Skew:                           0.805   Prob(JB):                        0.735
Kurtosis:                       2.402   Cond. No.                         1.00
==============================================================================

#Stats Value

statsValue(y_test,y_pred)

o/p:

statsValue(y_test,y_pred)
pvalues
 [0.53047777 0.00190127]
tvalues
 [-0.70710678 10.39230485]
rsquared
 0.972972972972973
rsquared_adj
 0.963963963963964