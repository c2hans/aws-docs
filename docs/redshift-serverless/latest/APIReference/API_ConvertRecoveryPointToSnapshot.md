---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ConvertRecoveryPointToSnapshot.html
---

# ConvertRecoveryPointToSnapshot
<a name="API_ConvertRecoveryPointToSnapshot"></a>

Converts a recovery point to a snapshot. For more information about recovery points and snapshots, see [Working with snapshots and recovery points](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshots-recovery-points.html).

## Request Syntax
<a name="API_ConvertRecoveryPointToSnapshot_RequestSyntax"></a>

```
{
   "recoveryPointId": "{{string}}",
   "retentionPeriod": {{number}},
   "snapshotName": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_ConvertRecoveryPointToSnapshot_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [recoveryPointId](#API_ConvertRecoveryPointToSnapshot_RequestSyntax) **   <a name="redshiftserverless-ConvertRecoveryPointToSnapshot-request-recoveryPointId"></a>
The unique identifier of the recovery point.
Type: String
Required: Yes

 ** [retentionPeriod](#API_ConvertRecoveryPointToSnapshot_RequestSyntax) **   <a name="redshiftserverless-ConvertRecoveryPointToSnapshot-request-retentionPeriod"></a>
How long to retain the snapshot.
Type: Integer
Required: No

 ** [snapshotName](#API_ConvertRecoveryPointToSnapshot_RequestSyntax) **   <a name="redshiftserverless-ConvertRecoveryPointToSnapshot-request-snapshotName"></a>
The name of the snapshot.
Type: String
Required: Yes

 ** [tags](#API_ConvertRecoveryPointToSnapshot_RequestSyntax) **   <a name="redshiftserverless-ConvertRecoveryPointToSnapshot-request-tags"></a>
An array of [Tag objects](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Tag.html) to associate with the created snapshot.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_ConvertRecoveryPointToSnapshot_ResponseSyntax"></a>

```
{
   "snapshot": {
      "accountsWithProvisionedRestoreAccess": [ "string" ],
      "accountsWithRestoreAccess": [ "string" ],
      "actualIncrementalBackupSizeInMegaBytes": number,
      "adminPasswordSecretArn": "string",
      "adminPasswordSecretKmsKeyId": "string",
      "adminUsername": "string",
      "backupProgressInMegaBytes": number,
      "currentBackupRateInMegaBytesPerSecond": number,
      "elapsedTimeInSeconds": number,
      "estimatedSecondsToCompletion": number,
      "kmsKeyId": "string",
      "namespaceArn": "string",
      "namespaceName": "string",
      "ownerAccount": "string",
      "snapshotArn": "string",
      "snapshotCreateTime": "string",
      "snapshotName": "string",
      "snapshotRemainingDays": number,
      "snapshotRetentionPeriod": number,
      "snapshotRetentionStartTime": "string",
      "status": "string",
      "totalBackupSizeInMegaBytes": number
   }
}
```

## Response Elements
<a name="API_ConvertRecoveryPointToSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [snapshot](#API_ConvertRecoveryPointToSnapshot_ResponseSyntax) **   <a name="redshiftserverless-ConvertRecoveryPointToSnapshot-response-snapshot"></a>
The snapshot converted from the recovery point.
Type: [Snapshot](API_Snapshot.md) object

## Errors
<a name="API_ConvertRecoveryPointToSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The submitted action has conflicts.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
The service limit was exceeded.
HTTP Status Code: 400

 ** TooManyTagsException **
The request exceeded the number of tags allowed for a resource.
 ** resourceName **
The name of the resource that exceeded the number of tags allowed for a resource.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ConvertRecoveryPointToSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/ConvertRecoveryPointToSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/ConvertRecoveryPointToSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/ConvertRecoveryPointToSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/ConvertRecoveryPointToSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/ConvertRecoveryPointToSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/ConvertRecoveryPointToSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/ConvertRecoveryPointToSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/ConvertRecoveryPointToSnapshot)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/ConvertRecoveryPointToSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/ConvertRecoveryPointToSnapshot)
