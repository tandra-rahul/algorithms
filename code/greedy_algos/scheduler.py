def read_input(filename, delimiter):

    out_list = []
    with open(filename) as fp:
        for line in fp:
            x = line.rstrip("\n").split(delimiter)
            #print(x)
            if len(x) > 1:
                out_list.append( (float(x[0]), float(x[1])) )

    return out_list

# def greedy_scheduler(l):
#
#     l.sort(key=lambda tup: tup[0], reverse=True)
#     return l

def scheduler(l, metric_type):

    # Add greedy metric to list:
    al = augment_metric(l, metric_type)

    s = sorted(al, reverse=True)
    total_weight = compute_weighted_completion_time(s)
    return total_weight, s

def augment_metric(l, metric_type):

    out_list = []
    if metric_type == 'diff':
        for job in l:
            metric = job[0] - job[1]
            out_list.append( (metric, job[0], job[1]) )
    elif metric_type == 'ratio':
        for job in l:
            metric = job[0]/job[1]
            out_list.append( (metric, job[0], job[1]) )
    else:
        print("Error: unknown metric")

    return out_list



def compute_weighted_completion_time(s):

    total_weight = 0.0
    ctime = 0.0
    for ind,val in enumerate(s):
        ctime = ctime + val[2]
        total_weight = total_weight + val[1]*ctime
        #print("completion time of job:", ctime)
        #print("weighted score:", total_weight)

    return total_weight

def test_compute_weighted_completion_time():
    f = '/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/jobs2.txt'
    l = read_input(f," ")
    print("list of jobs:", l)
    print(compute_weighted_completion_time(l))

def test_read_input():

    f = '/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/jobs2.txt'
    l = read_input(f," ")
    print("list of jobs:", l)
    #g = greedy_scheduler(l)
    #print("optimal schedule:", g)

def test_scheduler():

    f = '/Users/rahul/Coursera/Algorithms/coursera_stanford/algorithms/inputs/jobs.txt'
    l = read_input(f," ")
    #print("list of jobs:", l)
    metric_type = 'diff'

    [score, schedule] = scheduler(l, metric_type)
    #print("Schedule:", schedule)
    print("final score:", score)

#def test_scheduler_diff():

if __name__ == '__main__':

    #test_read_input()
    #test_compute_weighted_completion_time()
    test_scheduler()
