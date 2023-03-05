"""
Generate gif of t-SNE results in a dirty way 
"""
import imageio
import os

images = []
pic_path = '/Users/anmin/Documents/Courses/2023Winter/cs_app_2/final-project-ecoview/figs/cluster/'
file_names = os.listdir(pic_path)

for filename in file_names:
    images.append(imageio.imread(os.path.join(pic_path, filename)))
imageio.mimsave('/Users/anmin/Documents/Courses/2023Winter/cs_app_2/final-project-ecoview/figs/cluster_gif/movie.gif', images)
