---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteOpsMetadata.html
---

# DeleteOpsMetadata
<a name="API_DeleteOpsMetadata"></a>

Delete OpsMetadata related to an application.

## Request Syntax
<a name="API_DeleteOpsMetadata_RequestSyntax"></a>

```
{
   "OpsMetadataArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteOpsMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [OpsMetadataArn](#API_DeleteOpsMetadata_RequestSyntax) **   <a name="systemsmanager-DeleteOpsMetadata-request-OpsMetadataArn"></a>
The Amazon Resource Name (ARN) of an OpsMetadata Object to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:(aws[a-zA-Z-]*)?:ssm:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:opsmetadata\/([a-zA-Z0-9-_\.\/]*)`
Required: Yes

## Response Elements
<a name="API_DeleteOpsMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteOpsMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** OpsMetadataInvalidArgumentException **
One of the arguments passed is invalid.
HTTP Status Code: 400

 ** OpsMetadataNotFoundException **
The OpsMetadata object doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_DeleteOpsMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DeleteOpsMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DeleteOpsMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DeleteOpsMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DeleteOpsMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DeleteOpsMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DeleteOpsMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DeleteOpsMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DeleteOpsMetadata)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DeleteOpsMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DeleteOpsMetadata)
