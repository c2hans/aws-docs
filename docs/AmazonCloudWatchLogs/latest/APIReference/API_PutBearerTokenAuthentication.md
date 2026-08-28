---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutBearerTokenAuthentication.html
---

# PutBearerTokenAuthentication
<a name="API_PutBearerTokenAuthentication"></a>

Enables or disables bearer token authentication for the specified log group. When enabled on a log group, bearer token authentication is enabled on operations until it is explicitly disabled.

For information about the parameters that are common to all actions, see [Common Parameters](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/CommonParameters.html).

## Request Syntax
<a name="API_PutBearerTokenAuthentication_RequestSyntax"></a>

```
{
   "bearerTokenAuthenticationEnabled": {{boolean}},
   "logGroupIdentifier": "{{string}}"
}
```

## Request Parameters
<a name="API_PutBearerTokenAuthentication_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [bearerTokenAuthenticationEnabled](#API_PutBearerTokenAuthentication_RequestSyntax) **   <a name="CWL-PutBearerTokenAuthentication-request-bearerTokenAuthenticationEnabled"></a>
Whether to enable bearer token authentication.
Type: Boolean
Required: Yes
Type: Boolean
Required: Yes

 ** [logGroupIdentifier](#API_PutBearerTokenAuthentication_RequestSyntax) **   <a name="CWL-PutBearerTokenAuthentication-request-logGroupIdentifier"></a>
The name or ARN of the log group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: Yes
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w#+=/:,.@-]*`
Required: Yes

## Response Elements
<a name="API_PutBearerTokenAuthentication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutBearerTokenAuthentication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** InvalidOperationException **
The operation is not valid on the specified resource.
HTTP Status Code: 400

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
<a name="API_PutBearerTokenAuthentication_Examples"></a>

### Sample Request
<a name="API_PutBearerTokenAuthentication_Example_1"></a>

This example illustrates one usage of PutBearerTokenAuthentication.

#### Sample Request
<a name="API_PutBearerTokenAuthentication_Example_1_Request"></a>

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
          X-Amz-Target: Logs_20140328.PutBearerTokenAuthentication
          {
          "logGroupIdentifier": "my-log-group",
          "bearerTokenAuthenticationEnabled": true
          }
```

#### Sample Response
<a name="API_PutBearerTokenAuthentication_Example_1_Response"></a>

```
HTTP/1.1 200 OK
          x-amzn-RequestId: <RequestId>
          Content-Type: application/x-amz-json-1.1
          Content-Length: 0
          Date: <Date>
```

## See Also
<a name="API_PutBearerTokenAuthentication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/PutBearerTokenAuthentication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/PutBearerTokenAuthentication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/PutBearerTokenAuthentication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/PutBearerTokenAuthentication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/PutBearerTokenAuthentication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/PutBearerTokenAuthentication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/PutBearerTokenAuthentication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/PutBearerTokenAuthentication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/PutBearerTokenAuthentication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/PutBearerTokenAuthentication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
