from unittest import TestCase, mock
import pytest
import asyncio
import fs
import aiounittest

async def get_da():
    return await fs.get_data()

class TestExample(aiounittest.AsyncTestCase):
        
    @mock.patch('fs.check_output', return_value=b"food\nbar\n")
    def test_pring_contents_of_cwd(self, mock_check_output):
        actual_result = fs.print_contents_of_cwd()
        print(actual_result);
        expected_directory = b'food'
        self.assertIn(expected_directory, actual_result)
            
    async def test_get_data(self):
        result = await get_da()
        print(result)
        
    @mock.patch('fs.get_data', return_value={"body": {"destinations":[]}})
    async def test_get_data_mock(self, mock_data):
        result = await get_da()
        print('mock result: ', result)
    
    @mock.patch('fs.get_data', return_value={"body": {"destinations":["1233"]}})
    async def test_get_data_to_print_mock(self, mock_data):
        result = await fs.get_data_to_print()
        print('mock result 2222: ', result)