import numpy as np

all_rec_list = []
rec_list = []
results = np.load("results.npy", allow_pickle=True)
results = results.tolist()
idx_to_name = np.load("idx_to_name.npy", allow_pickle=True)
idx_to_name = idx_to_name.tolist()

# below is the input cocktail id list !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
input_item_list = [364, 392, 376]   # ['Martini', 'Orange Crush', 'Mojito']
rec_item_num = 20   # can change this

print(str(rec_item_num) + ' cocktails similar to ' + str(input_item_list) + ' are...')
for input_item in input_item_list:
    all_rec_list.append(results[input_item][:rec_item_num])

count_item = 0
lap = 0
while count_item < rec_item_num:
    for idx1, recs in enumerate(all_rec_list):
        if count_item >= rec_item_num:
            break
        rec = recs[lap]
        rec_list.append(rec)    # tuple(score, id)
        count_item += 1
        print('Recommended: ' + idx_to_name[int(rec[1])] + '  Score: ' + str(rec[0]))
    lap += 1

# below is the out cocktail (similarity, id) list !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
rec_list.sort(reverse=True)   # sort by high similarity
print(len(rec_list))
print(rec_list)