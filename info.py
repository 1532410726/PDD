import uiautomator2 as u2
import time


def get_texts_from_xpath(d, xpath):
    '''

    :param d:
    :param xpath: 父节点下第X个子节点的xpath，X为榜单顺序节点
    :return:返回节点所有的@text属性的信息
    '''
    nodes = d.xpath(xpath + '//*').all()
    texts = []
    for node in nodes:
        try:
            text = node.info.get("text", "").strip()
            if text:
                texts.append(text)
        except Exception as e:
            print("跳过异常节点:", e)
    return texts


def parse_texts(texts):
    '''
    第一个获取到的文案为标题，第二个为集数，倒数第二个为热度，第三个到倒数第三个之间为标签
    :param texts:
    :return: 标题、集数、热度、标签
    '''
    title = texts[0] if len(texts) >= 1 else ""
    episode = texts[1] if len(texts) >= 2 else ""
    heat = texts[-2] if len(texts) >= 2 else ""
    tags = texts[2:-2] if len(texts) > 4 else []
    return title, episode, heat, tags


def get_hot_rank_info(d, top_num):
    print(f"热榜第{top_num}条数据")
    xpath = f'(//*[@resource-id="com.xunmeng.pinduoduo:id/pdd"])[3]/*[{top_num}]'
    texts = get_texts_from_xpath(d, xpath)
    title, episode, heat, tags = parse_texts(texts)

    print("标题：", title)
    print("集数：", episode)
    print("热度：", heat)
    print("标签：", tags)
    print()


def get_woman_rank_info(d, top_num):
    print(f"女生榜第{top_num}条数据")
    d.xpath('//*[@text="女生榜"]').click()
    time.sleep(1)

    xpath = f'(//*[@resource-id="com.xunmeng.pinduoduo:id/pdd"])[3]/*[{top_num}]'
    texts = get_texts_from_xpath(d, xpath)
    title, episode, heat, tags = parse_texts(texts)

    print("标题：", title)
    print("集数：", episode)
    print("热度：", heat)
    print("标签：", tags)
    print()


def get_man_rank_info(d, top_num):
    print(f"男生榜第{top_num}条数据")
    d.xpath('//*[@text="男生榜"]').click()
    time.sleep(1)

    xpath = f'(//*[@resource-id="com.xunmeng.pinduoduo:id/pdd"])[3]/*[{top_num}]'
    texts = get_texts_from_xpath(d, xpath)
    title, episode, heat, tags = parse_texts(texts)

    print("标题：", title)
    print("集数：", episode)
    print("热度：", heat)
    print("标签：", tags)
    print()


def main():
    d = u2.connect()
    d.app_start("com.xunmeng.pinduoduo")
    d.xpath('//*[@content-desc="多多视频"]').click()
    d.xpath('//*[@content-desc="搜索"]').click()
    d.swipe(0.5, 0.8, 0.5, 0.2)
    d.xpath('//*[@text="查看完整榜单"]').click()
    time.sleep(2)
    for i in range(1, 4):
        get_hot_rank_info(d, top_num=i)
    for i in range(1, 4):
        get_woman_rank_info(d, top_num=i)
    for i in range(1, 4):
        get_man_rank_info(d, top_num=i)
    d.app_stop("com.xunmeng.pinduoduo")


if __name__ == "__main__":
    main()
