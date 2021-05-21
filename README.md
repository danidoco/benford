# Benford

Benford's law visualization with matplotlib.

Benford's law states that the first digit is likely to be small in the decimal value of naturally occurring numbers.
For example, if you collect data such as election votes, broadcast ratings, and soccer match data, 
the first digit of the data is most likely to be 1, the probability of 2 is less, and the probability of 3 is less than that.
Also, it is similar to a logarithmic graph if these probabilities are listed and graphed.

This simple code proves Benford's law not in a theoretical way but in an experimental way. (Not perfect)

## How it works

1. Read ```url.txt``` to crawl web pages with urls.
2. Crawl web pages.
3. Extract numbers.
4. Determine what the first digit of a number is and count.
5. Visualize.

## How to test

First things first, install matplotlib with ```pip```.
```
$ pip install matplotlib
```

Then, run ```visualization.py``` by typing this.
```
$ python visualization.py
```

Add urls to ```urls.txt``` to collect more data.
