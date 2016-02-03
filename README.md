## 支付宝自动 咻一咻(只支持安卓)

### 原理
    采用Appium 安卓自动化测试，利用uiautomatorviewer 查看每个步骤点击处的resourceId,
    通过find_element_by_id方法获取元素，执行相应的点击。因此，该插件**需要Appium使用基础**


### 环境需求
    node,python,android sdk,appium-pythoh-client

### 使用
    在项目目录，连接上手机，执行 ```python alyHongBao.py```

