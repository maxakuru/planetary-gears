# planetary-gears

Helps generate planetary gear combinations: 
- number of teeth for sun, planets, outer ring
- output gear ratio
- module/sizes

Only works with split-ring compound planetary gears that are driven via first stage sun gear and output through second/last stage's outer ring, AKA split-ring [epicyclic](https://en.wikipedia.org/wiki/Epicyclic_gearing).

## Usage

1. Setup `./gears/config.py` to your liking
2. Run `python3 main.py`

#### It will write a CSV to `./output` that contains something like this:
```csv
ratio,N_planets,module0,NT_ring0,NT_sun0,NT_planet0,module1,NT_ring1,NT_sun1,NT_planet1
0,3,0.9615384615384616,26,10,8,0.9615384615384616,26,10,8
34.8,3,0.9615384615384616,26,10,8,0.8241758241758241,29,13,8
144.0,3,0.9615384615384616,26,10,8,0.8241758241758241,30,12,9
-74.4,3,0.9615384615384616,26,10,8,0.8241758241758241,31,11,10
-30.72,3,0.9615384615384616,26,10,8,0.8241758241758241,32,10,11
19.2,3,0.9615384615384616,26,10,8,0.7211538461538461,32,16,8
31.68,3,0.9615384615384616,26,10,8,0.7211538461538461,33,15,9
81.6,3,0.9615384615384616,26,10,8,0.7211538461538461,34,14,10
...
```

#### Or in a more readable format:

| ratio | N_planets | module0 | NT_ring0 | NT_sun0 | NT_planet0 | module1 | NT_ring1 | NT_sun1 | NT_planet1 |
| ----- | --------- | ------- | -------- | ------- | ---------- | ------- | -------- | ------- | ---------- |
| 0 | 3 | 0.9615384615384616 | 26 | 10 | 8 | 0.9615384615384616 | 26 | 10 | 8 |
| 34.8 | 3 | 0.9615384615384616 | 26 | 10 | 8 | 0.8241758241758241 | 29 | 13 | 8 |
| 144.0 | 3 | 0.9615384615384616 | 26 | 10 | 8 | 0.8241758241758241 | 30 | 12 | 9 |
| -74.4 | 3 | 0.9615384615384616 | 26 | 10 | 8 | 0.8241758241758241 | 31 | 11 | 10 |
| -30.72 | 3 | 0.9615384615384616 | 26 | 10 | 8 | 0.8241758241758241 | 32 | 10 | 11 |
| 19.2 | 3 | 0.9615384615384616 | 26 | 10 | 8 | 0.7211538461538461 | 32 | 16 | 8 |
| 31.68 | 3 | 0.9615384615384616 | 26 | 10 | 8 | 0.7211538461538461 | 33 | 15 | 9 |
| 81.6 | 3 | 0.9615384615384616 | 26 | 10 | 8 | 0.7211538461538461 | 34 | 14 | 10 |

... and many more rows

where,
* `N_planets`  = number * of planets
* `moduleN`    = module of stage N
* `NT_ringN`   = number of teeth for ring in stage N
* `NT_sunN`    = number of teeth for sun in stage N
* `NT_planetN` = number of teeth for each planet in stage N