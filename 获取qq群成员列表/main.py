import csv
import time
from lxml import etree
from selenium import webdriver


def parser():
    driver = webdriver.Chrome()
    return driver


def login(url):
    driver =parser()
    driver.get(url)
    time.sleep(5)
    get_data(driver)
    return driver


def get_data(driver):
    for _ in range(20):
        scroller(driver)
        time.sleep(1)
    data = driver.page_source
    html = etree.HTML(data)
    mem_info_list = html.xpath('//*[@id="groupMember"]/tbody[@class="list"]/tr')   # TODO  QQ群成员列表

    with open('list.csv', 'a+', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, dialect="excel")
        writer.writerow(['成员', 'QQ号', '性别', '群昵称', '入群时间', '最后发言'])

        for mem_info in mem_info_list:
            data = {}
            data['成员'] = str(mem_info.xpath('./td[3]//text()')[3]).replace('\U0001f60a','').strip()
            data['QQ号'] = str(mem_info.xpath('./td[5]//text()')[0]).replace('\U0001f60a','').strip()
            data['性别'] = str(mem_info.xpath('./td[6]//text()')[0]).replace('\U0001f60a','').strip()
            data['群昵称'] = str(mem_info.xpath('./td[4]//text()')[1]).replace('\U0001f60a','').strip()
            data['入群时间'] = str(mem_info.xpath('./td[8]//text()')[0]).replace('\U0001f60a','').strip()
            data['最后发言'] = str(mem_info.xpath('./td[9]//text()')[0]).replace('\U0001f60a','').strip()
            print(data)

            if data:
                # writer.writerow(['成员', 'QQ号', '性别', '群昵称', '入群时间', '最后发言'])
                writer.writerow([data['成员'].replace('\xa0',''),data['QQ号'].replace('\xa0','').replace('\xa0',''), data['性别'].replace('\xa0',''),data['群昵称'].replace('\xa0',''),data['入群时间'].replace('\xa0',''),data['最后发言'].replace('\xa0','')])


def logout(driver):
    driver.find_element_by_class_name("logout").click()
    driver.quit()
    driver.close()


def scroller(driver):
    js = "var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)


def run():
#    QQnum = input('请输入一个【一个或多个QQ账号】:')
#    for num in QQnum.split(','):
    url = "https://qun.qq.com/member.html#gid=546786372"
    driver = login(url)

    logout(driver)   # TODO  退出登录


if __name__ == '__main__':

    run()