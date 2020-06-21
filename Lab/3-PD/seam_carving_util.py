import numpy as np
import scipy.ndimage as nd

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

def norm(image):
    image += np.abs(image.min())
    return image*(1./image.max())

def top3(mat, point):
    assert len(mat.shape) == 2
    
    if point[0] == 0: return []
    if point[1] == 0: return np.array([mat[point[0]-1,point[1]], mat[point[0]-1,point[1]+1]])
    if point[1] == mat.shape[1]-1: return np.array([mat[point[0]-1,point[1]-1], mat[point[0]-1,point[1]]])
    return np.array([mat[point[0]-1,point[1]-1], mat[point[0]-1,point[1]], mat[point[0]-1,point[1]+1]])

def del_path(mat, path):
    if len(mat.shape) == 2: # This is a one dimensional matrix
        dim = [mat.shape[0], mat.shape[1]-1]
        ret = np.zeros(dim).astype('float')
    
        for i in path:
            ret[i[0],:i[1]] = mat[i[0],:i[1]]
            ret[i[0],i[1]:] = mat[i[0],i[1]+1:]
        return ret

    if len(mat.shape) == 3 and mat.shape[2] == 3: # This is a 3D matrix (RGB commonly)
        dim = [mat.shape[0], mat.shape[1]-1, mat.shape[2]]
        ret = np.zeros(dim).astype('float')
        
        
        for i in path:
            ret[i[0],:i[1], :] = mat[i[0],:i[1], :]
            ret[i[0],i[1]:, :] = mat[i[0],i[1]+1:, :]
        return ret

def min_at(arr, avoid=-1):
    assert len(arr.shape) == 1
    pos = 0
    mn = arr[0]
    for i in range(1, len(arr)):
        if (arr[i] < mn and arr[i] != avoid) or mn == avoid:
            mn = arr[i]
            pos = i
    return pos

'''
Colorea un camino (lista de píxeles) de rojo sobre una imagen.
'''
def mark_path(img, path):
    for i in path:
        img[i] = np.array([1,0,0])
    return img


