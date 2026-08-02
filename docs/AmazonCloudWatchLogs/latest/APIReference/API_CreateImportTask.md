---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateImportTask.html
---

# CreateImportTask
<a name="API_CreateImportTask"></a>

Starts an import from a data source to CloudWatch Log and creates a managed log group as the destination for the imported data. Currently, [CloudTrail Event Data Store](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store.html) is the only supported data source.

The import task must satisfy the following constraints:
+ The specified source must be in an ACTIVE state.
+ The API caller must have permissions to access the data in the provided source and to perform iam:PassRole on the provided import role which has the same permissions, as described below.
+ The provided IAM role must trust the "cloudtrail.amazonaws.com" principal and have the following permissions:
  + cloudtrail:GetEventDataStoreData
  + logs:CreateLogGroup
  + logs:CreateLogStream
  + logs:PutResourcePolicy
  + (If source has an associated AWS KMS Key) kms:Decrypt
  + (If source has an associated AWS KMS Key) kms:GenerateDataKey

  Example IAM policy for provided import role:

   `[ { "Effect": "Allow", "Action": "iam:PassRole", "Resource": "arn:aws:iam::123456789012:role/apiCallerCredentials", "Condition": { "StringLike": { "iam:AssociatedResourceARN": "arn:aws:logs:us-east-1:123456789012:log-group:aws/cloudtrail/f1d45bff-d0e3-4868-b5d9-2eb678aa32fb:*" } } }, { "Effect": "Allow", "Action": [ "cloudtrail:GetEventDataStoreData" ], "Resource": [ "arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/f1d45bff-d0e3-4868-b5d9-2eb678aa32fb" ] }, { "Effect": "Allow", "Action": [ "logs:CreateImportTask", "logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutResourcePolicy" ], "Resource": [ "arn:aws:logs:us-east-1:123456789012:log-group:/aws/cloudtrail/*" ] }, { "Effect": "Allow", "Action": [ "kms:Decrypt", "kms:GenerateDataKey" ], "Resource": [ "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012" ] } ]`
+ If the import source has a customer managed key, the "cloudtrail.amazonaws.com" principal needs permissions to perform kms:Decrypt and kms:GenerateDataKey.
+ There can be no more than 3 active imports per account at a given time.
+ The startEventTime must be less than or equal to endEventTime.
+ The data being imported must be within the specified source's retention period.

## Request Syntax
<a name="API_CreateImportTask_RequestSyntax"></a>

```
{
   "importFilter": {
      "endEventTime": {{number}},
      "startEventTime": {{number}}
   },
   "importRoleArn": "{{string}}",
   "importSourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateImportTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [importFilter](#API_CreateImportTask_RequestSyntax) **   <a name="CWL-CreateImportTask-request-importFilter"></a>
Optional filters to constrain the import by CloudTrail event time. Times are specified in Unix timestamp milliseconds. The range of data being imported must be within the specified source's retention period.
Type: [ImportFilter](API_ImportFilter.md) object
Required: No

 ** [importRoleArn](#API_CreateImportTask_RequestSyntax) **   <a name="CWL-CreateImportTask-request-importRoleArn"></a>
The ARN of the IAM role that grants CloudWatch Logs permission to import from the CloudTrail Lake Event Data Store.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [importSourceArn](#API_CreateImportTask_RequestSyntax) **   <a name="CWL-CreateImportTask-request-importSourceArn"></a>
The ARN of the source to import from.
Type: String
Required: Yes

## Response Syntax
<a name="API_CreateImportTask_ResponseSyntax"></a>

```
{
   "creationTime": number,
   "importDestinationArn": "string",
   "importId": "string"
}
```

## Response Elements
<a name="API_CreateImportTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_CreateImportTask_ResponseSyntax) **   <a name="CWL-CreateImportTask-response-creationTime"></a>
The timestamp when the import task was created, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
Type: Long
Valid Range: Minimum value of 0.

 ** [importDestinationArn](#API_CreateImportTask_ResponseSyntax) **   <a name="CWL-CreateImportTask-response-importDestinationArn"></a>
The ARN of the CloudWatch Logs log group created as the destination for the imported events.
Type: String

 ** [importId](#API_CreateImportTask_ResponseSyntax) **   <a name="CWL-CreateImportTask-response-importId"></a>
A unique identifier for the import task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\-a-zA-Z0-9]+`

## Errors
<a name="API_CreateImportTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** ConflictException **
This operation attempted to create a resource that already exists.
HTTP Status Code: 400

 ** InvalidOperationException **
The operation is not valid on the specified resource.
HTTP Status Code: 400

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 400

 ** ValidationException **
One of the parameters for the request is not valid.
HTTP Status Code: 400

## Examples
<a name="API_CreateImportTask_Examples"></a>

### To create an import task from CloudTrail Lake to CloudWatch Logs
<a name="API_CreateImportTask_Example_1"></a>

The following example creates an import task with time-based filters.

#### Sample Request
<a name="API_CreateImportTask_Example_1_Request"></a>

```
POST / HTTP/1.1
          Host: logs.<region>.<domain>
          X-Amz-Target: Logs_20140328.CreateImportTask
          {
          "importSourceArn": "arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/f1d45bff-d0e3-4868-b5d9-2eb678aa32fb",
          "importRoleArn": "arn:aws:iam::123456789012:role/CloudWatchLogsImportRole",
          "importFilter": {
          "startEventTime": 1640995200000,
          "endEventTime": 1641081600000
          }
          }
```

#### Sample Response
<a name="API_CreateImportTask_Example_1_Response"></a>

```
HTTP/1.1 200 OK
          {
          "importId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
          "importDestinationArn": "arn:aws:logs:us-east-1:123456789012:log-group:aws/cloudtrail/f1d45bff-d0e3-4868-b5d9-2eb678aa32fb",
          "creationTime": 1641168000000
          }
```

## See Also
<a name="API_CreateImportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/CreateImportTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/CreateImportTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/CreateImportTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/CreateImportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/CreateImportTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/CreateImportTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/CreateImportTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/CreateImportTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/CreateImportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/CreateImportTask)
