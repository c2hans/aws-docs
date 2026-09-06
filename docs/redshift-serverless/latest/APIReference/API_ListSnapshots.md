---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListSnapshots.html
---

# ListSnapshots
<a name="API_ListSnapshots"></a>

Returns a list of snapshots.

## Request Syntax
<a name="API_ListSnapshots_RequestSyntax"></a>

```
{
   "endTime": {{number}},
   "maxResults": {{number}},
   "namespaceArn": "{{string}}",
   "namespaceName": "{{string}}",
   "nextToken": "{{string}}",
   "ownerAccount": "{{string}}",
   "startTime": {{number}}
}
```

## Request Parameters
<a name="API_ListSnapshots_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [endTime](#API_ListSnapshots_RequestSyntax) **   <a name="redshiftserverless-ListSnapshots-request-endTime"></a>
The timestamp showing when the snapshot creation finished.
Type: Timestamp
Required: No

 ** [maxResults](#API_ListSnapshots_RequestSyntax) **   <a name="redshiftserverless-ListSnapshots-request-maxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to display the next page of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [namespaceArn](#API_ListSnapshots_RequestSyntax) **   <a name="redshiftserverless-ListSnapshots-request-namespaceArn"></a>
The Amazon Resource Name (ARN) of the namespace from which to list all snapshots.
Type: String
Required: No

 ** [namespaceName](#API_ListSnapshots_RequestSyntax) **   <a name="redshiftserverless-ListSnapshots-request-namespaceName"></a>
The namespace from which to list all snapshots.
Type: String
Required: No

 ** [nextToken](#API_ListSnapshots_RequestSyntax) **   <a name="redshiftserverless-ListSnapshots-request-nextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String
Required: No

 ** [ownerAccount](#API_ListSnapshots_RequestSyntax) **   <a name="redshiftserverless-ListSnapshots-request-ownerAccount"></a>
The owner AWS account of the snapshot.
Type: String
Required: No

 ** [startTime](#API_ListSnapshots_RequestSyntax) **   <a name="redshiftserverless-ListSnapshots-request-startTime"></a>
The time when the creation of the snapshot was initiated.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_ListSnapshots_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "snapshots": [
      {
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
   ]
}
```

## Response Elements
<a name="API_ListSnapshots_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSnapshots_ResponseSyntax) **   <a name="redshiftserverless-ListSnapshots-response-nextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String

 ** [snapshots](#API_ListSnapshots_ResponseSyntax) **   <a name="redshiftserverless-ListSnapshots-response-snapshots"></a>
All of the returned snapshot objects.
Type: Array of [Snapshot](API_Snapshot.md) objects

## Errors
<a name="API_ListSnapshots_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_ListSnapshots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/ListSnapshots)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/ListSnapshots)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/ListSnapshots)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/ListSnapshots)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/ListSnapshots)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/ListSnapshots)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/ListSnapshots)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/ListSnapshots)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/ListSnapshots)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/ListSnapshots)
