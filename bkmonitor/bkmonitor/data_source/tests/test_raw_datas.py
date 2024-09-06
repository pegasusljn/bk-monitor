# """
# Tencent is pleased to support the open source community by making BK-BASE 蓝鲸基础平台 available.
# Copyright (C) 2021 THL A29 Limited, a Tencent company.  All rights reserved.
# BK-BASE 蓝鲸基础平台 is licensed under the MIT License.
# License for BK-BASE 蓝鲸基础平台:
# --------------------------------------------------------------------
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
# NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# """


import unittest
from unittest.mock import patch

from mock import Mock

from bkmonitor.data_source.data_source.rawdatas import BkRawDatasSource



class TestRawDataSource(unittest.TestCase):
    data_raw_obj = BkRawDatasSource()

    def test_get_sampling_data(self, mock_session):
        """
        测试采样
        """
        test_data_id = 525128
        response = BkRawDatasSource.get_sampling_data(test_data_id)
        self.assertEqual(response, {'key': 'value'})
        # def test_get_storages_data(self):
        #     """
        #     测试采样
        #     """
        #     test_data_id = 525128
        #     BkRawDatasSource.get_storages_data(test_data_id)
        #     mock_response = unittest.mock.Mock()
        #     mock_response.status_code = 200
        #     mock_response.json.return_value = {'key': 'value'}
        #
        # def test_get_metrics_data_count(self):
        #     """
        #     测试采样
        #     """
        #     param = {
        #         "start_time": 1725504443,
        #         "end_time": 1725590843,
        #         "bk_biz_id": 525128,
        #     }
        #     BkRawDatasSource.get_metrics_data_count(**param)
        #     mock_response = unittest.mock.Mock()
        #     mock_response.status_code = 200
        #     mock_response.json.return_value = {'key': 'value'}
        #     param = {
        #         "start_time": 1725033600,
        #         "end_time": 1725638399,
        #         "bk_biz_id": 525128,
        #         "is_day": True,
        #     }
        #     BkRawDatasSource.get_metrics_data_count(**param)
        #     mock_response = unittest.mock.Mock()
        #     mock_response.status_code = 200
        mock_response.json.return_value = {'key': 'value'}
