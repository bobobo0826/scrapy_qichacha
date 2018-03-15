# scrapy_qichacha:爬取企查查网页信息
##文件名qichacha_data：未登录状态爬取静态页面

      1、运行时在终端输入：scrapy crawl qichacha_data
      
      2、由于代理ip可能失效，为避免程序无法运行，将代理ip的中间件注释了，
         如需要代理ip，要在settings.py中取消注释ProxyMiddleware，并注释JavaScriptMiddleware
      
      3、每个省一共有500页数据，若只爬取几页，可在qichacha_spider.py的start_request中修改爬取页数
      
      4、爬取的数据保存在MongoDB qichacha Industry 中
      
      5、此程序爬取数据以json的形式保存，也可分字段保存
      
##文件名qichacha_mdata：登录状态（添加了headers和cookie）下爬取动态页面

      1、首先登录企查查，抓取cookie和user_agent
      
      2、在cookies.py中更换cookie
      
      3、在user_agents.py中更换agents
      
      4、运行时在终端输入：scrapy crawl qichacha_mdata
      
      5、爬取的数据保存在MongoDB qichachamdata JSONbase 中
