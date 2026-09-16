---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_ReportTaskRunnerHeartbeat.html
---

# ReportTaskRunnerHeartbeat
<a name="API_ReportTaskRunnerHeartbeat"></a>

Task runners call `ReportTaskRunnerHeartbeat` every 15 minutes to indicate that they are operational. If the AWS Data Pipeline Task Runner is launched on a resource managed by AWS Data Pipeline, the web service can use this call to detect when the task runner application has failed and restart a new instance.

## Request Syntax
<a name="API_ReportTaskRunnerHeartbeat_RequestSyntax"></a>

```
{
   "hostname": "{{string}}",
   "taskrunnerId": "{{string}}",
   "workerGroup": "{{string}}"
}
```

## Request Parameters
<a name="API_ReportTaskRunnerHeartbeat_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [hostname](#API_ReportTaskRunnerHeartbeat_RequestSyntax) **   <a name="DP-ReportTaskRunnerHeartbeat-request-hostname"></a>
The public DNS name of the task runner.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: No

 ** [taskrunnerId](#API_ReportTaskRunnerHeartbeat_RequestSyntax) **   <a name="DP-ReportTaskRunnerHeartbeat-request-taskrunnerId"></a>
The ID of the task runner. This value should be unique across your AWS account. In the case of AWS Data Pipeline Task Runner launched on a resource managed by AWS Data Pipeline, the web service provides a unique identifier when it launches the application. If you have written a custom task runner, you should assign a unique identifier for the task runner.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: Yes

 ** [workerGroup](#API_ReportTaskRunnerHeartbeat_RequestSyntax) **   <a name="DP-ReportTaskRunnerHeartbeat-request-workerGroup"></a>
The type of task the task runner is configured to accept and process. The worker group is set as a field on objects in the pipeline when they are created. You can only specify a single value for `workerGroup`. There are no wildcard values permitted in `workerGroup`; the string must be an exact, case-sensitive, match.
Type: String
Required: No

## Response Syntax
<a name="API_ReportTaskRunnerHeartbeat_ResponseSyntax"></a>

```
{
   "terminate": boolean
}
```

## Response Elements
<a name="API_ReportTaskRunnerHeartbeat_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [terminate](#API_ReportTaskRunnerHeartbeat_ResponseSyntax) **   <a name="DP-ReportTaskRunnerHeartbeat-response-terminate"></a>
Indicates whether the calling task runner should terminate.
Type: Boolean

## Errors
<a name="API_ReportTaskRunnerHeartbeat_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
An internal service error occurred.
 ** message **
Description of the error message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.
 ** message **
Description of the error message.
HTTP Status Code: 400

## Examples
<a name="API_ReportTaskRunnerHeartbeat_Examples"></a>

### Example
<a name="API_ReportTaskRunnerHeartbeat_Example_1"></a>

This example illustrates one usage of ReportTaskRunnerHeartbeat.

#### Sample Request
<a name="API_ReportTaskRunnerHeartbeat_Example_1_Request"></a>

```

POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: DataPipeline.ReportTaskRunnerHeartbeat
Content-Length: 84
Host: datapipeline.us-east-1.amazonaws.com
X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT
Authorization: AuthParams

{"taskrunnerId": "1234567890",
 "workerGroup": "wg-12345",
 "hostname": "example.com"}
```

#### Sample Response
<a name="API_ReportTaskRunnerHeartbeat_Example_1_Response"></a>

```
Status:
x-amzn-RequestId: b3104dc5-0734-11e2-af6f-6bc7a6be60d9
Content-Type: application/x-amz-json-1.1
Content-Length: 20
Date: Mon, 12 Nov 2012 17:50:53 GMT

{"terminate": false}
```

## See Also
<a name="API_ReportTaskRunnerHeartbeat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datapipeline-2012-10-29/ReportTaskRunnerHeartbeat)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datapipeline-2012-10-29/ReportTaskRunnerHeartbeat)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/ReportTaskRunnerHeartbeat)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datapipeline-2012-10-29/ReportTaskRunnerHeartbeat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/ReportTaskRunnerHeartbeat)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datapipeline-2012-10-29/ReportTaskRunnerHeartbeat)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datapipeline-2012-10-29/ReportTaskRunnerHeartbeat)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datapipeline-2012-10-29/ReportTaskRunnerHeartbeat)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datapipeline-2012-10-29/ReportTaskRunnerHeartbeat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/ReportTaskRunnerHeartbeat)
