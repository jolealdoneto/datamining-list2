m = [(0.5,4.5,2.5),
    (2.2,1.5,0.1),
    (3.9,3.5,1.1),
    (2.1,1.9,4.9),
    (0.5,3.2,1.2),
    (0.8,4.3,2.6),
    (2.7,1.1,3.1),
    (2.5,3.5,2.8),
    (2.8,3.9,1.5),
    (0.1,4.1,2.9)]

c1 = (0.5, 4.5, 2.5)
c2 = (2.5, 2, 1.5)

def distance(measurement, c):
    return sum(abs(mea-cl) for mea, cl in zip(measurement, c))

index = 1
points = { "c1":[], "c2": [] }
for measurement in m:
    d_c1 = distance(measurement, c1)
    d_c2 = distance(measurement, c2)
    if d_c1 < d_c2:
        print measurement, "c1", d_c1, d_c2, index
        points['c1'].append(measurement)
    else:
        print measurement, "c2", d_c1, d_c2, index
        points['c2'].append(measurement)
    index += 1

def calc_mean(points):
    return tuple(float(sum(t[i] for t in points))/len(points) for i in range(3))

def calc_variance(x1, x2, x1_mean, x2_mean):
    return float(sum((x-x1_mean)*(y-x2_mean) for x, y in zip(x1, x2))) / (len(x1)-1)

def get_points_from_index(i, points):
    return list(t[i] for t in points)
def calc_covariance_matrix(points, mean_vector):
    return list(calc_variance(get_points_from_index(i, points), get_points_from_index(j, points), mean_vector[i], mean_vector[j]) for i, j in reduce(lambda acc, a: acc+a, (zip([k]*3, range(3)) for k in range(3))))



print "====c1====="
print points['c1']
c1_mean = calc_mean(points['c1'])
print "(%.2f,%.2f,%.2f)" % c1_mean
print calc_covariance_matrix(points['c1'], c1_mean)
print "==========="
print "====c2====="
print points['c2']
print "(%.2f,%.2f,%.2f)" % calc_mean(points['c2'])
c2_mean = calc_mean(points['c2'])
print calc_covariance_matrix(points['c2'], c2_mean)
print "==========="
