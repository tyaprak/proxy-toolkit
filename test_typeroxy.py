import unittest
import os
import concurrent.futures
from unittest.mock import patch, mock_open
#from datetime import datetime

from typeroxy import worker, main, DATE  # Import from your script

class TestProxyChecker(unittest.TestCase):

    def setUp(self):
        # Create a dummy proxies file for testing
        self.proxies_file_content = [
            "192.168.1.1:8080\n",
            "10.0.0.1:3128\n",
            "invalid_proxy\n",
            "172.16.0.1:80\n"
        ]
        with open("proxies-2024_11_19_00_17.txt", "w") as f:
            f.writelines(self.proxies_file_content)
        
        self.output_filename= rf"final_check-{DATE}.txt"

    def tearDown(self):
        # Clean up the dummy files after testing
        if os.path.exists("proxies-2024_11_19_00_17.txt"):
            os.remove("proxies-2024_11_19_00_17.txt")
        if os.path.exists(self.output_filename):
            os.remove(self.output_filename)
    

    @patch("typeroxy.ProxyChecker.check_proxy")
    @patch("builtins.open", new_callable=mock_open)
    def test_worker_valid_proxy(self, mock_file, mock_check_proxy):
        # Mock the ProxyChecker to return a valid result
        mock_check_proxy.return_value = {'protocols': ['http'], 'anonymity': 'Transparent', 'timeout': 100, 'country': 'Test', 'country_code': 'TT'}
        proxy = "192.168.1.1:8080"
        worker(proxy)

        # Assert that check_proxy was called
        mock_check_proxy.assert_called_once_with(proxy)

        # Assert that the file was opened in append mode and the content was written
        mock_file.assert_called_with(self.output_filename, "a")
        mock_file().write.assert_called_with(f"{proxy} - {{'protocols': ['http'], 'anonymity': 'Transparent', 'timeout': 100, 'country': 'Test', 'country_code': 'TT'}}\n")

    @patch("typeroxy.ProxyChecker.check_proxy")
    @patch("builtins.open", new_callable=mock_open)
    def test_worker_invalid_proxy(self, mock_file, mock_check_proxy):
        # Mock the ProxyChecker to return None (invalid proxy)
        mock_check_proxy.return_value = None
        proxy = "invalid_proxy"
        worker(proxy)

        # Assert that check_proxy was called
        mock_check_proxy.assert_called_once_with(proxy)

        # Assert that the file was opened but nothing was written (no valid proxy)
        mock_file.assert_not_called()
        mock_file().write.assert_not_called()
    
    @patch("typeroxy.ProxyChecker.check_proxy")
    @patch("builtins.open", new_callable=mock_open)
    def test_worker_exception_in_check_proxy(self, mock_file, mock_check_proxy):
         # Mock the ProxyChecker to return an exception
        mock_check_proxy.side_effect = Exception("Some error during check")
        proxy = "192.168.1.1:8080"
        
        try:
            worker(proxy)
        except Exception:
           self.fail("worker should not raise exception")
        
        mock_check_proxy.assert_called_once_with(proxy)
        # Assert that the file was opened but nothing was written (no valid proxy)
        mock_file.assert_not_called()
        mock_file().write.assert_not_called()

    @patch("typeroxy.worker")
    @patch("concurrent.futures.ThreadPoolExecutor")
    @patch("builtins.print")
    def test_main_function(self, mock_print, mock_executor, mock_worker):
        # Mock ThreadPoolExecutor context manager
        mock_executor.return_value.__enter__.return_value.submit.side_effect = lambda func, arg: concurrent.futures.Future()
        mock_future = concurrent.futures.Future()
        mock_future.set_result("future result")
        concurrent.futures.as_completed = lambda x : [mock_future for y in x ]
        
        mock_worker.return_value = None

        main()
        # Assert that worker was called for each proxy in the file
        self.assertEqual(mock_worker.call_count, len(self.proxies_file_content))
        
        # Assert print was called
        mock_print.assert_called_with("future result")

        # Clean up after the test

if __name__ == "__main__":
    unittest.main()