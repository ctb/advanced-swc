
    x = 0
    for i in range(0, limit):
        x += i

    return x

def count2(limit=1500000):
    x = 0
    for i in range(0, limit):
        x += i

    return x

if __name__ == '__main__':
    print ''
    print '*** STATPROF output ***'
    print ''
    
    import statprof
    statprof.start()
    count1()
    count2()
    statprof.stop()
    statprof.display()

    print ''
    print '*** HOTSHOT output *** '
    print ''

    import hotshot, hotshot.stats
    prof = hotshot.Profile('profile1.prof')
    prof.runcall(count1)
    prof.runcall(count2)
    prof.close()

    stats = hotshot.stats.load('profile1.prof')
    stats.sort_stats('time', 'calls')
    stats.print_stats(20)
