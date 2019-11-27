import openpyxl as op
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# open excel file
wb = op.load_workbook('C:\\Users\\Michael\\Desktop\\All_cocktails.xlsx')

# get sheet
ws = wb['시트1']
desc_dict = {}
idx_to_name = []
name_to_idx = {}
global description
desc_list = []
idx_list = []

count = 0
for r in ws.rows:
    if count >= 1:
        row_idx = int(r[0].value)
        cocktail_name = str(r[1].value)
        description = str(r[2].value)
        for i in range(3, 17):  # until instruction
            if r[i].value is not None:
                description += ', '
                description += str(r[i].value)
            else:
                description += '.'
                break
        idx_to_name.append(cocktail_name)
        name_to_idx[cocktail_name] = row_idx
        desc_dict[cocktail_name] = description
        desc_list.append(description)
        idx_list.append(row_idx)
        # print(row_idx, cocktail_name, description)
    count += 1

# this steps generates word counts for the words in your docs

# print(desc_list)
tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(desc_list)
# print(tfidf_matrix)

cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
results = {}
for idx, row in enumerate(desc_list):
    similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
    similar_items = [(cosine_similarities[idx][i], idx_list[i]) for i in similar_indices]
    results[idx] = similar_items[1:]

np.save("results", results)
np.save("idx_to_name", idx_to_name)
