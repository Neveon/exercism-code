def recite(start_verse, end_verse):
    days = ('first', 'second', 'third', 'fourth', 'fifth', 'sixth',
            'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth')
    gifts = ["twelve Drummers Drumming, ",
             "eleven Pipers Piping, ",
             "ten Lords-a-Leaping, ",
             "nine Ladies Dancing, ",
             "eight Maids-a-Milking, ",
             "seven Swans-a-Swimming, ",
             "six Geese-a-Laying, ",
             "five Gold Rings, ",
             "four Calling Birds, ",
             "three French Hens, ",
             "two Turtle Doves, ",
             "and a Partridge in a Pear Tree."]
    ans = []
    for verse in range(start_verse-1, end_verse):
        tmp = []
        verse_line = ['On the ' + days[verse] + ' day of Christmas my true love gave to me: ']
        if verse == 0:
            ans.extend(verse_line)
            ans[0] += ('a Partridge in a Pear Tree.')
        else:
            tmp.extend(verse_line)
            tmp[0] += (''.join(map(str, gifts[12-(verse + 1):])))
            ans.extend(tmp)

    return ans
