---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_ListFunctionEventInvokeConfigs.html
---

# ListFunctionEventInvokeConfigs
<a name="API_ListFunctionEventInvokeConfigs"></a>

Retrieves a list of configurations for asynchronous invocation for a function.

To configure options for asynchronous invocation, use [PutFunctionEventInvokeConfig](API_PutFunctionEventInvokeConfig.md).

## Request Syntax
<a name="API_ListFunctionEventInvokeConfigs_RequestSyntax"></a>

```
GET /2019-09-25/functions/{{FunctionName}}/event-invoke-config/list?Marker={{Marker}}&MaxItems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListFunctionEventInvokeConfigs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FunctionName](#API_ListFunctionEventInvokeConfigs_RequestSyntax) **   <a name="lambda-ListFunctionEventInvokeConfigs-request-uri-FunctionName"></a>
The name or ARN of the Lambda function.

**Name formats**
+  **Function name** - `my-function`.
+  **Function ARN** - `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
+  **Partial ARN** - `123456789012:function:my-function`.
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_\.]+)(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`
Required: Yes

 ** [Marker](#API_ListFunctionEventInvokeConfigs_RequestSyntax) **   <a name="lambda-ListFunctionEventInvokeConfigs-request-uri-Marker"></a>
Specify the pagination token that's returned by a previous request to retrieve the next page of results.

 ** [MaxItems](#API_ListFunctionEventInvokeConfigs_RequestSyntax) **   <a name="lambda-ListFunctionEventInvokeConfigs-request-uri-MaxItems"></a>
The maximum number of configurations to return.
Valid Range: Minimum value of 1. Maximum value of 50.

## Request Body
<a name="API_ListFunctionEventInvokeConfigs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListFunctionEventInvokeConfigs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "FunctionEventInvokeConfigs": [
      {
         "DestinationConfig": {
            "OnFailure": {
               "Destination": "string"
            },
            "OnSuccess": {
               "Destination": "string"
            }
         },
         "FunctionArn": "string",
         "LastModified": number,
         "MaximumEventAgeInSeconds": number,
         "MaximumRetryAttempts": number
      }
   ],
   "NextMarker": "string"
}
```

## Response Elements
<a name="API_ListFunctionEventInvokeConfigs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FunctionEventInvokeConfigs](#API_ListFunctionEventInvokeConfigs_ResponseSyntax) **   <a name="lambda-ListFunctionEventInvokeConfigs-response-FunctionEventInvokeConfigs"></a>
A list of configurations.
Type: Array of [FunctionEventInvokeConfig](API_FunctionEventInvokeConfig.md) objects

 ** [NextMarker](#API_ListFunctionEventInvokeConfigs_ResponseSyntax) **   <a name="lambda-ListFunctionEventInvokeConfigs-response-NextMarker"></a>
The pagination token that's included if more results are available.
Type: String

## Errors
<a name="API_ListFunctionEventInvokeConfigs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource specified in the request does not exist.
HTTP Status Code: 404

 ** ServiceException **
The AWS Lambda service encountered an internal error.
HTTP Status Code: 500

 ** TooManyRequestsException **
The request throughput limit was exceeded. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests).
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 429

## See Also
<a name="API_ListFunctionEventInvokeConfigs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/ListFunctionEventInvokeConfigs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/ListFunctionEventInvokeConfigs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/ListFunctionEventInvokeConfigs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/ListFunctionEventInvokeConfigs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/ListFunctionEventInvokeConfigs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/ListFunctionEventInvokeConfigs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/ListFunctionEventInvokeConfigs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/ListFunctionEventInvokeConfigs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/ListFunctionEventInvokeConfigs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/ListFunctionEventInvokeConfigs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
