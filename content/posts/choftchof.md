+++
title = "what is the most fitting timezone for Morocco?"
description = "A TECHNOCRATIC PRATIC"
date = 2026-06-28

[taxonomies]
tags = ['ramblings']

+++

This week the Moroccan government officially announced that
it would switch timezones from the previous GMT+1 to a more
fitting GMT+0.

Personally, I think a timezone is just a convention on what
we should name a certain time. Outside of work time, which
the biological clock should easily adapt to if it was too early,
to get earlier to bed and vice versa, that's why I don't get
how this decision is that popular. I'll just blame it
on oversimplifying populism politics and move on.

But if we actually want to get it right, is GMT+1 really
the fittest option?

The thing about timezones is that they are often whole number
additions and subtractions, so every whole number shift of
longitude is 360/24 = 15° wide, with the Greenwich line
in the middle, meaning GMT+0 is spanning from longitude lines
7.5°E and -7.5°W, and GMT-1 from -7.5°W to -22.5°W.

THE COUNTRY IS DIVIDED:

![Image](/sun/divided.png)

We can see that the -7.5°W longitude line cuts the
country. If we wanted to make a decision based on this map
alone, we should definitely choose GMT-1, but it's people who
use time not territory, so we need a better approach.

I found this [dataset](https://sig-maroc.com/donnees/shapefiles-recensement-2024)
for Moroccan communes and their population count as of
the 2024 demographic count. Using Python I found the
following results:

GMT: 22384541, 61.5% of the populace

GMT-1: 13966489, 38.4% of the populace

Very clear but very close win for the GMT+0 team.

```python
import geopandas as gpd

gdf = gpd.read_file("communes.shp")

if gdf.crs is None:
    gdf = gdf.set_crs(epsg=4326)
elif gdf.crs.to_epsg() != 4326:
    gdf = gdf.to_crs(epsg=4326)

m = gdf.geometry.centroid.x < -7.5

GMT1 = gdf.loc[m, "P_ensemble"].sum()
GMT0 = gdf.loc[~m, "P_ensemble"].sum()


print("GMT+0: ", GMT0, 100*GMT0/(GMT0+GMT1), '%')
print("GMT-1: ", GMT1, 100*GMT1/(GMT0+GMT1), '%')
```

Soooo yeah, that was a waste of time.
