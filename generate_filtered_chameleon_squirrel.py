import numpy as np
import pandas as pd

def generate_raws_splits_from_npz(input_name, return_name):
  data = np.load(input_name)
  split_path = "./splits/"
  raw_path = "./datasets/" + return_name + '/raw/'

  for i in range(10):

    train, val, test = data['train_masks'][i,:], data['val_masks'][i,:], data['test_masks'][i,:]

    split_name = return_name+'_split_0.6_0.2_' + str(i)

    a,b,c = np.count_nonzero(train), np.count_nonzero(val), np.count_nonzero(test)
    print(a,b,c, a+b+c)

    np.savez_compressed(split_path+split_name
                                    , train_mask = train,
                                      val_mask = val,
                                      test_mask = test)

  edges = data['edges']
  edges_df = pd.DataFrame(edges, columns= ['node_id', 'node_id'])
  edges_df.to_csv(raw_path+'out1_graph_edges.txt', sep = '\t', index = False
                  , compression = None)

  N = data['node_features'].shape[0]

  nodes = np.arange(N)
  features = data['node_features'].astype(int)
  features = [", ".join(map(str, features[i,:])) for i in range(N)]

  labels = data['node_labels']


  node_feature_label = {'node_id' : nodes, 'feature' : features, 'label' : labels}
  nfl_df = pd.DataFrame(node_feature_label)
  nfl_df.to_csv(raw_path+'out1_node_feature_label.txt', sep = '\t', index = False)

  return None

generate_raws_splits_from_npz('./datasets/chameleon_filtered.npz', 'chameleon')
generate_raws_splits_from_npz('./datasets/squirrel_filtered.npz', 'squirrel')
