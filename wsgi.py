# -*- coding: utf-8 -*-
"""
wsgi.py: Wsgi init
"""

import api

app = api.app

if __name__ == "__main__":
    app.run(host="0.0.0.0")
