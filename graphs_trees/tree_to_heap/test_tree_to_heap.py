from nose.tools import assert_equal

class TestTreeToHeap(object):
    
    def test_build_max_heap(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        output_heap = build_max_heap(test_input)
        
        assert_equal(is_max_heap(output_heap), True)
        
        print "Success: test_build_max_heap"
    
    
    def test_build_min_heap(self):
        test_input = [3, 5, 4, 2, 6, 8, 9, 7, 1]
        output_heap = build_min_heap(test_input)
        
        assert_equal(is_min_heap(output_heap), True)
        
        print "Success: test_build_min_heap"
        
def main():
    test = TestTreeToHeap()
    
    test.test_build_max_heap()
    test.test_build_min_heap()

if __name__ == "__main__":
    main()