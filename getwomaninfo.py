import uiautomator2 as u2

d = u2.connect()

d.app_start("com.xunmeng.pinduoduo")
d.xpath('//*[@content-desc="多多视频"]').click()
d.xpath('//*[@content-desc="搜索"]').click()
d.swipe(0.5, 0.8, 0.5, 0.2)
d.xpath('//*[@text="查看完整榜单"]').click()
d.sleep(2)
d.xpath('//*[@text="女生榜"]').click()

print("进入女生榜单页面，开始获取")

d.sleep(2)
#all_text_nodes = d.xpath("(//android.view.ViewGroup)[50]//*").all()
#parent_element = d(resourceId="com.xunmeng.pinduoduo:id/pdd")
first_child_xpath = '(//*[@resource-id="com.xunmeng.pinduoduo:id/pdd"])[3]/*[2]'
all_nodes = d.xpath(first_child_xpath + '//*').all()

# 提取所有非空 text 文案
texts = []
for node in all_nodes:
    try:
        info = node.info
        text = info.get("text", "").strip()
        if text:
            texts.append(text)
    except Exception as e:
        print("跳过异常节点:", e)
print(texts)
title = texts[0] if len(texts) >= 1 else ""
episode = texts[1] if len(texts) >= 2 else ""
heat = texts[-2] if len(texts) >= 2 else ""
tags = texts[2:-2] if len(texts) > 4 else []

print("标题：", title)
print("集数：", episode)
print("热度：", heat)
print("标签：", tags)
