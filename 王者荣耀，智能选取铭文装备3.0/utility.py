#from equipment import*
#from rune import*

def cent(n):
    return n*0.01

def arm2dam(armor):
    return (1-armor/(600+armor))

def sumf(items, feature):
    if isinstance(items, list):
        return sum([eval("item."+feature) for item in items])

def sum_runes_f(d, feature):
    if isinstance(d, dict):
        #print([sumf(d[key],feature) for key in d])
        return sum([sumf(d[key],feature) for key in d])

def sum_equips_f(d,feature):
    if isinstance(d, dict):
        return sum([sumf(d[key],feature) for key in d])

def comb(l, n):
    result = []
    for i in l:
        result.append({i})
    n-=1
    if n == 0:
        return result
    else:
        while n != 0:
            n-=1
            new_result = []
            while result !=[] :
                k = result.pop()
                for i in l:
                    ele = k.copy()   
                    if not i in ele:
                        ele.add(i)
                        if not ele in new_result:
                            new_result.append(ele)
            result = new_result
        return result

def perm(l, n):
    result = []
    for i in l:
        result.append([i])
    n-=1
    if n == 0:
        return result
    else:
        while n != 0:
            n-=1
            new_result = []
            while result !=[] :
                k = result.pop()
                for i in l:
                    ele = k.copy()   
                    if not i in ele:
                        ele.append(i)
                        new_result.append(ele)
            result = new_result
        return result

def ave(l):
    return sum(l)/len(l)

if __name__ == "__main__":
    c = comb(useful, 3)
    for i in c:
        print(i)





















        
