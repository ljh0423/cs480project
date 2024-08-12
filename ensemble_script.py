output_col_test = ['X4', 'X11', 'X18', 'X26', 'X50', 'X3112']

#  weights for ensembling model outputs
weightm1 = 0.40
weightm2 = 0.60

pred1 = pd.read_csv('submissionm1.csv').values
pred2 = pd.read_csv('submissionm2.csv').values

newdf = pred1.copy()

# Compute the weighted average of two models
for i in range(1,7):
    newdf[:,i] =  pred1[:,i] * weightm1 + pred2[:,i] * weightm2

newdf = pd.DataFrame(newdf, columns=['id']+ output_col_test)
newdf['id'] = newdf['id'].astype(int)
newdf.to_csv('submission.csv', index=False)