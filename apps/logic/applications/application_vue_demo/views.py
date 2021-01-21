# !/bin/env python
# -*- coding=utf-8 -*-
from . import application_vue_demo
from flask import jsonify, render_template
import sqlite3 as sql
from .fun import TableAnalysis


@application_vue_demo.route("/vue_demo", methods=['GET'])
def vue_demo():
    return render_template('vue_demo.html')


@application_vue_demo.route('/readdata')
def readdata():
    try:
        TA = TableAnalysis()
        result = TA.readdata()
        return jsonify({"rescode": 0, "resmsg": "查询成功", "data":result})
    except Exception as ex:
        return jsonify({"rescode": -1, "resmsg": f"{ex}"})


@application_vue_demo.route('/submit', methods=['GET', 'POST'])
def submit():
    try:
        TA = TableAnalysis()
        result = TA.submit()
        return jsonify({"rescode": 0, "resmsg": "添加成功", "data":""})
    except Exception as ex:
        return jsonify({"rescode": -1, "resmsg": f"{ex}"})


@application_vue_demo.route('/deletedata', methods=['GEt', 'POST'])
def deletedata():
    try:
        TA = TableAnalysis()
        result = TA.delectdata()
        return jsonify({"rescode": 0, "resmsg": "查询成功", "data":result})
    except Exception as ex:
        return jsonify({"rescode": -1, "resmsg": f"{ex}"})


@application_vue_demo.route('/update', methods=['GET', 'POST'])
def update():
    try:
        TA = TableAnalysis()
        result = TA.update()
        return jsonify({"rescode": 0, "resmsg": "查询成功", "data":result})
    except Exception as ex:
        return jsonify({"rescode": -1, "resmsg": f"{ex}"})

@application_vue_demo.route('/upload', methods=['GET', 'POST'])
def upload():
    try:
        TA = TableAnalysis()
        result = TA.upload()
        return jsonify({"rescode": 0, "resmsg": "上传成功", "data":result})
    except Exception as ex:
        return jsonify({"rescode": -1, "resmsg": f"{ex}"})