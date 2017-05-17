from unittest import TestCase


class TestInsertionSort(TestCase):
    #check if data is none it should be false
    #check if data has less then 2 then display the same
    #check if the build works properly
    def test_check_if_data_is_none_it_should_be_false(self):
        try:
            from build import InsertionSort
        except ImportError:
            self.assertFalse("Import Error")

        s = InsertionSort()

        result = s.build(None)
        self.assertEqual(None,result)
