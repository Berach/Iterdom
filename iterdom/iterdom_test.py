import iterdom


class TestChoice():
    def test_choicetype(self):
        gen = (x for x in range(1000))
        assert type(iterdom.choice(gen)) == int

    def test_choiceinrange(self):
        gen = (x for x in range(1000))
        assert iterdom.choice(gen) < 1000

    def test_sampletype(self):
        gen = (x for x in range(1000))
        samplesize = 100
        assert type(iterdom.sample(gen, samplesize)) == list

    def test_sampleitemtype(self):
        gen = (x for x in range(1000))
        samplesize = 100
        for i in iterdom.sample(gen, samplesize):
            assert type(i) == int

    def test_samplesize(self):
        gen = (x for x in range(1000))
        samplesize = 100
        assert len(iterdom.sample(gen, samplesize)) == 100

    def test_shuffle(self):
        gen = (x for x in range(1000))
        assert iterdom.shuffle(gen) != range(1000)

    def test_choicerange(self):
        gen = (x for x in range(1000))
        start = 15
        stop = 500
        assert 15 <= iterdom.choicerange(gen, start, stop) <= 500
