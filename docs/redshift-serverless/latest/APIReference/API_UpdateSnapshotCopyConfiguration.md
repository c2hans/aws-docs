---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_UpdateSnapshotCopyConfiguration.html
---

# UpdateSnapshotCopyConfiguration
<a name="API_UpdateSnapshotCopyConfiguration"></a>

Updates a snapshot copy configuration.

## Request Syntax
<a name="API_UpdateSnapshotCopyConfiguration_RequestSyntax"></a>

```
{
   "snapshotCopyConfigurationId": "{{string}}",
   "snapshotRetentionPeriod": {{number}}
}
```

## Request Parameters
<a name="API_UpdateSnapshotCopyConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [snapshotCopyConfigurationId](#API_UpdateSnapshotCopyConfiguration_RequestSyntax) **   <a name="redshiftserverless-UpdateSnapshotCopyConfiguration-request-snapshotCopyConfigurationId"></a>
The ID of the snapshot copy configuration to update.
Type: String
Required: Yes

 ** [snapshotRetentionPeriod](#API_UpdateSnapshotCopyConfiguration_RequestSyntax) **   <a name="redshiftserverless-UpdateSnapshotCopyConfiguration-request-snapshotRetentionPeriod"></a>
The new retention period of how long to keep a snapshot in the destination AWS Region.
Type: Integer
Required: No

## Response Syntax
<a name="API_UpdateSnapshotCopyConfiguration_ResponseSyntax"></a>

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
<a name="API_UpdateSnapshotCopyConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [snapshotCopyConfiguration](#API_UpdateSnapshotCopyConfiguration_ResponseSyntax) **   <a name="redshiftserverless-UpdateSnapshotCopyConfiguration-response-snapshotCopyConfiguration"></a>
The updated snapshot copy configuration object.
Type: [SnapshotCopyConfiguration](API_SnapshotCopyConfiguration.md) object

## Errors
<a name="API_UpdateSnapshotCopyConfiguration_Errors"></a>

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

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateSnapshotCopyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/UpdateSnapshotCopyConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/UpdateSnapshotCopyConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/UpdateSnapshotCopyConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/UpdateSnapshotCopyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/UpdateSnapshotCopyConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/UpdateSnapshotCopyConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/UpdateSnapshotCopyConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/UpdateSnapshotCopyConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/UpdateSnapshotCopyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/UpdateSnapshotCopyConfiguration)
