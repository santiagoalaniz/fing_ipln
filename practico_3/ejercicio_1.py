import numpy as np

corpus = {
  'd1': ['Nacional', 'Internacional'],
  'd2': ['Deportes', 'Internacional'],
  'd3': ['Nacional', 'Nacional'],
  'd4': ['Deportes', 'Nacional'],
  'd5': ['Deportes', 'Deportes'],
  'd6': ['Deportes', 'Deportes'],
  'd7': ['Deportes', 'Nacional'],
  'd8': ['Internacional', 'Internacional'],
  'd9': ['Internacional', 'Deportes'],
  'd10': ['Internacional', 'Deportes'],
  'd11': ['Deportes', 'Deportes'],
  'd12': ['Nacional', 'Nacional'],
  'd13': ['Deportes', 'Deportes'],
  'd14': ['Deportes', 'Deportes'],
  'd15': ['Internacional', 'Nacional'],
  'd16': ['Internacional', 'Nacional'],
  'd17': ['Internacional', 'Internacional'],
  'd18': ['Internacional', 'Internacional'],
  'd19': ['Internacional', 'Internacional'],
  'd20': ['Deportes', 'Nacional']
}

categories = {'Nacional': 0, 'Internacional': 1, 'Deportes': 2}

confussion_matrix = np.zeros((len(categories), len(categories)))

def set_confussion_matrix():
  for doc in corpus:
    confussion_matrix[categories[corpus[doc][0]], categories[corpus[doc][1]]] += 1
  return confussion_matrix

def accuracy():
  return np.trace(confussion_matrix) / np.sum(confussion_matrix)

def metrics():
  TP_ = {
    'Nacional': confussion_matrix[0][0],
    'Internacional': confussion_matrix[1][1],
    'Deportes': confussion_matrix[2][2]
  }
  TP = sum(TP_.values())

  TN_ = {
    'Nacional': np.sum(confussion_matrix) - TP_['Nacional'],
    'Internacional': np.sum(confussion_matrix) - TP_['Internacional'],
    'Deportes': np.sum(confussion_matrix) - TP_['Deportes']
  }
  TN = sum(TN_.values())

  FP_ = {
    'Nacional': np.sum(confussion_matrix, axis=0)[0] - TP_['Nacional'],
    'Internacional': np.sum(confussion_matrix, axis=0)[1] - TP_['Internacional'],
    'Deportes': np.sum(confussion_matrix, axis=0)[2] - TP_['Deportes']
  }
  FP = sum(FP_.values())

  FN_ = {
    'Nacional': np.sum(confussion_matrix, axis=1)[0] - TP_['Nacional'],
    'Internacional': np.sum(confussion_matrix, axis=1)[1] - TP_['Internacional'],
    'Deportes': np.sum(confussion_matrix, axis=1)[2] - TP_['Deportes']
  }
  FN = sum(FN_.values())

  precission = TP / (TP + FP)
  recall = TP / (TP + FN)
  f_score = 2 * (precission * recall) / (precission + recall)

  print(TP_)
  print(TN_)
  print(FP_)
  print(FN_)

  return f"TN={TN}, FP={FP}, FN={FN}, TP={TP}, precission={precission}, recall={recall}, f_score={f_score}"




def main():
  # parte a)
  print(f"confussion matrix =")
  print(set_confussion_matrix())
  # parte b)
  print(f"accuracy:{accuracy()}")
  # parte c)
  print(f"metrics: {metrics()}")

if __name__ == '__main__':
  main()
