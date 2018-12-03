### RSS Reader 服务端

基于[rss reader](https://github.com/ivone-liu/rss_reader)的服务端程序。

用作用户订阅频道的实时更新，长时间不登入也不会丢失订阅频道更新的内容。

~~框架基于ThinkPHP 5.1。~~

PHP解析起来比较费力，换用Python。 采用`tornado`框架。

### 开发进展

**version1.0**

- [x] 基础数据库建设
- [x] 登入/注册功能
- [x] 添加RSS功能
- [x] 获取新数据
- [x] 计划任务：服务端轮询
- [x] 客户端同步

**version2.0**

- [ ] 采用json web token方式数据交互