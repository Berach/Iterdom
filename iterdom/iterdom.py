#!/usr/bin/env python2

import random
import itertools


def choice(iterator):
    """ Chooses a random item from a generator """

    samplesize = 1
    results = sample(iterator, samplesize)

    return results[0]


def sample(iterator, samplesize):
    """ Chooses a random sample from a generator """

    results = []
    iterator = iter(iterator)

    for _ in xrange(samplesize):
        results.append(iterator.next())

    random.shuffle(results)

    for i, v in enumerate(iterator, samplesize):
        r = random.randint(0, i)
        if r < samplesize:
            results[r] = v

    if len(results) < samplesize:
        raise ValueError("Sample larger than population.")

    return results


def shuffle(iterator):
    """
    Shuffles a generator, has to load the generator
    in to memory to do so, can't shuffle in place
    """
    genlst = list(iterator)
    random.shuffle(genlst)
    return genlst


def choicerange(iterator, start, stop):
    """ Selects a random item from within a range """
    newIt = itertools.islice(iterator, start, stop)

    return choice(newIt)
