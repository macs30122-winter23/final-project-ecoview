!!! This is a temporary file subject to change. 

Hi, all!

As our data are mostly tabular and light weigted, we can gather them on GitHub. 

I construct the repository in the following structure:

- data

  - raw_data

    - subject_1 (for instance, air_quality)
    - subject_2 (for instance, bill)

    ...

  - clean_data

    - a concated tabel (master table) that aggregate all the data we use (.csv)
    - subject_1

    ... 

- figs

- scripts

  - preprocess (any script that contribute to raw_data, clean_data and the master table)
  - analysis (any operation on the master table)

- presentation



 

