---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogGroups.html
---

# DescribeLogGroups
<a name="API_DescribeLogGroups"></a>

Returns information about log groups, including data sources that ingest into each log group. You can return all your log groups or filter the results by prefix. The results are ASCII-sorted by log group name.

CloudWatch Logs doesn't support IAM policies that control access to the `DescribeLogGroups` action by using the `aws:ResourceTag/key-name ` condition key. Other CloudWatch Logs actions do support the use of the `aws:ResourceTag/key-name ` condition key to control access. For more information about using tags to control access, see [Controlling access to Amazon Web Services resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html).

If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account and view data from the linked source accounts. For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html).

## Request Syntax
<a name="API_DescribeLogGroups_RequestSyntax"></a>

```
{
   "accountIdentifiers": [ "{{string}}" ],
   "includeLinkedAccounts": {{boolean}},
   "limit": {{number}},
   "logGroupClass": "{{string}}",
   "logGroupIdentifiers": [ "{{string}}" ],
   "logGroupNamePattern": "{{string}}",
   "logGroupNamePrefix": "{{string}}",
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeLogGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [accountIdentifiers](#API_DescribeLogGroups_RequestSyntax) **   <a name="CWL-DescribeLogGroups-request-accountIdentifiers"></a>
When `includeLinkedAccounts` is set to `true`, use this parameter to specify the list of accounts to search. You can specify as many as 20 account IDs in the array.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** [includeLinkedAccounts](#API_DescribeLogGroups_RequestSyntax) **   <a name="CWL-DescribeLogGroups-request-includeLinkedAccounts"></a>
If you are using a monitoring account, set this to `true` to have the operation return log groups in the accounts listed in `accountIdentifiers`.
If this parameter is set to `true` and `accountIdentifiers` contains a null value, the operation returns all log groups in the monitoring account and all log groups in all source accounts that are linked to the monitoring account.
The default for this parameter is `false`.
Type: Boolean
Required: No

 ** [limit](#API_DescribeLogGroups_RequestSyntax) **   <a name="CWL-DescribeLogGroups-request-limit"></a>
The maximum number of items returned. If you don't specify a value, the default is up to 50 items.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [logGroupClass](#API_DescribeLogGroups_RequestSyntax) **   <a name="CWL-DescribeLogGroups-request-logGroupClass"></a>
Use this parameter to limit the results to only those log groups in the specified log group class. If you omit this parameter, log groups of all classes can be returned.
Specifies the log group class for this log group. There are three classes:
+ The `Standard` log class supports all CloudWatch Logs features.
+ The `Infrequent Access` log class supports a subset of CloudWatch Logs features and incurs lower costs.
+ Use the `Delivery` log class only for delivering AWS Lambda logs to store in Amazon S3 or Amazon Data Firehose. Log events in log groups in the Delivery class are kept in CloudWatch Logs for only one day. This log class doesn't offer rich CloudWatch Logs capabilities such as CloudWatch Logs Insights queries.
For details about the features supported by each class, see [Log classes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html)
Type: String
Valid Values: `STANDARD | INFREQUENT_ACCESS | DELIVERY`
Required: No

 ** [logGroupIdentifiers](#API_DescribeLogGroups_RequestSyntax) **   <a name="CWL-DescribeLogGroups-request-logGroupIdentifiers"></a>
Use this array to filter the list of log groups returned. If you specify this parameter, the only other filter that you can choose to specify is `includeLinkedAccounts`.
If you are using this operation in a monitoring account, you can specify the ARNs of log groups in source accounts and in the monitoring account itself. If you are using this operation in an account that is not a cross-account monitoring account, you can specify only log group names in the same account as the operation.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w#+=/:,.@-]*`
Required: No

 ** [logGroupNamePattern](#API_DescribeLogGroups_RequestSyntax) **   <a name="CWL-DescribeLogGroups-request-logGroupNamePattern"></a>
If you specify a string for this parameter, the operation returns only log groups that have names that match the string based on a case-sensitive substring search. For example, if you specify `DataLogs`, log groups named `DataLogs`, `aws/DataLogs`, and `GroupDataLogs` would match, but `datalogs`, `Data/log/s` and `Groupdata` would not match.
If you specify `logGroupNamePattern` in your request, then only `arn`, `creationTime`, and `logGroupName` are included in the response.
 `logGroupNamePattern` and `logGroupNamePrefix` are mutually exclusive. Only one of these parameters can be passed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]*`
Required: No

 ** [logGroupNamePrefix](#API_DescribeLogGroups_RequestSyntax) **   <a name="CWL-DescribeLogGroups-request-logGroupNamePrefix"></a>
The prefix to match.
 `logGroupNamePrefix` and `logGroupNamePattern` are mutually exclusive. Only one of these parameters can be passed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** [nextToken](#API_DescribeLogGroups_RequestSyntax) **   <a name="CWL-DescribeLogGroups-request-nextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_DescribeLogGroups_ResponseSyntax"></a>

```
{
   "logGroups": [
      {
         "arn": "string",
         "bearerTokenAuthenticationEnabled": boolean,
         "creationTime": number,
         "dataProtectionStatus": "string",
         "deletionProtectionEnabled": boolean,
         "inheritedProperties": [ "string" ],
         "kmsKeyId": "string",
         "logGroupArn": "string",
         "logGroupClass": "string",
         "logGroupName": "string",
         "metricFilterCount": number,
         "retentionInDays": number,
         "storedBytes": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeLogGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [logGroups](#API_DescribeLogGroups_ResponseSyntax) **   <a name="CWL-DescribeLogGroups-response-logGroups"></a>
An array of structures, where each structure contains the information about one log group.
Type: Array of [LogGroup](API_LogGroup.md) objects

 ** [nextToken](#API_DescribeLogGroups_ResponseSyntax) **   <a name="CWL-DescribeLogGroups-response-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DescribeLogGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## Examples
<a name="API_DescribeLogGroups_Examples"></a>

### To list all log groups
<a name="API_DescribeLogGroups_Example_1"></a>

The following example lists all your log groups.

#### Sample Request
<a name="API_DescribeLogGroups_Example_1_Request"></a>

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
X-Amz-Target: Logs_20140328.DescribeLogGroups
```

#### Sample Response
<a name="API_DescribeLogGroups_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "logGroups": [
    {
      "storageBytes": 1048576,
      "arn": "arn:aws:logs:us-east-1:123456789012:log-group:my-log-group-1:*",
      "creationTime": 1393545600000,
      "logGroupName": "my-log-group-1",
      "metricFilterCount": 0,
      "retentionInDays": 14,
      "kmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/abcd1234-a123-456a-a12b-a123b4cd56ef",
      "deletionProtectionEnabled": true
      "bearerTokenAuthenticationEnabled": true
    },
    {
      "storageBytes": 5242880,
      "arn": "arn:aws:logs:us-east-1:123456789012:log-group:my-log-group-2:*",
      "creationTime": 1396224000000,
      "logGroupName": "my-log-group-2",
      "metricFilterCount": 0,
      "retentionInDays": 30,
      "deletionProtectionEnabled": false
      "bearerTokenAuthenticationEnabled": false
    }
  ]
}
```

### To list all of the log groups in a monitoring account and all linked source accounts that have logGroup in their name
<a name="API_DescribeLogGroups_Example_2"></a>

The following example lists all of the log groups in a monitoring account and all linked source accounts that have `logGroup` in their name.

#### Sample Request
<a name="API_DescribeLogGroups_Example_2_Request"></a>

```
{
  "includeLinkedAccounts" : "true",
  "logGroupNamePattern": "logGroup"
}
```

#### Sample Response
<a name="API_DescribeLogGroups_Example_2_Response"></a>

```
{
  "logGroups": [
    {
      "arn": "arn:aws:logs:us-east-1:123456789012:log-group:monitoring-logGroup-1234:*",
      "creationTime": 1393545600000,
      "logGroupName": "monitoring-logGroup-1234"
    },
    {
      "arn": "arn:aws:logs:us-east-1:012345678901:log-group:source-loggroup-5678:*",
      "creationTime": 1396224000000,
      "logGroupName": "source-loggroup-5678"
      }
  ]
}
```

## See Also
<a name="API_DescribeLogGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/DescribeLogGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/DescribeLogGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DescribeLogGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/DescribeLogGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DescribeLogGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/DescribeLogGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/DescribeLogGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/DescribeLogGroups)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/DescribeLogGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DescribeLogGroups)
