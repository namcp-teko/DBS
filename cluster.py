from collections import defaultdict

from scipy.spatial.distance import cosine
from spherecluster import SphericalKMeans
from code.dataset import SubDataSet
from sklearn.cluster import DBSCAN

class Clusterer:

    def __init__(self, data, n_cluster):
        self.data = data
        self.n_cluster = n_cluster
        self.clus = DBSCAN(eps=20, min_samples=3)#SphericalKMeans(n_cluster)
        self.clusters = defaultdict(list)  # cluster id -> members
        self.membership = None  # a list contain the membership of the data points
        self.center_ids = None  # a list contain the ids of the cluster centers
        self.inertia_scores = None

    def fit(self):
        print("Start fit cluster")
        self.clus.fit(self.data)
        labels = self.clus.labels_
        n = len(list(labels))
        noise = 0
        for i in range(0, n-1):
            if labels[i] == -1:
                noise += 1

        print(1.0*noise/n)
        # print(self.clus.labels_)
        print(labels[10])
        print(len(set(labels)))
        for idx, label in enumerate(labels):
            self.clusters[label].append(idx)
        self.membership = labels
        self.center_ids = self.gen_center_idx()
        self.inertia_scores = self.clus.inertia_
        print('Clustering concentration score:', self.inertia_scores)

    # find the idx of each cluster center
    def gen_center_idx(self):
        ret = []
        for cluster_id in range(self.n_cluster):
            center_idx = self.find_center_idx_for_one_cluster(cluster_id)
            ret.append((cluster_id, center_idx))
        return ret


    def find_center_idx_for_one_cluster(self, cluster_id):
        query_vec = self.clus.cluster_centers_[cluster_id]
        members = self.clusters[cluster_id]
        best_similarity, ret = -1, -1
        for member_idx in members:
            member_vec = self.data[member_idx]
            cosine_sim = self.calc_cosine(query_vec, member_vec)
            if cosine_sim > best_similarity:
                best_similarity = cosine_sim
                ret = member_idx
        return ret

    def calc_cosine(self, vec_a, vec_b):
        return 1 - cosine(vec_a, vec_b)


def run_clustering(full_data, doc_id_file, filter_keyword_file, n_cluster, parent_direcotry, parent_description, cluster_keyword_file, hierarchy_file, doc_membership_file):
    print("Start run")
    dataset = SubDataSet(full_data, doc_id_file, filter_keyword_file)
    print('Start clustering for ', len(dataset.keywords), ' keywords under parent:', parent_description)
    clus = Clusterer(dataset.embeddings, n_cluster)
    print(clus.clus)
    clus.fit()
    print('Done clustering for ', len(dataset.keywords), ' keywords under parent:', parent_description)
    dataset.write_cluster_members(clus, cluster_keyword_file, parent_direcotry)
    center_names = dataset.write_cluster_centers(clus, parent_description, hierarchy_file)
    dataset.write_document_membership(clus, doc_membership_file, parent_direcotry)
    print('Done saving cluster results for ', len(dataset.keywords), ' keywords under parent:', parent_description)
    return center_names
