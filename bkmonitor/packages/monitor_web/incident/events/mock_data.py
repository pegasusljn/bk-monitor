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

INCIDENT_EVENTS_SEARCH_MOCK_DATA = {
        "series": [
            {
                "dimensions": {},
                "target": "COUNT(_index)",
                "metric_field": "_result_",
                "datapoints": [
                    [
                        1749124800000,     # 时序
                        0                  # 事件序列值
                    ],
                    [
                        1749125100000,
                        0
                    ],
                    [
                        1749125400000,
                        2
                    ],
                ],
                "alias": "_result_",
                "type": "bar",
                "dimensions_translation": {},
                "unit": ""
            }
        ],
        "metrics": [],
}
