/*
 * Tencent is pleased to support the open source community by making BK-LOG 蓝鲸日志平台 available.
 * Copyright (C) 2021 THL A29 Limited, a Tencent company.  All rights reserved.
 * BK-LOG 蓝鲸日志平台 is licensed under the MIT License.
 *
 * License for BK-LOG 蓝鲸日志平台:
 * --------------------------------------------------------------------
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
 * documentation files (the "Software"), to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
 * and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 * The above copyright notice and this permission notice shall be included in all copies or substantial
 * portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
 * LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
 * NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
 * SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
 */

import { Component as tsc } from 'vue-tsx-support';
import { Component, Prop } from 'vue-property-decorator';
import './text-segmentation.scss';

interface IProps {
  field: any;
  content: String | Number;
  menuClick: Function;
}

@Component
export default class QueryStatement extends tsc<IProps> {
  @Prop({ type: Object, required: true }) field: any;
  @Prop({ type: [String, Number], required: true }) content: string | number;
  @Prop({ type: Function, required: true }) menuClick: Function;

  /** 当前选中分词 */
  curValue = '';
  /** 检索高亮分词字符串 */
  markRegStr = '<mark>(.*?)</mark>';
  /** 默认分词字符串 */
  // eslint-disable-next-line
  segmentRegStr = ',&*+:;?^=!$<>\'"{}()|[]\\/\\s\\r\\n\\t-';
  /** 支持分词最大数量 */
  limitCount = 256;
  /** 当前点击的分词实例 */
  currentEvent = null;
  /** 超出隐藏实例 */
  intersectionObserver = null;

  popoverInstance = null;

  get currentFieldRegStr() {
    try {
      let currentRegStr = this.segmentRegStr;
      if (this.field.tokenize_on_chars) currentRegStr = this.field.tokenize_on_chars;
      return currentRegStr;
    } catch (error) {
      return '';
    }
  }

  get isVirtual() {
    return this.field?.field_type === '__virtual__';
  }

  get isText() {
    return this.field?.field_type === 'text';
  }

  get isAnalyzed() {
    return this.field.is_analyzed;
  }

  get splitList() {
    const value = this.content.toString();
    let arr = [];
    if (this.isAnalyzed) {
      // 这里进来的都是开了分词的情况
      arr = this.splitParticipleWithStr(value, this.currentFieldRegStr);
    } else {
      // 未开分词的情况 且非text类型 则是整个值可点击 否则不可点击
      arr = [
        {
          text: value.replace(/<mark>/g, '').replace(/<\/mark>/g, ''),
          isNotParticiple: this.isText,
          isMark: new RegExp(this.markRegStr).test(value)
        }
      ];
    }
    return arr;
  }

  splitParticipleWithStr(str: string, delimiterPattern: string) {
    // 转义特殊字符，并构建用于分割的正则表达式
    const regexPattern = delimiterPattern
      .split('')
      .map(delimiter => `\\${delimiter}`)
      .join('|');

    // 构建正则表达式以找到分隔符或分隔符周围的文本
    const regex = new RegExp(`(${this.markRegStr}|${regexPattern})`);

    // 高亮
    const markRegex = new RegExp(this.markRegStr, 'g');

    // 使用正则分割字符串
    const parts = str
      .replace(/<mark>/g, '')
      .replace(/<\/mark>/g, '')
      .split(regex);
    const markVal = str.match(markRegex) || [];

    // 转换结果为对象数组，包含分隔符标记
    const result = parts
      .filter(part => part && part.length)
      .map((part, index) => {
        return {
          text: part,
          isNotParticiple: index < this.limitCount ? regex.test(part) : true,
          isMark: this.checkMark(part, markVal)
        };
      });

    return result;
  }

  checkMark(splitItem, markVal) {
    if (!markVal.length) return false;
    const filterMarkArr = markVal.map(item => item.replace(/<mark>/g, '').replace(/<\/mark>/g, ''));
    // 以句号开头或句号结尾的分词符匹配成功也高亮展示
    return filterMarkArr.some(
      item => item === splitItem || splitItem.startsWith(`.${item}`) || splitItem.endsWith(`${item}.`)
    );
  }

