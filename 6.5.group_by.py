from collections import defaultdict

def group_by(fun, iterable):

    group_dic = defaultdict(list)

    dic = {i: fun(i)for i in iterable}
    for key, val in dic.items():
        group_dic[val].append(key)
    return str(dict(group_dic))


