def sorting(li):
    for i in range(len(li)):
        for j in range(len(li)):
            if li[i] < li[j]:
                li[j],li[i] = li[i],li[j]
    return li

