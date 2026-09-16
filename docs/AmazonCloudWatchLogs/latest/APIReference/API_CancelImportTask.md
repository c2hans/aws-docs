---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CancelImportTask.html
---

# CancelImportTask
<a name="API_CancelImportTask"></a>

Cancels an active import task and stops importing data from the CloudTrail Lake Event Data Store.

## Request Syntax
<a name="API_CancelImportTask_RequestSyntax"></a>

```
{
   "importId": "{{string}}"
}
```

## Request Parameters
<a name="API_CancelImportTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [importId](#API_CancelImportTask_RequestSyntax) **   <a name="CWL-CancelImportTask-request-importId"></a>
The ID of the import task to cancel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\-a-zA-Z0-9]+`
Required: Yes

## Response Syntax
<a name="API_CancelImportTask_ResponseSyntax"></a>

```
{
   "creationTime": number,
   "importId": "string",
   "importStatistics": {
      "bytesImported": number
   },
   "importStatus": "string",
   "lastUpdatedTime": number
}
```

## Response Elements
<a name="API_CancelImportTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_CancelImportTask_ResponseSyntax) **   <a name="CWL-CancelImportTask-response-creationTime"></a>
The timestamp when the import task was created, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
Type: Long
Valid Range: Minimum value of 0.

 ** [importId](#API_CancelImportTask_ResponseSyntax) **   <a name="CWL-CancelImportTask-response-importId"></a>
The ID of the cancelled import task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\-a-zA-Z0-9]+`

 ** [importStatistics](#API_CancelImportTask_ResponseSyntax) **   <a name="CWL-CancelImportTask-response-importStatistics"></a>
Statistics about the import progress at the time of cancellation.
Type: [ImportStatistics](API_ImportStatistics.md) object

 ** [importStatus](#API_CancelImportTask_ResponseSyntax) **   <a name="CWL-CancelImportTask-response-importStatus"></a>
The final status of the import task. This will be set to CANCELLED.
Type: String
Valid Values: `IN_PROGRESS | CANCELLED | COMPLETED | FAILED`

 ** [lastUpdatedTime](#API_CancelImportTask_ResponseSyntax) **   <a name="CWL-CancelImportTask-response-lastUpdatedTime"></a>
The timestamp when the import task was cancelled, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
Type: Long
Valid Range: Minimum value of 0.

## Errors
<a name="API_CancelImportTask_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 400

## Examples
<a name="API_CancelImportTask_Examples"></a>

### To cancel an import task
<a name="API_CancelImportTask_Example_1"></a>

The following example cancels an active import task and returns the final status.

#### Sample Request
<a name="API_CancelImportTask_Example_1_Request"></a>

```
POST / HTTP/1.1
          Host: logs.<region>.<domain>
          X-Amz-Target: Logs_20140328.CancelImportTask
          {
          "importId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
          }
```

#### Sample Response
<a name="API_CancelImportTask_Example_1_Response"></a>

```
HTTP/1.1 200 OK
          {
          "importId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
          "importStatistics": {
          "bytesImported": 524288
          },
          "importStatus": "CANCELLED",
          "creationTime": 1641168000000,
          "lastUpdatedTime": 1641175200000
          }
```

## See Also
<a name="API_CancelImportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/CancelImportTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/CancelImportTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/CancelImportTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/CancelImportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/CancelImportTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/CancelImportTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/CancelImportTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/CancelImportTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/CancelImportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/CancelImportTask)
