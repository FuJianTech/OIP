# !/bin/env python
# -*- coding=utf-8 -*-
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from apps.logic import create_app
from apps import little_config


port = int(little_config().get("project_port", 5010))
app = create_app()

if __name__ == '__main__':
    # app.run(debug=False, host='0.0.0.0', port=port)
    app.run(debug=False, host='127.0.0.1', port=port)
