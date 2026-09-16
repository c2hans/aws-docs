---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_DeleteSnapshot.html
---

# DeleteSnapshot
<a name="API_DeleteSnapshot"></a>

Deletes a snapshot from Amazon Redshift Serverless.

## Request Syntax
<a name="API_DeleteSnapshot_RequestSyntax"></a>

```
{
   "snapshotName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteSnapshot_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [snapshotName](#API_DeleteSnapshot_RequestSyntax) **   <a name="redshiftserverless-DeleteSnapshot-request-snapshotName"></a>
The name of the snapshot to be deleted.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteSnapshot_ResponseSyntax"></a>

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
<a name="API_DeleteSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [snapshot](#API_DeleteSnapshot_ResponseSyntax) **   <a name="redshiftserverless-DeleteSnapshot-response-snapshot"></a>
The deleted snapshot object.
Type: [Snapshot](API_Snapshot.md) object

## Errors
<a name="API_DeleteSnapshot_Errors"></a>

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

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DeleteSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/DeleteSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/DeleteSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/DeleteSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/DeleteSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/DeleteSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/DeleteSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/DeleteSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/DeleteSnapshot)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/DeleteSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/DeleteSnapshot)
