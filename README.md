### RSS Reader 服务端

基于[rss reader](https://github.com/ivone-liu/rss_reader)的服务端程序。

用作用户订阅频道的实时更新，长时间不登入也不会丢失订阅频道更新的内容。

~~框架基于ThinkPHP 5.1。~~

PHP解析起来比较费力，换用Python。 采用`tornado`框架。

### 开发进展

- [x] 基础数据库建设
- [ ] 登入/注册功能
- [ ] 添加RSS功能
- [ ] 获取新数据
- [ ] 计划任务：服务端轮询
- [ ] 客户端同步