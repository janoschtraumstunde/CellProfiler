""" tests - tests of CellProfiler-level modules

Also test numpy and scipy here
"""

if __name__ == "__main__":
    import scipy.io.matlab
    import unittest
    import nose
    
    scipy.io.matlab.test()
    nose.main()
    
