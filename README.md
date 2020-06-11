# CRAWLER FRAMEWORK

## 项目简介

>1. 基于grequests的简单协程爬虫框架
>2. 本爬虫框架基于广度优先爬虫设计
>3. 本爬虫框架默认支持两层爬行深度（可自行添加多层index索引页到redis中间件内，以提升爬虫深度）
>4. 框架执行流程：data_file -> start_url -> start_redis_hash -> downloader -> index_redis_hash -> downloader -> detail_postgresql_table
>5. 上述流程中，downloader模块，parser方法需要传入response的解析函数和response的错误处理函数，一般情况下，仅需要编写index页和detail页的parser_function函数，即可实现爬虫

## 项目依赖

>1. python3.7.3
>2. redis，用于存储index索引页
>3. postgresql，用于存储detail结果页
>4. crawler_proxy_checked，爬虫代理redis hash表，crawler proxy项目中可自动生成该redis hash表

## 部署方式

>1. pip install virtualenv
>2. virtualenv venv
>3. ./venv/bin/pip install -r requirements.txt

## 启停程序

>启动项目
>
>1. bash run.sh
>
>停止项目
>
>1. bash stop.sh
