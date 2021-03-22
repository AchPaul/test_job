def appearance(intervals):
    puptime = []
    tuttime = []
    pp = 0
    tp = 0
    for key in intervals:
        if key == 'pupil':
            flug = True
            for i in intervals[key]:
                puptime.append(i)
        if key == 'tutor':
            for i in intervals[key]:
                tuttime.append(i)
    puptime.reverse()
    tuttime.reverse()
    pup = 0
    tut = 0
    flug = True
    for i in puptime:
        if flug:
            pup += i
        else:
            pup -= i
        flug = not flug
    for i in tuttime:
        if flug:
            tut += i
        else:
            tut -= i
        flug = not flug


    print(pup)
    print(tut)


l = {'lesson': [1594663200, 1594666800],
     'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
     'tutor': [1594663290, 1594663430, 1594663443, 1594666473]}
appearance(l)
