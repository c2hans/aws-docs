---
source_url: https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway-errors.html
---

# Handling Lambda errors with an API Gateway API
<a name="services-apigateway-errors"></a>

API Gateway treats all invocation and function errors as internal errors. If the Lambda API rejects the invocation request, API Gateway returns a 500 error code. If the function runs but returns an error, or returns a response in the wrong format, API Gateway returns a 502. In both cases, the body of the response from API Gateway is `{"message": "Internal server error"}`.

**Note**
API Gateway does not retry any Lambda invocations. If Lambda returns an error, API Gateway returns an error response to the client.

The following example shows an X-Ray trace map for a request that resulted in a function error and a 502 from API Gateway. The client receives the generic error message.

![Trace map for a function error with API Gateway.](http://docs.aws.amazon.com/lambda/latest/dg/images/tracemap-apig-502.png)

To customize the error response, you must catch errors in your code and format a response in the required format.

**Example [index.mjs](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/nodejs-apig/function/index.mjs) – Error formatting**

```
var formatError = function(error){
  var response = {
    "statusCode": error.statusCode,
    "headers": {
      "Content-Type": "text/plain",
      "x-amzn-ErrorType": error.code
    },
    "isBase64Encoded": false,
    "body": error.code + ": " + error.message
  }
  return response
}
```

API Gateway converts this response into an HTTP error with a custom status code and body. In the trace map, the function node is green because it handled the error.

![Trace map for a formatted error with API Gateway.](http://docs.aws.amazon.com/lambda/latest/dg/images/tracemap-apig-404.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
