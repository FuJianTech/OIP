# !/bin/env python
# -*- coding=utf-8 -*-
from . import application_vue_demo
from flask import jsonify, render_template


@application_vue_demo.route("/vue", methods=['GET'])
def test():
    return render_template('vue_demo.html')
