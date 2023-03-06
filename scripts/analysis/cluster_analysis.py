"""
Dimension Reduction for all Features with t-SNE
serve as visualization and hypothesis test

hypothesis: states with the same political leaning may form in the same cluster

Dimension Reduction:
1. analysis by year (master for loop)
2. perlexity defines the outcome of t-SNE, here use gridserch for best possible result(secondary loop)
3. to resolve the randomness of t-SNE, with each perplexity, the process repeats 60 times(tertiary loop)
4. repeacted matrixed are averaged to a two dimensional matrix as the final representation

Plots:
5. scatterplot in two dimensional space, with color representing political category and
    hue representing intensity
6. add annotation of state name next to the scatter

@author Anmin Yang
"""
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns

from sklearn.manifold import TSNE
from sklearn.preprocessing import scale

root_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
df = pd.read_csv(os.path.join(root_path,
                    'data', 'clean_data',
                    'final_data_with_population.csv'))

#### main loop
years = [2018, 2019, 2020, 2021]
random_time = 60
perplexities = range(3,30,5)
for year in years:
    df_political = pd.read_csv(os.path.join(root_path,
                                            'data', 'clean_data',
                                            'political_leaning',
                                            'political_leaning_2018-2021.csv'))
    df_political = df_political[df_political['Year'] == year]
    y = df_political.score.to_numpy()

    # States
    states = df_political.State.to_list()


    df_temp = df[df['year'] == year]
    X = df_temp.to_numpy()[:,2:]
    X = scale(X)

    for perlexity in perplexities:
        for t in range(random_time):
            X_embedded_temp = TSNE(n_components=2, learning_rate='auto',
                                init='random', perplexity=perlexity).fit_transform(X)
            if t == 0:
                print(f'--------------{year}--------------')
                X_embedded = np.zeros(X_embedded_temp.shape)
            if t % 20 == 0:
                print(f'{t} is completed.')
            X_embedded = np.dstack((X_embedded, X_embedded_temp))

        X_embedded = X_embedded[:,:,1:]
        X_embedded = np.mean(X_embedded, axis=2)

        df_embedded = pd.DataFrame(np.column_stack((X_embedded,
                                                    y)),
                                columns=['X', 'Y', 'political leaning'])

        # set the center of the pallette at 0
        offset = mcolors.TwoSlopeNorm(vmin=np.min(y),
                                    vcenter=0., vmax=np.max(y))
        # main plot
        sns.scatterplot(data=df_embedded, x="X", y="Y", hue="political leaning",
                        palette="bwr_r",hue_norm=offset,
                        size='political leaning', sizes=(200,400))
        for i, state in enumerate(states):
            if df_political[df_political['State'] == state].score.values[0] > 0:
                plt.annotate(state,
                            xy=(X_embedded[i,0],
                                X_embedded[i,1]),
                            fontsize=5,
                            color='blue',
                            xytext=(X_embedded[i,0]+1,
                                    X_embedded[i,1]))
            else:
                plt.annotate(state,
                            xy=(X_embedded[i,0],
                                X_embedded[i,1]),
                            fontsize=5,
                            color='red',
                            xytext=(X_embedded[i,0]+1,
                                    X_embedded[i,1]))

        ax = plt.gca()
        ax.spines['top'].set_color('none')
        ax.spines['right'].set_color('none')

        plt.legend().remove()
        plt.title(f'{year}')
        #plt.xlim(-8,8)
        #plt.ylim(-8,8)

        plt.savefig(os.path.join(root_path, 'figs', 'cluster',
                                f'{year}_{perlexity}.png'),
                    dpi=400)
        plt.clf()
