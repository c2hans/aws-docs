---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateExportTask.html
---

# CreateExportTask
<a name="API_CreateExportTask"></a>

Creates an export task so that you can efficiently export data from a log group to an Amazon S3 bucket. When you perform a `CreateExportTask` operation, you must use credentials that have permission to write to the S3 bucket that you specify as the destination.

Exporting log data to S3 buckets that are encrypted by AWS KMS is supported. Exporting log data to Amazon S3 buckets that have S3 Object Lock enabled with a retention period is also supported.

Exporting to S3 buckets that are encrypted with AES-256 is supported.

This is an asynchronous call. If all the required information is provided, this operation initiates an export task and responds with the ID of the task. After the task has started, you can use [DescribeExportTasks](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeExportTasks.html) to get the status of the export task. Each account can only have one active (`RUNNING` or `PENDING`) export task at a time. To cancel an export task, use [CancelExportTask](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CancelExportTask.html).

You can export logs from multiple log groups or multiple time ranges to the same S3 bucket. To separate log data for each export task, specify a prefix to be used as the Amazon S3 key prefix for all exported objects.

**Note**
We recommend that you don't regularly export to Amazon S3 as a way to continuously archive your logs. For that use case, we instead recommend that you use subscriptions. For more information about subscriptions, see [Real-time processing of log data with subscriptions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscriptions.html).

**Note**
Time-based sorting on chunks of log data inside an exported file is not guaranteed. You can sort the exported log field data by using Linux utilities.

## Request Syntax
<a name="API_CreateExportTask_RequestSyntax"></a>

```
{
   "destination": "{{string}}",
   "destinationPrefix": "{{string}}",
   "from": {{number}},
   "logGroupName": "{{string}}",
   "logStreamNamePrefix": "{{string}}",
   "taskName": "{{string}}",
   "to": {{number}}
}
```

## Request Parameters
<a name="API_CreateExportTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [destination](#API_CreateExportTask_RequestSyntax) **   <a name="CWL-CreateExportTask-request-destination"></a>
The name of S3 bucket for the exported log data. The bucket must be in the same AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** [destinationPrefix](#API_CreateExportTask_RequestSyntax) **   <a name="CWL-CreateExportTask-request-destinationPrefix"></a>
The prefix used as the start of the key for every object exported. If you don't specify a value, the default is `exportedlogs`.
The length of this parameter must comply with the S3 object key name length limits. The object key name is a sequence of Unicode characters with UTF-8 encoding, and can be up to 1,024 bytes.
Type: String
Required: No

 ** [from](#API_CreateExportTask_RequestSyntax) **   <a name="CWL-CreateExportTask-request-from"></a>
The start time of the range for the request, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC`. Events with a timestamp earlier than this time are not exported.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** [logGroupName](#API_CreateExportTask_RequestSyntax) **   <a name="CWL-CreateExportTask-request-logGroupName"></a>
The name of the log group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: Yes

 ** [logStreamNamePrefix](#API_CreateExportTask_RequestSyntax) **   <a name="CWL-CreateExportTask-request-logStreamNamePrefix"></a>
Export only log streams that match the provided prefix. If you don't specify a value, no prefix filter is applied.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:*]*`
Required: No

 ** [taskName](#API_CreateExportTask_RequestSyntax) **   <a name="CWL-CreateExportTask-request-taskName"></a>
The name of the export task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [to](#API_CreateExportTask_RequestSyntax) **   <a name="CWL-CreateExportTask-request-to"></a>
The end time of the range for the request, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC`. Events with a timestamp later than this time are not exported.
You must specify a time that is not earlier than when this log group was created.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

## Response Syntax
<a name="API_CreateExportTask_ResponseSyntax"></a>

```
{
   "taskId": "string"
}
```

## Response Elements
<a name="API_CreateExportTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [taskId](#API_CreateExportTask_ResponseSyntax) **   <a name="CWL-CreateExportTask-response-taskId"></a>
The ID of the export task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

## Errors
<a name="API_CreateExportTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** LimitExceededException **
You have reached the maximum number of resources that can be created.
HTTP Status Code: 400

 ** OperationAbortedException **
Multiple concurrent requests to update the same resource were in conflict.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The specified resource already exists.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## Examples
<a name="API_CreateExportTask_Examples"></a>

### To create an export task
<a name="API_CreateExportTask_Example_1"></a>

The following example creates an export task that exports data from a log group to an S3 bucket.

#### Sample Request
<a name="API_CreateExportTask_Example_1_Request"></a>

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
X-Amz-Target: Logs_20140328.CreateExportTask
{
  "taskName": "my-task",
  "logGroupName": "my-log-group",
  "from": 1437584472382,
  "to": 1437584472833,
  "destination": "my-destination",
  "destinationPrefix": "my-prefix"
}
```

#### Sample Response
<a name="API_CreateExportTask_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "taskId": "exampleTaskId"
}
```

## See Also
<a name="API_CreateExportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/CreateExportTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/CreateExportTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/CreateExportTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/CreateExportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/CreateExportTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/CreateExportTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/CreateExportTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/CreateExportTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/CreateExportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/CreateExportTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
