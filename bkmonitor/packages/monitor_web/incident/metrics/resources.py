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
from core.drf_resource.base import Resource
from monitor_web.incident.metrics.serializers import MetricsSearchSerializer
from monitor_web.incident.metrics.mock_data import INCIDENT_METRICS_SEARCH_MOCK_DATA

class IncidentMetricsSearchResource(Resource):
    """
    故障告警指标查询接口
    """

    def __init__(self):
        super().__init__()

    class RequestSerializer(MetricsSearchSerializer):
        pass

    def perform_request(self, validated_request_data: dict) -> dict:
        return INCIDENT_METRICS_SEARCH_MOCK_DATA
    


