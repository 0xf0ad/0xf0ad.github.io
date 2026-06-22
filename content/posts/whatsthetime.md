+++
title = "estimating time with using temperature"
description = "its hot, it must be the noon, or does it ????"
date = 2026-06-22

[taxonomies]
tags = ['science', 'physics', 'modeling']

+++

In the previous post / blog, we estimated how much radiation
the earth gets from the sun, now to exploit that idea to estimate
time of the day based on the temperature which is directly affected
by the solar radiation among other things.

First, we should note that we are aiming here to calculate time of
the day, based on the solar day, which is different than the
time of the day based on the local timezone, the later is a discretized
approximation of the former, and is based not just by the sun, but also
politics, religious activities that shifts the biological day of the
population, economic blocks that prefer to be syncronised, etc...

Second, you may notice that we mesure solar radiation throu
temperature, which are not the same, the only actual major difference
is the temporal shift due to termal inirtial, meaning the earth need
some time to catch heat, and similarly to dispose of it, it also may
varie depending on the region, other factors like clouds and winds
are with the margin of error.

To acomodate for the thermal inirtia and the difference between solar
clock and the local timezone, the user should input a correction term
which we call 'lag' correspounding to the time on which the temperature
is at its maximum, thats the solar noon, a lag of 0 implies that the
hotest time of the day is at 12h00.

We fetch some real world weather temperature from a wether API, I use
open meteo, here a command to fetch Casablanca's previous day
temperature data as a JSON:
```bash
curl "https://api.open-meteo.com/v1/forecast?latitude=33.5883&longitude=-7.6114&minutely_15=temperature_2m&timezone=Europe%2FLondon&past_days=1&forecast_days=0"
```
the data comes as a neet python formated array, so I wouldn't be
bothered by using the officiel library, a simple copy paste into
a file in sufficient, there should be a command to do that more
effiently using piping, but again its a one time thing.

Now a corolation function sweeping over our signal (or record)
against the theoritical sample to determine which is the most
probable to be the one represented in the sample, the parametres
here are such 'r' is the real world data, 't' is the theoritical
analysis data.

```python
def correlate(r, t):
    out = []
    for start in range(len(t)):
        out += [sum(r[i] * t[(start + i) % len(t)] for i in range(len(r)))]
    return out
```

the data should first be normalised.

```python
def norm(x):
    n = len(x)
    mean = sum(x) / n
    var = sum((v - mean) ** 2 for v in x) / n
    std = var ** (1/2)
    return [(v - mean) / std for v in x]
```

the lag and the latitude are specified by the user to fit local
clock, I emulated incremental recording of a sensor as it adds
samples as it runs, by choping the real data and mesuring the
error and the confedance afterward.

the lag is mesured by taking the diference between local 12h00
and the time when the temperature is at maximum in hours - the
difference - and multiplying it by 4 as the open-meteo provides
samples mesured every 15 minutes. the standart latatude should
be subtracted from 90 as in the code the 90 deg north pole
correspond to latetude of 0 deg.

```python
lat = 90 - 34
lag = 17
error = []
confedance = []

for i in range(2, len(rtemp)):
    corr = correlate(norm(rtemp[:i]), norm(ttemp[lat]))
    nowisthetime = max(range(len(corr)), key=lambda k: corr[k])
    last_sample_index = nowisthetime + len(a) - 1
    error += [(last_sample_index-i+lag)%96]
    confedance += [corr[nowisthetime]]
```

and of course a vibe coded function to nicely print tamestamps
as a clock:

```python
def time_str(n):
    h, m = divmod(15*n, 60)
    return f"{h%24:02d}:{m:02d}"
```

here are the results:

overlay the real world data as shifted by the resulted beggening time:
![Image](/sun/hah.png)

error in blue (how much 15 min samples)
and confedance (in percente) (just the result of the correlation function)
![Image](/sun/errconf.png)


