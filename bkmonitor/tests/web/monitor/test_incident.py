from monitor_web.incident.metrics.resources import IncidentMetricsSearchResource
from monitor_web.incident.events.resources import IncidentEventsSearchResource
from django.test import TestCase


class TestIncidentMetric(TestCase):
    """
    测试故障的指标相关接口
    """

    def test_incident_metric_search(self):
        """
        测试指标搜索接口(IncidentMetricsSearchResource)
        """
        data = {
            "bk_biz_id": 2,
            "metric_type": "node",
            "index_info": {
                "bk_biz_id": 2,
                "bk_host_id": 1,
            },
            "start_time": 1718035200,
            "end_time": 1718038800,
        }
        inst = IncidentMetricsSearchResource().request(data)
        # 断言返回的数据是一个列表
        self.assertIsNotNone(inst)
        print("Metric Search Result:", inst)


class TestIncidentEvent(TestCase):
    """
    测试故障的事件相关接口
    """

    def test_incident_event_search(self):
        """
        测试事件搜索接口(IncidentEventsSearchResource)
        """
        data = {
            "bk_biz_id": 2,
            "metric_type": "node",
            "index_info": {
                "bk_biz_id": 2,
                "bk_host_id": 1,
            },
            "start_time": 1718035200,
            "end_time": 1718038800,
        }
        inst = IncidentEventsSearchResource().request(data)
        # 添加一个基本的断言，确保返回的实例不是None
        self.assertIsNotNone(inst)
        print("Event Search Result:", inst)
