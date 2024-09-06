# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云 - 监控平台 (BlueKing - Monitor) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
import unittest
from unittest.mock import patch

from bkmonitor.data_source.data_source.rawdatas import BkRawDatasSource


class TestRawDataSource(unittest.TestCase):
    data_raw_obj = BkRawDatasSource()

    @patch('core.drf_resource.APIResource.perform_request')
    def test_get_sampling_data(self, mock_get):
        """
        采样
        """
        mock_get.return_value = {"data": []}
        test_data_id = 525128
        response = BkRawDatasSource.get_sampling_data(test_data_id)
        self.assertEqual(response, {"data": []})

    @patch('core.drf_resource.APIResource.perform_request')
    def test_get_storages_data(self, mock_get):
        """
        存储信息
        """

        mock_get.return_value = {"data": []}
        test_data_id = 525128
        response = BkRawDatasSource.get_storages_data(test_data_id)
        self.assertEqual(response, {"data": []})

    @patch('core.drf_resource.APIResource.perform_request')
    def test_get_metrics_by_minute(self, mock_get):
        """
        数据量统计-分钟
        """
        mock_get.return_value = {"data": []}
        param = {
            "start_time": 1725504443,
            "end_time": 1725590843,
            "bk_biz_id": 525128,
        }

        response = BkRawDatasSource.get_metrics_data_count(**param)
        self.assertEqual(response, {"data": []})

    @patch('core.drf_resource.APIResource.perform_request')
    def test_get_metrics_by_day(self, mock_get):
        """
        数据量统计-天
        """
        mock_get.return_value = {"data": []}

        param = {
            "start_time": 1725033600,
            "end_time": 1725638399,
            "bk_biz_id": 525128,
            "is_day": True,
        }
        response_day = BkRawDatasSource.get_metrics_data_count(**param)
        self.assertEqual(response_day, {"data": []})
