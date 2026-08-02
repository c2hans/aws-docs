---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateOpsMetadata.html
---

# UpdateOpsMetadata
<a name="API_UpdateOpsMetadata"></a>

 AWS Systems Manager calls this API operation when you edit OpsMetadata in Application Manager.

## Request Syntax
<a name="API_UpdateOpsMetadata_RequestSyntax"></a>

```
{
   "KeysToDelete": [ "{{string}}" ],
   "MetadataToUpdate": {
      "{{string}}" : {
         "Value": "{{string}}"
      }
   },
   "OpsMetadataArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateOpsMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [KeysToDelete](#API_UpdateOpsMetadata_RequestSyntax) **   <a name="systemsmanager-UpdateOpsMetadata-request-KeysToDelete"></a>
The metadata keys to delete from the OpsMetadata object.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^(?!\s*$).+`
Required: No

 ** [MetadataToUpdate](#API_UpdateOpsMetadata_RequestSyntax) **   <a name="systemsmanager-UpdateOpsMetadata-request-MetadataToUpdate"></a>
Metadata to add to an OpsMetadata object.
Type: String to [MetadataValue](API_MetadataValue.md) object map
Map Entries: Maximum number of 5 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `^(?!\s*$).+`
Required: No

 ** [OpsMetadataArn](#API_UpdateOpsMetadata_RequestSyntax) **   <a name="systemsmanager-UpdateOpsMetadata-request-OpsMetadataArn"></a>
The Amazon Resource Name (ARN) of the OpsMetadata Object to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:(aws[a-zA-Z-]*)?:ssm:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:opsmetadata\/([a-zA-Z0-9-_\.\/]*)`
Required: Yes

## Response Syntax
<a name="API_UpdateOpsMetadata_ResponseSyntax"></a>

```
{
   "OpsMetadataArn": "string"
}
```

## Response Elements
<a name="API_UpdateOpsMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OpsMetadataArn](#API_UpdateOpsMetadata_ResponseSyntax) **   <a name="systemsmanager-UpdateOpsMetadata-response-OpsMetadataArn"></a>
The Amazon Resource Name (ARN) of the OpsMetadata Object that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:(aws[a-zA-Z-]*)?:ssm:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:opsmetadata\/([a-zA-Z0-9-_\.\/]*)`

## Errors
<a name="API_UpdateOpsMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** OpsMetadataInvalidArgumentException **
One of the arguments passed is invalid.
HTTP Status Code: 400

 ** OpsMetadataKeyLimitExceededException **
The OpsMetadata object exceeds the maximum number of OpsMetadata keys that you can assign to an application in Application Manager.
HTTP Status Code: 400

 ** OpsMetadataNotFoundException **
The OpsMetadata object doesn't exist.
HTTP Status Code: 400

 ** OpsMetadataTooManyUpdatesException **
The system is processing too many concurrent updates. Wait a few moments and try again.
HTTP Status Code: 400

## See Also
<a name="API_UpdateOpsMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/UpdateOpsMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/UpdateOpsMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/UpdateOpsMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/UpdateOpsMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/UpdateOpsMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/UpdateOpsMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/UpdateOpsMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/UpdateOpsMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/UpdateOpsMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/UpdateOpsMetadata)
