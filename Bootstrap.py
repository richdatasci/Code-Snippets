boot_mean_diff = []
for i in range(3000):
    boot_before = before_someval.sample(frac=1, replace=True)
    boot_after = after_propsomeval.sample(frac=1, replace=True)
    boot_mean_diff.append( boot_after.mean() - boot_before.mean() )

# Calculating a 95% confidence interval from boot_mean_diff 
confidence_interval = pd.Series(boot_mean_diff).quantile([0.025, 0.975])
confidence_interval
