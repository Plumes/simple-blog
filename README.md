这是一个简单的静态博客生成程序
添加新文章时，先在 rawpost 目录下新建一个 英文命名的 txt 文件，在文件头部按格式添加文章信息，多标签用英文逗号分隔
然后运行 conver.py 将 rawpost 转换成 post ，即生成文章 html 页面
然后再运行 make_index.py 为文章生成索引。
再用 git 上传即可
note:
1.需要 python 3.3