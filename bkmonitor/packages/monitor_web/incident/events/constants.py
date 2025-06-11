"""
Tencent is pleased to support the open source community by making 蓝鲸智云 - 监控平台 (BlueKing - Monitor) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
EVENT_NAMES = ["evnet.flow_error"]
EVENT_ALIAS = {"evnet.flow_error": "flow异常事件"}

EVENTS_SOURCES = ["蓝盾", "BCS", "主机监控", "其他"]
EVENTS_LEVELS = ["warning", "normal", "default"]

# time series原点时间戳，写死主要是方便后续events和metrics的时序对齐
START_TIMESTAMP = 1746682440000
TIME_INTERVAL = 60000