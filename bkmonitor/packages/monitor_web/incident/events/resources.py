"""
Tencent is pleased to support the open source community by making 蓝鲸智云 - 监控平台 (BlueKing - Monitor) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

import logging
import random
import string
import time
from core.drf_resource.base import Resource
from monitor_web.incident.events.serializers import EventsSearchSerializer
from monitor_web.incident.events.constants import EVENT_NAMES, EVENT_ALIAS, EVENTS_SOURCES, EVENTS_LEVELS, START_TIMESTAMP, TIME_INTERVAL


class IncidentEventsSearchResource(Resource):
    """
    故障告警指标查询接口
    """

    def __init__(self):
        super().__init__()

    RequestSerializer = EventsSearchSerializer

    def perform_request(self, validated_request_data: dict) -> dict:
        metric_type = validated_request_data.get("metric_type")
        bk_biz_id = validated_request_data.get("bk_biz_id")
        mock_response = {}
        mock_response["bk_biz_id"] = bk_biz_id
        mock_response["events"] = {}
        mock_response["statistics"] = {
            "event_source": {},
            "event_level": {}
        }
        random_number = random.randint(2, 5)
        for i in range(random_number):
            random_str = "".join(random.choices(string.ascii_letters, k=5))
            random_lable = f"{int(time.time())}_{random_str}"
            origin_events_name = random.choice(EVENT_NAMES)
            event_name = f"{origin_events_name}_{random_lable}"
            event_alias = f"{EVENT_ALIAS[origin_events_name]}_{random_lable}"
            event_source = random.choice(EVENTS_SOURCES)
            event_level = random.choice(EVENTS_LEVELS)
            statistics = mock_response["statistics"]
            statistics["event_source"][event_source] = statistics["event_source"].get(
                event_source, 0) + 1
            statistics["event_level"][event_level] = statistics["event_level"].get(
                event_level, 0) + 1
            mock_response["events"][event_name] = {
                "event_name": event_name,
                "event_alias": event_alias,
                "event_source": event_source,
                "event_level": event_level,
                "series": []
            }
            random_series_number = random.randint(3, 5)
            for j in range(random_series_number):
                mock_response["events"][event_name]["series"].append(
                    {
                        "dimensions": {},
                        "target": "COUNT(_index)",
                        "metric_field": "_result_",
                        "datapoints": [
                            [
                                START_TIMESTAMP+j*TIME_INTERVAL,
                                random.randint(0, 20),
                            ] for j in range(random.randint(3, 8))
                        ],
                        "alias": "_result_",
                        "type": "bar",
                        "dimensions_translation": {},
                        "unit": ""
                    }
                )
        return mock_response
