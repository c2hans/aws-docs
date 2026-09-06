---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateSnapshotCopyConfiguration.html
---

# CreateSnapshotCopyConfiguration
<a name="API_CreateSnapshotCopyConfiguration"></a>

Creates a snapshot copy configuration that lets you copy snapshots to another AWS Region.

## Request Syntax
<a name="API_CreateSnapshotCopyConfiguration_RequestSyntax"></a>

```
{
   "destinationKmsKeyId": "{{string}}",
   "destinationRegion": "{{string}}",
   "namespaceName": "{{string}}",
   "snapshotRetentionPeriod": {{number}}
}
```

## Request Parameters
<a name="API_CreateSnapshotCopyConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [destinationKmsKeyId](#API_CreateSnapshotCopyConfiguration_RequestSyntax) **   <a name="redshiftserverless-CreateSnapshotCopyConfiguration-request-destinationKmsKeyId"></a>
The KMS key to use to encrypt your snapshots in the destination AWS Region.
Type: String
Required: No

 ** [destinationRegion](#API_CreateSnapshotCopyConfiguration_RequestSyntax) **   <a name="redshiftserverless-CreateSnapshotCopyConfiguration-request-destinationRegion"></a>
The destination AWS Region that you want to copy snapshots to.
Type: String
Required: Yes

 ** [namespaceName](#API_CreateSnapshotCopyConfiguration_RequestSyntax) **   <a name="redshiftserverless-CreateSnapshotCopyConfiguration-request-namespaceName"></a>
The name of the namespace to copy snapshots from.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

 ** [snapshotRetentionPeriod](#API_CreateSnapshotCopyConfiguration_RequestSyntax) **   <a name="redshiftserverless-CreateSnapshotCopyConfiguration-request-snapshotRetentionPeriod"></a>
The retention period of the snapshots that you copy to the destination AWS Region.
Type: Integer
Required: No

## Response Syntax
<a name="API_CreateSnapshotCopyConfiguration_ResponseSyntax"></a>

```
{
   "snapshotCopyConfiguration": {
      "destinationKmsKeyId": "string",
      "destinationRegion": "string",
      "namespaceName": "string",
      "snapshotCopyConfigurationArn": "string",
      "snapshotCopyConfigurationId": "string",
      "snapshotRetentionPeriod": number
   }
}
```

## Response Elements
<a name="API_CreateSnapshotCopyConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [snapshotCopyConfiguration](#API_CreateSnapshotCopyConfiguration_ResponseSyntax) **   <a name="redshiftserverless-CreateSnapshotCopyConfiguration-response-snapshotCopyConfiguration"></a>
The snapshot copy configuration object that is returned.
Type: [SnapshotCopyConfiguration](API_SnapshotCopyConfiguration.md) object

## Errors
<a name="API_CreateSnapshotCopyConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

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

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateSnapshotCopyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/CreateSnapshotCopyConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/CreateSnapshotCopyConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/CreateSnapshotCopyConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/CreateSnapshotCopyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/CreateSnapshotCopyConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/CreateSnapshotCopyConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/CreateSnapshotCopyConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/CreateSnapshotCopyConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/CreateSnapshotCopyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/CreateSnapshotCopyConfiguration)
