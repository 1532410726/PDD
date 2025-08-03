import uiautomator2 as u2
import time

def start_app(d):
    d.app_start("com.xunmeng.pinduoduo")
    d.xpath('//*[@content-desc="多多视频"]').click()
    d.xpath('//*[@content-desc="搜索"]').click()
    d.swipe(0.5, 0.8, 0.5, 0.2)
    d.xpath('//*[@text="查看完整榜单"]').click()
    print("进入榜单页面，开始获取")
    time.sleep(2)

def get_card_texts(d, card_index):
    """
    获取榜单卡片指定 index（从1开始）的所有 text 文案
    """
    xpath_expr = f'(//*[@resource-id="com.xunmeng.pinduoduo:id/pdd"])[3]/*[{card_index}]//*'
    nodes = d.xpath(xpath_expr).all()
    texts = []

    for node in nodes:
        try:
            text = node.info.get("text", "").strip()
            if text:
                texts.append(text)
        except Exception as e:
            print("跳过异常节点:", e)

    return texts

def parse_card_info(texts):
    """
    按规则解析标题、集数、热度、标签
    """
    title = texts[0] if len(texts) >= 1 else ""
    episode = texts[1] if len(texts) >= 2 else ""
    heat = texts[-2] if len(texts) >= 2 else ""
    tags = texts[2:-2] if len(texts) > 4 else []

    return {
        "标题": title,
        "集数": episode,
        "热度": heat,
        "标签": tags
    }

def main():
    d = u2.connect()
    start_app(d)
    for i in range(1, 3):  #前三个
        texts = get_card_texts(d, card_index=i)
        info = parse_card_info(texts)
        print(f"\n短剧热榜第{i}的榜单信息：")
        print("标题：", info["标题"])
        print("集数：", info["集数"])
        print("热度：", info["热度"])
        print("标签：", info["标签"])

if __name__ == "__main__":
    main()

