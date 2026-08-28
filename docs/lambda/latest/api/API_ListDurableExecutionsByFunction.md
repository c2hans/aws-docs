---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_ListDurableExecutionsByFunction.html
---

# ListDurableExecutionsByFunction
<a name="API_ListDurableExecutionsByFunction"></a>

Returns a list of [durable executions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html) for a specified Lambda function. You can filter the results by execution name, status, and start time range. This API supports pagination for large result sets.

## Request Syntax
<a name="API_ListDurableExecutionsByFunction_RequestSyntax"></a>

```
GET /2025-12-01/functions/{{FunctionName}}/durable-executions?DurableExecutionName={{DurableExecutionName}}&Marker={{Marker}}&MaxItems={{MaxItems}}&Qualifier={{Qualifier}}&ReverseOrder={{ReverseOrder}}&StartedAfter={{StartedAfter}}&StartedBefore={{StartedBefore}}&Statuses={{Statuses}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDurableExecutionsByFunction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DurableExecutionName](#API_ListDurableExecutionsByFunction_RequestSyntax) **   <a name="lambda-ListDurableExecutionsByFunction-request-uri-DurableExecutionName"></a>
Filter executions by name. Only executions with names that matches this string are returned.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`

 ** [FunctionName](#API_ListDurableExecutionsByFunction_RequestSyntax) **   <a name="lambda-ListDurableExecutionsByFunction-request-uri-FunctionName"></a>
The name or ARN of the Lambda function. You can specify a function name, a partial ARN, or a full ARN.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_\.]+)(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`
Required: Yes

 ** [Marker](#API_ListDurableExecutionsByFunction_RequestSyntax) **   <a name="lambda-ListDurableExecutionsByFunction-request-uri-Marker"></a>
Pagination token from a previous request to continue retrieving results.

 ** [MaxItems](#API_ListDurableExecutionsByFunction_RequestSyntax) **   <a name="lambda-ListDurableExecutionsByFunction-request-uri-MaxItems"></a>
Maximum number of executions to return (1-1000). Default is 100.
Valid Range: Minimum value of 0. Maximum value of 1000.

 ** [Qualifier](#API_ListDurableExecutionsByFunction_RequestSyntax) **   <a name="lambda-ListDurableExecutionsByFunction-request-uri-Qualifier"></a>
The function version or alias. If not specified, lists executions for the $LATEST version.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\$(LATEST(\.PUBLISHED)?)|[a-zA-Z0-9-_$]+`

 ** [ReverseOrder](#API_ListDurableExecutionsByFunction_RequestSyntax) **   <a name="lambda-ListDurableExecutionsByFunction-request-uri-ReverseOrder"></a>
Set to true to return results in chronological order (oldest first). Default is false.

 ** [StartedAfter](#API_ListDurableExecutionsByFunction_RequestSyntax) **   <a name="lambda-ListDurableExecutionsByFunction-request-uri-StartedAfter"></a>
Filter executions that started after this timestamp (ISO 8601 format).

 ** [StartedBefore](#API_ListDurableExecutionsByFunction_RequestSyntax) **   <a name="lambda-ListDurableExecutionsByFunction-request-uri-StartedBefore"></a>
Filter executions that started before this timestamp (ISO 8601 format).

 ** [Statuses](#API_ListDurableExecutionsByFunction_RequestSyntax) **   <a name="lambda-ListDurableExecutionsByFunction-request-uri-Statuses"></a>
Filter executions by status. Valid values: RUNNING, SUCCEEDED, FAILED, TIMED\_OUT, STOPPED.
Array Members: Fixed number of 1 item.
Valid Values: `RUNNING | SUCCEEDED | FAILED | TIMED_OUT | STOPPED`

## Request Body
<a name="API_ListDurableExecutionsByFunction_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDurableExecutionsByFunction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DurableExecutions": [
      {
         "DurableExecutionArn": "string",
         "DurableExecutionName": "string",
         "EndTimestamp": number,
         "FunctionArn": "string",
         "KMSKeyArn": "string",
         "StartTimestamp": number,
         "Status": "string"
      }
   ],
   "NextMarker": "string"
}
```

## Response Elements
<a name="API_ListDurableExecutionsByFunction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DurableExecutions](#API_ListDurableExecutionsByFunction_ResponseSyntax) **   <a name="lambda-ListDurableExecutionsByFunction-response-DurableExecutions"></a>
List of durable execution summaries matching the filter criteria.
Type: Array of [Execution](API_Execution.md) objects

 ** [NextMarker](#API_ListDurableExecutionsByFunction_ResponseSyntax) **   <a name="lambda-ListDurableExecutionsByFunction-response-NextMarker"></a>
Pagination token for retrieving additional results. Present only if there are more results available.
Type: String

## Errors
<a name="API_ListDurableExecutionsByFunction_Errors"></a>

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
<a name="API_ListDurableExecutionsByFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/ListDurableExecutionsByFunction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/ListDurableExecutionsByFunction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/ListDurableExecutionsByFunction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/ListDurableExecutionsByFunction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/ListDurableExecutionsByFunction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/ListDurableExecutionsByFunction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/ListDurableExecutionsByFunction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/ListDurableExecutionsByFunction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/ListDurableExecutionsByFunction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/ListDurableExecutionsByFunction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
