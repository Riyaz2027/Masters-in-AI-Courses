import unittest
from unittest.mock import patch
import builtins

class TestRainfallScript(unittest.TestCase):
    @patch('builtins.input')
    @patch('builtins.print')
    def test_rainfall_for_2_years(self, mock_print, mock_input):
        # Simulate input: 2 years, 24 rainfall values
        test_inputs = ['2'] + [str(val) for val in [
            1.2, 2.3, 0.8, 1.5, 2.0, 1.1, 0.9, 1.7, 2.2, 1.3, 0.6, 1.0,  # Year 1
            1.4, 2.1, 0.7, 1.6, 2.3, 1.2, 1.0, 1.8, 2.0, 1.5, 0.9, 1.1   # Year 2
        ]]
        mock_input.side_effect = test_inputs

        # Import the script (executes the code)
        with open(
            '/Applications/Projects/Masters_Courses_Workspace/Masters-in-AI-Courses/Course1/5_Module/CT_01_Rainfall.py'
        ) as f:
            code = f.read()
            exec(code, {})


        # Check print calls for expected results
        # Total months: 24
        # Total inches: sum of all values
        # Average: total / 24
        total_inches = sum([
            1.2, 2.3, 0.8, 1.5, 2.0, 1.1, 0.9, 1.7, 2.2, 1.3, 0.6, 1.0,
            1.4, 2.1, 0.7, 1.6, 2.3, 1.2, 1.0, 1.8, 2.0, 1.5, 0.9, 1.1
        ])
        average_inches = total_inches / 24

        mock_print.assert_any_call(f"Total months: 24")
        mock_print.assert_any_call(f"Total inches of rain: {total_inches:.2f}")
        mock_print.assert_any_call(f"Average inches of rain per month: {average_inches:.2f}")
        # Print all calls to verify
        # for call in mock_print.call_args_list:
        #     print(call)


if __name__ == '__main__':
    unittest.main()
# This code tests the rainfall calculation script by simulating user input for two years of rainfall data
# and checking the output for correctness.
