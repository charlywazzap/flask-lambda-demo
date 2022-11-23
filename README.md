# python-flask-api-with-apigateway-base

use this as a sample base flask API

## local api

`pipenv shell`

`pipenv run dev`

## test api

`pipenv run test`

`pipenv run format_ci`

`pipenv run sort_ci`

## lambda + api proxy test

`pipenv run test_lambda`

Sample output

```
[root - INFO - 2022-08-30 10:07:27,284] Event: {'body': '{"test":"body"}', 'resource': '/{proxy+}', 'path': '/', 'httpMethod': 'GET', 'isBase64Encoded': True, 'queryStringParameters': {'foo': 'bar'}, 'multiValueQueryStringParameters': {'foo': ['bar']}, 'pathParameters': {'proxy': '/'}, 'stageVariables': {'baz': 'qux'}, 'headers': {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'en-US,en;q=0.8', 'Cache-Control': 'max-age=0', 'CloudFront-Forwarded-Proto': 'https', 'CloudFront-Is-Desktop-Viewer': 'true', 'CloudFront-Is-Mobile-Viewer': 'false', 'CloudFront-Is-SmartTV-Viewer': 'false', 'CloudFront-Is-Tablet-Viewer': 'false', 'CloudFront-Viewer-Country': 'US', 'Host': '1234567890.execute-api.us-east-1.amazonaws.com', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Custom User Agent String', 'Via': '1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)', 'X-Amz-Cf-Id': 'cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA==', 'X-Forwarded-For': '127.0.0.1, 127.0.0.2', 'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https'}, 'multiValueHeaders': {'Accept': ['text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'], 'Accept-Encoding': ['gzip, deflate, sdch'], 'Accept-Language': ['en-US,en;q=0.8'], 'Cache-Control': ['max-age=0'], 'CloudFront-Forwarded-Proto': ['https'], 'CloudFront-Is-Desktop-Viewer': ['true'], 'CloudFront-Is-Mobile-Viewer': ['false'], 'CloudFront-Is-SmartTV-Viewer': ['false'], 'CloudFront-Is-Tablet-Viewer': ['false'], 'CloudFront-Viewer-Country': ['US'], 'Host': ['0123456789.execute-api.us-east-1.amazonaws.com'], 'Upgrade-Insecure-Requests': ['1'], 'User-Agent': ['Custom User Agent String'], 'Via': ['1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)'], 'X-Amz-Cf-Id': ['cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA=='], 'X-Forwarded-For': ['127.0.0.1, 127.0.0.2'], 'X-Forwarded-Port': ['443'], 'X-Forwarded-Proto': ['https']}, 'requestContext': {'accountId': '123456789012', 'resourceId': '123456', 'stage': 'prod', 'requestId': 'c6af9ac6-7b61-11e6-9a41-93e8deadbeef', 'requestTime': '09/Apr/2015:12:34:56 +0000', 'requestTimeEpoch': 1428582896000, 'identity': {'cognitoIdentityPoolId': None, 'accountId': None, 'cognitoIdentityId': None, 'caller': None, 'accessKey': None, 'sourceIp': '127.0.0.1', 'cognitoAuthenticationType': None, 'cognitoAuthenticationProvider': None, 'userArn': None, 'userAgent': 'Custom User Agent String', 'user': None}, 'path': '/', 'resourcePath': '/{proxy+}', 'httpMethod': 'GET', 'apiId': '1234567890', 'protocol': 'HTTP/1.1'}}
[root - INFO - 2022-08-30 10:07:27,284] START RequestId: 64b4d4cf-905f-444c-87b5-cf5aff12fbb6 Version: 
[root - INFO - 2022-08-30 10:07:27,491] END RequestId: 64b4d4cf-905f-444c-87b5-cf5aff12fbb6
[root - INFO - 2022-08-30 10:07:27,491] REPORT RequestId: 64b4d4cf-905f-444c-87b5-cf5aff12fbb6  Duration: 0.24 ms
[root - INFO - 2022-08-30 10:07:27,491] RESULT:
{'statusCode': 200, 'multiValueHeaders': {'Content-Type': ['text/html; charset=utf-8'], 'Content-Length': ['13']}, 'body': 'Hello, World!', 'isBase64Encoded': False}
```
