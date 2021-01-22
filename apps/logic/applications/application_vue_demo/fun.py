# !/bin/env python
# -*- coding=utf-8 -*-

# from apps.logic.applications.application_vue_demo.database.model import *

from flask import request, render_template, jsonify
import shutil
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

    def get_upload_path(self):
        from apps import appdir
        return os.path.join(appdir, "upload")

    def upload_pic(self):
        print(57)
        data_dict = eval(request.data.decode())
        print(59, data_dict)
        id = data_dict.get('id')
        temp = data_dict.get('temp')
        update_data_dict = {"table": Todolist, "filters": Todolist.id == id,
                            "update_data": {'pic_path': temp}}
        self.OpOr.update_data(update_data_dict)

        return '成功'

    def upload_timestemp(self):
        data = request.data.decode()
        import uuid

        abs_path = ''
        if request.method == 'POST':
            path = self.get_upload_path()
            f = request.files
            timestamp = str(uuid.uuid1().hex)
            for key, value in f.items():
                abs_path = os.path.join(path, timestamp)
                if not os.path.exists(abs_path):
                    os.makedirs(abs_path)
            for key, value in f.items():
                _, name = os.path.split(value.filename)
                fil=open(os.path.join(abs_path, name), "wb")
                fil.write(value.stream.read())
                fil.close()
            shutil.copy(os.path.join(abs_path, name),os.path.join(appdir, f'static{os.sep}uploads{os.sep}images{os.sep}{name}'))
            return timestamp



if __name__ == '__main__':
    # OpOr = OperateOrm()
    # DA = OpOr.select_all_data(Todolist)
    # print(DA)
    pass
    da=TableAnalysis().readdata()
    print(da)
