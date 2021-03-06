import matplotlib.pyplot as plt

for i in df.columns:
    fig, ax = plt.subplots(figsize = (15, 10))
    plt.hist(df[i], alpha = 0.3) 
    plt.title(i)
    plt.show()
    plt.close()
