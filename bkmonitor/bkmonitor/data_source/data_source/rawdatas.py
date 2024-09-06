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
from core.drf_resource import api
from core.errors.api import BKAPIError
from core.errors.bkmonitor.rawdatas import StoragesApiError, SamplingApiError, MetricsDataCountApiError


class BkRawDatasSource(object):

    @staticmethod
    def get_storages_data(bk_biz_id):
        """
        获取存储信息
        参数:
        bk_biz_id：数据源id

        return:
        api response

        except:
        StoragesApiError
        """
        try:
            response = api.bkdata.get_storages_data(raw_data_id=bk_biz_id, with_sql=True)
            return response
        except BKAPIError:
            raise StoragesApiError()

    @staticmethod
    def get_sampling_data(bk_biz_id):
        """
        获取采样数据
        """
        try:
            response = api.bkdata.get_sampling_data(data_id=bk_biz_id)
            return response
        except BKAPIError:
            return SamplingApiError()

    @staticmethod
    def get_test(bk_biz_id):
        """
        获取采样数据
        """
        response = api.bkdata.test(raw_data_id=bk_biz_id)
        return response

    @staticmethod
    def get_metrics_data_count(start_time, end_time, bk_biz_id, is_day=False):
        """
        获取数据量统计

        param：
        start_time(int):开始时间(时间戳)
        end_time(int):结束时间(时间戳)
        bk_biz_id(int):数据源ID
        time_grain(bool):是否为天查询

        return:
        api data

        except:
        """
        params = {
            "start_time": f"{start_time}s",
            "end_time": f"{end_time}s",
            "bk_biz_id": bk_biz_id,
        }
        if is_day:
            params.update({"time_grain": "1d"})

        try:
            response = api.bkdata.get_metrics_data_count(**params)
            return response
        except:
            raise MetricsDataCountApiError()
