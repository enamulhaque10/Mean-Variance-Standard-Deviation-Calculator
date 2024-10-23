import numpy as num

def calculate(data):
    if len(data) !=9:
        raise ValueError('List must contain nine numbers.')
    else:
        matrix = num.array(data).reshape(3,3)
        mean = [(matrix.mean(axis=0).tolist()),(matrix.mean(axis=1).tolist()), num.mean(data)]
        variance =[(matrix.var(axis=0).tolist()),(matrix.var(axis=1).tolist()),num.var(data)]
        deviation = [(matrix.std(axis=0).tolist()),(matrix.std(axis=1).tolist()),num.std(data)]
        max = [(matrix.max(axis=0).tolist()),(matrix.max(axis=1).tolist()),num.max(data)]
        min = [(matrix.min(axis=0).tolist()),(matrix.min(axis=1).tolist()),num.min(data)]
        sum = [(matrix.sum(axis=0).tolist()),(matrix.sum(axis=1).tolist()),num.sum(data)]

    return {
        'mean':mean,
        'variance':variance,
        'standard deviation':deviation,
        'max': max,
        'min':min,
        'sum':sum
    }