# !/usr/bin/env python
# -*- coding: utf-8 -*-

# from apps.logic.applications.application_vue_demo.database.model import *

from flask import request, render_template

from apps import appdir
from apps.DB.sql_orm import *
from werkzeug.utils import secure_filename


class TableAnalysis(object):
    def __init__(self):
        self.OpOr = OperateOrm()

    def readdata(self):
        res_list = self.OpOr.select_all_data(Todolist)
        return res_list

    def submit(self):
        if request.method == 'POST':
            data = request.data.decode()
            if data != '':
                d = eval(data)
                print(23, d)
                date = d['date']
                mission = d['mission']
                level = d['level']
                add_one_str = Todolist(date=date, mission=mission, level=level)
                self.OpOr.add_one_data(add_one_str)

    def delectdata(self):
        data = request.data.decode()
        if request.method == 'POST':
            if data != '':
                data = eval(data)
                print(36, type(data))
                delete_data_dict = {"table": Todolist, "filters": Todolist.id == data.get('id')}
                print(38, delete_data_dict)
                self.OpOr.delete_data(delete_data_dict)
                print('ok')

    def update(self):
        data = request.data.decode()
        if request.method == 'POST':
            if data != '':
                update_data_dict = {"table": Todolist, "filters": Todolist.id == eval(data).get("id"),
                                    "update_data": eval(data)}
                self.OpOr.update_data(update_data_dict)

    def upload(self):
        data = request.data.decode()
        if request.method == 'POST':
            f = request.files['file']
            print(54, f)
            print(54, f.filename)
            upload_path = os.path.join(appdir, r'static\uploads',
                                       secure_filename(f.filename))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
            f.save(upload_path)


if __name__ == '__main__':
    # OpOr = OperateOrm()
    # DA = OpOr.select_all_data(Todolist)
    # print(DA)
    pass
    da = TableAnalysis().readdata()
    print(da)
