fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16,6))

sns.regplot(x="x", y="y", data=df, fit_reg=False, ax=ax1, color='steelblue', scatter_kws={'alpha':0.2})

idx = (df_form.x < 80) & (df_form.y < 80)
sns.regplot(x="x", y="y", data=df[idx], fit_reg=False, ax=ax2, color='steelblue', scatter_kws={'alpha':0.2})
