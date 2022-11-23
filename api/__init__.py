import logging
import random
import time

import requests
from flask import Flask, has_request_context, request
from structlog import contextvars

from api.utilities.logger import logger

app = Flask(__name__)


def set_context(*args, **kw):
    start_time = time.perf_counter_ns()
    logger.info("request to received")
    if has_request_context():
        contextvars.bind_contextvars(
            request_method=request.method,
            request_url_rule=str(request.url_rule),
            request_path=str(request.path),
            request_start_time=start_time,
        )


def log_result(response):
    end_time = time.perf_counter_ns()
    ctx = contextvars.get_contextvars()
    start_time = ctx.get("request_start_time")
    execution_time = int((end_time - start_time) / 1000)
    logger.debug(
        "request done",
        status=response.status_code,
        execution_time=execution_time,
        time_measure="microseconds",
    )
    return response


app.before_request(set_context)
app.after_request(log_result)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/users/<id>")
def get_user(id):
    contextvars.bind_contextvars(user_id=id)
    return f"the user id is , {id}!"


@app.route("/request_method/<method>")
def get_request(method):
    contextvars.bind_contextvars(method=method)
    url = f"https://httpbin.org/{method}"
    headers = {"Accept": "application/json"}
    response = "hi"
    try:
        response = requests.get(url, headers=headers).json()
        logger.info("got response", response=response, url=url)
    except Exception as e:
        logger.error("error in request ", e=e)

    return response


@app.route("/request_code/<code>")
def get_status_request(code):
    contextvars.bind_contextvars(code=code)
    url = f"https://httpbin.org/status/{code}"
    headers = {"Accept": "application/json"}
    response = "hi"
    try:
        response = requests.get(url, headers=headers).headers
        logger.info("got response", response=response, url=url)
    except Exception as e:
        logger.error("error in request ", e=e)
        response = {"error": str(e)}

    return dict(response)


@app.route("/random_err/")
def throw_error():
    error_list = [KeyError, TypeError, Exception, ReferenceError, RuntimeError]
    raise random.choice(error_list)

    return ""


@app.errorhandler(Exception)
def catch_err(err):
    logger.exception("request failed", err=err)
    return "system failed", 500