  handleClick(e, value) {
    if (!value.toString() || value === '--') return;
    this.handleDestroy();
    this.curValue = value;
    this.popoverInstance = this.$bkPopover(e.target, {
      content: this.$refs.moreTools,
      trigger: 'click',
      placement: 'bottom-start',
      arrow: true,
      theme: 'light',
      interactive: true,
      extCls: 'event-tippy-content',
      onHidden: () => {
        this.unregisterObserver();
        this.popoverInstance && this.popoverInstance.destroy();
        this.popoverInstance = null;
        this.currentEvent.classList.remove('focus-text');
      },
      onShow: () => {
        setTimeout(this.registerObserver, 20);
        this.currentEvent = e.target;
        this.currentEvent.classList.add('focus-text');
      }
    });
    this.popoverInstance && this.popoverInstance.show(10);
  }
  // 注册Intersection监听
  registerObserver() {
    if (this.intersectionObserver) this.unregisterObserver();
    this.intersectionObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (this.intersectionObserver) {
          if (entry.intersectionRatio <= 0) {
            this.popoverInstance.hide();
          }
        }
      });
    });
    this.intersectionObserver.observe(this.$el);
  }
  unregisterObserver() {
    if (this.intersectionObserver) {
      this.intersectionObserver.unobserve(this.$el);
      this.intersectionObserver.disconnect();
      this.intersectionObserver = null;
    }
  }
  handleDestroy() {
    if (this.popoverInstance) {
      this.popoverInstance?.hide(0);
      this.popoverInstance?.destroy();
      this.popoverInstance = null;
      this.curValue = '';
    }
  }

  handleMenuClick(event: string, isLink = false) {
    this.menuClick(event, this.curValue, isLink);
    this.handleDestroy();
  }

  render() {
    return (
      <span class='log-content-wrapper'>
        {this.isVirtual ? (
          <span class='null-item'>{this.content}</span>
        ) : (
          <span class='segment-content'>
            {this.splitList.map(item => {
              if (item.text === '\n') return <br />;
              if (item.isMark) return <mark onClick={$event => this.handleClick($event, item.text)}>{item.text}</mark>;
              if (!item.isNotParticiple)
                return (
                  <span
                    class='valid-text'
                    onClick={$event => this.handleClick($event, item.text)}
                  >
                    {item.text}
                  </span>
                );
              return item.text;
            })}
          </span>
        )}

        <div v-show={false}>
          <div
            ref='moreTools'
            class='event-icons'
          >
            <div class='event-box'>
              <span
                class='event-btn'
                onClick={() => this.handleMenuClick('copy')}
              >
                <i class='icon log-icon icon-copy'></i>
                <span>{this.$t('复制')}</span>
              </span>
            </div>
            <div class='event-box'>
              <span
                class='event-btn'
                onClick={() => this.handleMenuClick('is')}
              >
                <i class='icon bk-icon icon-plus-circle'></i>
                <span>{this.$t('添加到本次检索')}</span>
              </span>
              <div
                class='new-link'
                v-bk-tooltips={this.$t('新开标签页')}
                onClick={e => {
                  e.stopPropagation();
                  this.handleMenuClick('is', true);
                }}
              >
                <i class='log-icon icon-jump'></i>
              </div>
            </div>
            <div class='event-box'>
              <span
                class='event-btn'
                onClick={() => this.handleMenuClick('not')}
              >
                <i class='icon bk-icon icon-minus-circle'></i>
                <span>{this.$t('从本次检索中排除')}</span>
              </span>
              <div
                class='new-link'
                v-bk-tooltips={this.$t('新开标签页')}
                onClick={e => {
                  e.stopPropagation();
                  this.handleMenuClick('new-page', true);
                }}
              >
                <i class='log-icon icon-jump'></i>
              </div>
            </div>
          </div>
        </div>
      </span>
    );
  }
}