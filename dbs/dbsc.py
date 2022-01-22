from sklearn.cluster import DBSCAN
import math

n = 450
dimens = 100
map = []
data = []

c0 = []

def centrer(arr):
    ans = [-1]
    n_arr = len(arr)
    for dimen in range(1, dimens+1):
        temp = 0
        for i in range(n_arr):
            temp += arr[i][dimen]
        ans.append(1.0*temp/n_arr)
    return ans


def eu_distance(point1):
    temp = 0
    for i in range(1, dimens + 1):
        temp += (point1[i] - c0[i]) ** 2
    return math.sqrt(temp)


def loadData():
    global n, dimens, map, data
    f = open("embeddings.txt", "r")
    fi = f.readline().split()
    dimens = int(fi[1])
    for _ in range(n):
        fi = f.readline().split()
        map.append(fi[0])
        temp = []
        for i in range(1, dimens+1):
            temp.append(float(fi[i]))
        data.append(temp)


def clustering():
    global n, dimens, map, data, c0
    cluster = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
    db = DBSCAN(eps=25.62, min_samples=3).fit(data)
    labels = db.labels_
    noise = 0
    for i in range(len(labels)):
        if labels[i] == -1:
            noise += 1
            continue
        temp = [i]
        temp.extend(data[i])
        cluster[labels[i]].append(temp)

    c0 = centrer(cluster[0])
    cluster[0].sort(key=eu_distance)

    print(map[cluster[0][0][0]]," ", map[cluster[0][1][0]], map[cluster[0][2][0]])
    print("Number of labels:", len(set(labels)) - 1)
    print("Ratio noise point:", 1.0*noise/n)



if __name__ == '__main__':
    loadData()
    # print(n)
    # print(dimens)
    # print(len(map))
    clustering()