from programs.questions import one, two, three, four, five, six

def test_one():
    assert one("hello world", "aeiou") == "h_ll_ w_rld"
    assert one("didgeridoo", "do") == "_i_geri___"
    assert one("punctuation, or something?", " ,?") == "punctuation__or_something_"

def test_two():
    assert two(270) == (0, 0, 4, 30)
    assert two(3600) == (0, 1, 0, 0)
    assert two(86400) == (1, 0, 0, 0)
    assert two(0) == (0, 0, 0, 0)

def test_three():
    assert three({'hello':'hola', 'thank you':'gracias'}) == {'hola':'hello', 'gracias':'thank you'}
    assert three({101:'Optimisation', 102:'Partial ODEs'}) == {'Optimisation':101, 'Partial ODEs':102}

def test_four():
    assert four(10) == 5
    assert four(24) == 12
    assert four(7) == 1
    assert four(-10) == 5
    assert four(1) == 1

def test_five():
    assert five('abcdef') == 'a'
    assert five('LoremIpsum') == 'I'
    assert five('hello world!') == ' '

def test_six():
    assert six('hello world, how are you?', 12) == ['hello world,', 'how are you?']
    assert six('hello world, how are you?', 6) == ['hello', 'world,', 'how', 'are', 'you?']
    assert six('hello world, how are you?', 20) == ['hello world, how are', 'you?']
