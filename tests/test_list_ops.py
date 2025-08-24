from list_ops import flatten_list, deep_reverse

def test_flatten_list():
    assert flatten_list([[1,'a',['cat'],2],[[[3]],'dog'],4,5]) == [1,'a','cat',2,3,'dog',4,5]

def test_deep_reverse():
    assert deep_reverse([[1,2],[3,4],[5,6,7]]) == [[7,6,5],[4,3],[2,1]]
