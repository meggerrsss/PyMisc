# for viewing old posts a la timehop

import datetime

tod = datetime.datetime.today()

yr = tod.year
mn = tod.month
dy = tod.day

tumblrurl = "calmandcalculating"

dailyurl = 'http://{0}.tumblr.com/day/{1}/{2}/{3}'.format(tumblrurl, str(yr-1), str(mn), str(dy) )

