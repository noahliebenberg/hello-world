
def test(l):
    return sum(l)

def test_1():
    assert test([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_1()
    print("Everything passed")
