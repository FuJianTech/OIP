# !/bin/env python
# -*- coding=utf-8 -*-


import requests
import os
from lxml import etree


class DownTf(object):
    """
    This is a download file Class，from https://pypi.org/project/tensorflow/#history.
    Include tensorflow history version and python history version
    """
    def __init__(self):
        self.tf_his_url = "https://pypi.org/project/tensorflow/#history"
        self.save_folder = './TF/'

    def return_html_by_request_url(self, url):
        content = requests.get(url)
        html = etree.HTML(content.text)
        return html

    def tf_history(self, tf_his_url):
        """
        :param tf_his_url: "https://pypi.org/project/tensorflow/#history"
        :return:  list
        """
        tf_history_html = self.return_html_by_request_url(tf_his_url)
        data_list = []
        for j in range(50):  # random choose num ,should be bigger than all nums
            try:
                html_data = tf_history_html.xpath(f'//*[@id="history"]/div/div[{j}]/a/p[1]')
                for i in html_data:
                    res = i.text.replace("\n", "").replace(" ", "")
                    if res not in data_list:
                        data_list.append(res)
            except Exception as e:
                print(e)
        return data_list

    def tf_version(self, tf_list):
        """
        :param tf_list :["2.4.0"..."1.13.0rc1"]
        :return: tf_version_list : ["https://xxx/xxx/tf-2.4-cp3.8.whl"..."https://xxx/xxx/tf-2.4-cp3.5.whl"]
        """
        tf_version_list = []
        for j in range(1, 4):
            for i in tf_list:
                tf_ver_url = f'https://pypi.org/project/tensorflow/{i}/#files'
                tf_list_html = self.return_html_by_request_url(tf_ver_url)
                html_data = tf_list_html.xpath(f'//*[@id="files"]/table/tbody/tr[{j}]/th/a/@href')

                for tf_last_url in html_data:
                    print(f'read {tf_last_url}')
                    tf_version_list.append(tf_last_url)
        print('There are {len(tf_version_list)} documents in total')

        return tf_version_list

    def progress_bar(self, url, save_folder):

        file_name = url.split("/")[-1]
        try:
            if url is None or save_folder is None or file_name is None:
                print('parameter error')
                return None
            # if folder not exist,create it
            folder = os.path.exists(save_folder)
            if not folder:
                os.makedirs(save_folder)
            # read url resource
            res = requests.get(url, stream=True)
            total_size = int(int(res.headers["Content-Length"]) / 1024 + 0.5)
            # get file address
            file_path = os.path.join(save_folder, file_name)
            if os.path.exists(file_path):
                print("file is exist")
                pass
            else:
                # Open local folder path, which is written in binary stream and saved locally
                from tqdm import tqdm
                with open(file_path, 'wb') as fd:
                    print('start download file：{},current file size：{}KB'.format(file_name, total_size))
                    for chunk in tqdm(iterable=res.iter_content(1024), total=total_size, unit='k', desc=None):
                        fd.write(chunk)
                    print(file_name + 'download complete !')

        except Exception as e:
            print(e)

    def down_tf_file(self, tf_version_list):
        for url in tf_version_list:
            self.progress_bar(url, self.save_folder)

    def main(self):
        tf_list = self.tf_history(self.tf_his_url)
        tf_version_list = self.tf_version(tf_list)
        self.down_tf_file(tf_version_list)


if __name__ == '__main__':
    DownTf().main()
