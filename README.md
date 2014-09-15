Iterdom
======

A small Python 2 library for working with generators, with a specific focus on getting random items from generators.

Usage
======
**iterdom.choice(iterator)**
Returns a random item from a generator without loading the whole list in to memory.

**iterdom.sample(iterator, samplesize)**
Returns a random sample from a generator of defined samplesize quickly.

**iterdom.shuffle(iterator)**
Returns a shuffled *list* from a generator.

**iterdom.choicerange(iterator, start, stop)**
Returns a random item in the defined range.