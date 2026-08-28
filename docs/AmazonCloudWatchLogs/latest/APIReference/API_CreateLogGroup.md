---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.html
---

# CreateLogGroup
<a name="API_CreateLogGroup"></a>

Creates a log group with the specified name. You can create up to 1,000,000 log groups per Region per account.

You must use the following guidelines when naming a log group:
+ Log group names must be unique within a Region for an AWS account.
+ Log group names can be between 1 and 512 characters long.
+ Log group names consist of the following characters: a-z, A-Z, 0-9, '\_' (underscore), '-' (hyphen), '/' (forward slash), '.' (period), and '\#' (number sign)
+ Log group names can't start with the string `aws/`

When you create a log group, by default the log events in the log group do not expire. To set a retention policy so that events expire and are deleted after a specified time, use [PutRetentionPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutRetentionPolicy.html).

If you associate an AWS KMS key with the log group, ingested data is encrypted using the KMS key. This association is stored as long as the data encrypted with the KMS key is still within CloudWatch Logs. This enables CloudWatch Logs to decrypt this data whenever it is requested.

If you attempt to associate a KMS key with the log group but the KMS key does not exist or the KMS key is disabled, you receive an `InvalidParameterException` error.

**Important**
CloudWatch Logs supports only symmetric KMS keys. Do not associate an asymmetric KMS key with your log group. For more information, see [Using Symmetric and Asymmetric Keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html).

## Request Syntax
<a name="API_CreateLogGroup_RequestSyntax"></a>

```
{
   "deletionProtectionEnabled": {{boolean}},
   "kmsKeyId": "{{string}}",
   "logGroupClass": "{{string}}",
   "logGroupName": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateLogGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deletionProtectionEnabled](#API_CreateLogGroup_RequestSyntax) **   <a name="CWL-CreateLogGroup-request-deletionProtectionEnabled"></a>
Use this parameter to enable deletion protection for the new log group. When enabled on a log group, deletion protection blocks all deletion operations until it is explicitly disabled. By default log groups are created without deletion protection enabled.
Type: Boolean
Required: No

 ** [kmsKeyId](#API_CreateLogGroup_RequestSyntax) **   <a name="CWL-CreateLogGroup-request-kmsKeyId"></a>
The Amazon Resource Name (ARN) of the KMS key to use when encrypting log data. For more information, see [Amazon Resource Names](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kms).
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [logGroupClass](#API_CreateLogGroup_RequestSyntax) **   <a name="CWL-CreateLogGroup-request-logGroupClass"></a>
Use this parameter to specify the log group class for this log group. There are three classes:
+ The `Standard` log class supports all CloudWatch Logs features.
+ The `Infrequent Access` log class supports a subset of CloudWatch Logs features and incurs lower costs.
+ Use the `Delivery` log class only for delivering AWS Lambda logs to store in Amazon S3 or Amazon Data Firehose. Log events in log groups in the Delivery class are kept in CloudWatch Logs for only one day. This log class doesn't offer rich CloudWatch Logs capabilities such as CloudWatch Logs Insights queries.
If you omit this parameter, the default of `STANDARD` is used.
The value of `logGroupClass` can't be changed after a log group is created.
For details about the features supported by each class, see [Log classes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html)
Type: String
Valid Values: `STANDARD | INFREQUENT_ACCESS | DELIVERY`
Required: No

 ** [logGroupName](#API_CreateLogGroup_RequestSyntax) **   <a name="CWL-CreateLogGroup-request-logGroupName"></a>
A name for the log group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: Yes

 ** [tags](#API_CreateLogGroup_RequestSyntax) **   <a name="CWL-CreateLogGroup-request-tags"></a>
The key-value pairs to use for the tags.
You can grant users access to certain log groups while preventing them from accessing other log groups. To do so, tag your groups and use IAM policies that refer to those tags. To assign tags when you create a log group, you must have either the `logs:TagResource` or `logs:TagLogGroup` permission. For more information about tagging, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html). For more information about using tags to control access, see [Controlling access to Amazon Web Services resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html).
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]+)$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Elements
<a name="API_CreateLogGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateLogGroup_Errors"></a>

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

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## Examples
<a name="API_CreateLogGroup_Examples"></a>

### To create a log group
<a name="API_CreateLogGroup_Example_1"></a>

The following example creates a log group.

#### Sample Request
<a name="API_CreateLogGroup_Example_1_Request"></a>

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
X-Amz-Target: Logs_20140328.CreateLogGroup
{
  "logGroupName": "my-log-group",
  "kmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/abcd1234-a123-456a-a12b-a123b456c789"
}
```

#### Sample Response
<a name="API_CreateLogGroup_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

## See Also
<a name="API_CreateLogGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/CreateLogGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/CreateLogGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/CreateLogGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/CreateLogGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/CreateLogGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/CreateLogGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/CreateLogGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/CreateLogGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/CreateLogGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/CreateLogGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
