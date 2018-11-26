### RSS Reader 服务端

基于[rss reader](https://github.com/ivone-liu/rss_reader)的服务端程序。

用作用户订阅频道的实时更新，长时间不登入也不会丢失订阅频道更新的内容。

接口协议采用`OAuth2`。

框架基于ThinkPHP 5.1。

### OAuth 身份验证说明

sign计算方法

`md5(appid=post.appid&mobile=post.mobile&nonce=post.nonce&timestamp=post.timestamp&key=secretkey)`


authentication计算方法

接口请求时添加header`authentication`，值为`authentication:USERID base64_encode(appid:accesstoken:uid)`


refresh 请求

需提供旧access_token以及appid来验证身份