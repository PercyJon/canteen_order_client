## renren-fast
- 一个轻量级的Java快速开发平台，能快速开发项目并交付【接私活利器】
- 友好的代码结构及注释，便于阅读及二次开发
- 完善的XSS防范及脚本过滤，彻底杜绝XSS攻击
- 实现前后端分离，通过token进行数据交互
- 后台Git地址：[gitee.com/renrenio/renren-fast](https://gitee.com/renrenio/renren-fast)

## renren-fast-vue
- renren-fast-vue基于vue、element-ui构建开发，实现renren-fast后台管理前端功能，提供一套更优的前端解决方案
- 前后端分离，通过token进行数据交互，可独立部署
- 支持发布时，动态配置CDN静态资源，动态切换新旧版本
- 演示地址：[fast.demo.renren.io](http://fast.demo.renren.io) (账号密码：admin/admin)

![demo-screenshot](https://github.com/daxiongYang/renren-fast-vue/blob/master/screenshot.png)

## 开发
> 无法正常预览项目效果时，请先检查是否正常安装依赖，再查看启动服务是否存在报错

```bash
# 克隆项目
git clone https://github.com/daxiongYang/renren-fast-vue.git

# 安装依赖(优先使用)
npm install
# 安装依赖(下载较慢时使用)
npm install --registry=https://registry.npm.taobao.org

# 启动服务
npm run dev
```

- 开发时，如何连接后台项目api接口？
> 1. 修改renren-fast-vue/static/config/index.js目录文件中window.SITE_CONFIG.baseUrl = '本地api接口请求地址'

- 开发时，如何解决跨域？
> 1. 修改renren-fast-vue/config/dev.env.js目录文件中OPEN_PROXY: true开启代理
> 2. 修改renren-fast-vue/config/index.js目录文件中proxyTable对象target: '代理api接口请求地址'
> 3. 重启本地服务

- 开发时，如何提前配置CDN静态资源？
> 1. 修改renren-fast-vue/static/config/index-[qa/uat/prod].js目录文件中window.SITE_CONFIG.cdnUrl = '静态资源cdn地址' + window.SITE_CONFIG.staticFileName

## 发布
> 构建生成的资源文件保存在renren-fast-vue/dist目录下，可通过config/index.js目录文件修改相关配置信息

```bash
# 构建生产环境(默认)
npm run build

# 构建测试环境
npm run build --qa

# 构建验收环境
npm run build --uat

# 构建生产环境
npm run build --prod
```

- 构建生成后，发布需要上传哪些文件？
> 1. renren-fast-vue/dist目录下：180307（静态资源，由当前日期动态生成文件夹名）、config（配置文件）、index.html

- 构建生成后，如何动态配置CDN静态资源？
> 1. 修改renren-fast-vue/dist/config/index.js目录文件中window.SITE_CONFIG.cdnUrl = '静态资源cdn地址' + window.SITE_CONFIG.staticFileName

- 构建生成后，如何动态切换新旧版本？
> 1. 修改renren-fast-vue/dist/config/index.js目录文件中window.SITE_CONFIG.staticFileName = '180307（静态资源文件夹名称）'


## 其他
``` bash
# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```