
# 초기설정 ref.: https://wikidocs.net/91474
# 초기설정 ref.: https://catloaf.tistory.com/19

import time
from selenium import webdriver


def ExplorePilmography(driver, max_num=4):  # max_num: 최대 작품 수
    # 최근 활동 정보
    elements = driver.find_elements_by_xpath('//strong[@class="this_text"]')
    work_num = 0

    for i in range(len(elements)):
        elements = driver.find_elements_by_xpath('//strong[@class="this_text"]')    # 뒤로 가기 누르면 정보가 바뀌는 듯

        if elements[i].text == '':
            continue
        work_num += 1

        elements[i].click()
        time.sleep(1)

        # 시청률 확인
        for j, ele in enumerate(driver.find_elements_by_tag_name('dt')):
            if ele.text == '시청률':
                viewer_ratings = driver.find_elements_by_tag_name('dd')[j].text.split()[0]
                print(viewer_ratings)
                break

        if work_num == max_num:
            break

        driver.back()
        time.sleep(1)


def Crawling(search_name="김은숙"):
    path = "C:/Users/user/Downloads/chromedriver_win32/chromedriver.exe"
    driver = webdriver.Chrome(path)

    # 검색
    driver.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=" + search_name)
    time.sleep(1)

    # 최근 작품 탐색
    flag = 0
    for ele in driver.find_elements_by_xpath('//li[@class="_tab"]'):
        if ele.text == '방송':
            ele.click()
            flag = 1
            break
    if not flag:
        print("방송 태그를 찾을 수 없습니다.")
        exit()

    # 더보기 클릭
    driver.find_element_by_xpath('//a[@data-tab="onair"]').click()

    time.sleep(1)
    ExplorePilmography(driver)

    driver.quit()


if __name__ == "__main__":
    Crawling()