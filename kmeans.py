from copy import deepcopy
from random import sample
 
def should_change(cur_centroid_dif, min_centroid_dif):
    cur_centroid = list(cur_centroid_dif.keys())[0]
    cur_dif = list(cur_centroid_dif.values())[0]
    min_centroid = list(min_centroid_dif.keys())[0]
    min_dif = list(min_centroid_dif.values())[0]
    
    if cur_dif == min_dif:
        return cur_centroid < min_centroid
    
    return cur_dif < min_dif
 
def get_closest_centroid(num, cur_centroids_clusters):
    min_centroid_dif = {0 : float('inf')}
    for c in cur_centroids_clusters.keys():
        cur_centroid_dif = {c : abs(c - num)}
        if should_change(cur_centroid_dif, min_centroid_dif):
            min_centroid_dif = cur_centroid_dif
    return list(min_centroid_dif.keys())[0] 
 
def termination_condition(cur_centroids_clusters, prev_centroids_clusters):
    return cur_centroids_clusters == prev_centroids_clusters
    
def init_centroids(data, k):
    sample_data = sample(data, k)
    samples = {}
    
    for i in sample_data:
        samples[i] = []
    
    return samples

def assign_values_to_centroids(data, cur_centroids_clusters):
    for num in data:
        closest_centroid = get_closest_centroid(num, cur_centroids_clusters)
        closest_centroid_vals = deepcopy(cur_centroids_clusters[closest_centroid])
        closest_centroid_vals.append(num)
        cur_centroids_clusters[closest_centroid] = closest_centroid_vals

def calc_new_centroids(cur_centroids_clusters):
    new_centroids_clusters = {}
    for c in cur_centroids_clusters:
        cur_vals = cur_centroids_clusters[c]
        new_centroid = sum(cur_vals) / len(cur_vals)
        new_centroids_clusters[new_centroid] = cur_vals
    
    return new_centroids_clusters

def kmeans(data, k):
    prev_centroids_clusters = init_centroids(data, k)
    cur_centroids_clusters = prev_centroids_clusters
       
    while True:
        assign_values_to_centroids(data, cur_centroids_clusters)
        
        for key, val in cur_centroids_clusters.items(): 
            print(round(key, 2), ':', val)
        print('\n')
        
        new_centroids_clusters = calc_new_centroids(cur_centroids_clusters)
        
        prev_centroids_clusters = cur_centroids_clusters
        if termination_condition(new_centroids_clusters, prev_centroids_clusters):
            cur_centroids_clusters = list(prev_centroids_clusters.keys())
            break
        else:
            cur_centroids_clusters = dict.fromkeys(new_centroids_clusters, [])
    
    return cur_centroids_clusters

if __name__ == '__main__':
    data = [1, 2, 3, 10, 20, 30, 40, 50]
    print(kmeans(data, 3))
