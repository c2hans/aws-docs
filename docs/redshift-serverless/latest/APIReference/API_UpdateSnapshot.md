---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_UpdateSnapshot.html
---

# UpdateSnapshot
<a name="API_UpdateSnapshot"></a>

Updates a snapshot.

## Request Syntax
<a name="API_UpdateSnapshot_RequestSyntax"></a>

```
{
   "retentionPeriod": {{number}},
   "snapshotName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateSnapshot_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [retentionPeriod](#API_UpdateSnapshot_RequestSyntax) **   <a name="redshiftserverless-UpdateSnapshot-request-retentionPeriod"></a>
The new retention period of the snapshot.
Type: Integer
Required: No

 ** [snapshotName](#API_UpdateSnapshot_RequestSyntax) **   <a name="redshiftserverless-UpdateSnapshot-request-snapshotName"></a>
The name of the snapshot.
Type: String
Required: Yes

## Response Syntax
<a name="API_UpdateSnapshot_ResponseSyntax"></a>

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
<a name="API_UpdateSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [snapshot](#API_UpdateSnapshot_ResponseSyntax) **   <a name="redshiftserverless-UpdateSnapshot-response-snapshot"></a>
The updated snapshot object.
Type: [Snapshot](API_Snapshot.md) object

## Errors
<a name="API_UpdateSnapshot_Errors"></a>

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
<a name="API_UpdateSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/UpdateSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/UpdateSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/UpdateSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/UpdateSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/UpdateSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/UpdateSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/UpdateSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/UpdateSnapshot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/UpdateSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/UpdateSnapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
