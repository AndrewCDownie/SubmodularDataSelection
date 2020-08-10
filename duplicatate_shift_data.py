
import pandas as pd
import random
from names import names
stories = pd.read_csv("/Users/andrewdownie/Documents/Graduate Studies/Courses/CS680/Project/Datasets/2018/cloze_test_val__spring2016 - cloze_test_ALL_val.csv")
print(stories)
print(stories.columns)
cols = ['InputSentence1', 'InputSentence2', 'InputSentence3',
       'InputSentence4', 'RandomFifthSentenceQuiz1',
       'RandomFifthSentenceQuiz2']


precentage = 0.01
repeat = 100
n_samples = len(stories)
sample_points = random.sample(list(range(n_samples)),int(precentage*n_samples))
print(len( stories))
new_stories = stories.copy()
for i in range(repeat):
    new_stories = pd.concat([new_stories,stories.iloc[sample_points,:]],ignore_index=True)

#ew_stories = pd.concat([stories,stories.iloc[sample_points,:]],ignore_index=True)
print(len(new_stories))
new_stories.to_csv("redundant_data_set_1_100.csv")
