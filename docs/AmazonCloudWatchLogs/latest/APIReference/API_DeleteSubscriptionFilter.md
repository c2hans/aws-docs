---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteSubscriptionFilter.html
---

# DeleteSubscriptionFilter
<a name="API_DeleteSubscriptionFilter"></a>

Deletes the specified subscription filter.

## Request Syntax
<a name="API_DeleteSubscriptionFilter_RequestSyntax"></a>

```
{
   "filterName": "{{string}}",
   "logGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteSubscriptionFilter_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filterName](#API_DeleteSubscriptionFilter_RequestSyntax) **   <a name="CWL-DeleteSubscriptionFilter-request-filterName"></a>
The name of the subscription filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:*]*`
Required: Yes

 ** [logGroupName](#API_DeleteSubscriptionFilter_RequestSyntax) **   <a name="CWL-DeleteSubscriptionFilter-request-logGroupName"></a>
The name of the log group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: Yes

## Response Elements
<a name="API_DeleteSubscriptionFilter_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteSubscriptionFilter_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** OperationAbortedException **
Multiple concurrent requests to update the same resource were in conflict.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## Examples
<a name="API_DeleteSubscriptionFilter_Examples"></a>

### To delete a subscription filter
<a name="API_DeleteSubscriptionFilter_Example_1"></a>

The following example deletes the specified subscription filter for the specified log group.

#### Sample Request
<a name="API_DeleteSubscriptionFilter_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: logs.<region>.<domain>
X-Amz-Date: <DATE>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Accept: application/json
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: Logs_20140328.DeleteSubscriptionFilter
{
  "logGroupName": "my-log-group",
  "filterName": "my-subscription-filter"
}
```

#### Sample Response
<a name="API_DeleteSubscriptionFilter_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

## See Also
<a name="API_DeleteSubscriptionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/DeleteSubscriptionFilter)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/DeleteSubscriptionFilter)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DeleteSubscriptionFilter)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/DeleteSubscriptionFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DeleteSubscriptionFilter)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/DeleteSubscriptionFilter)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/DeleteSubscriptionFilter)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/DeleteSubscriptionFilter)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/DeleteSubscriptionFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DeleteSubscriptionFilter)
