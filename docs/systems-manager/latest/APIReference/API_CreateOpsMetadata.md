---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateOpsMetadata.html
---

# CreateOpsMetadata
<a name="API_CreateOpsMetadata"></a>

If you create a new application in Application Manager, AWS Systems Manager calls this API operation to specify information about the new application, including the application type.

## Request Syntax
<a name="API_CreateOpsMetadata_RequestSyntax"></a>

```
{
   "Metadata": {
      "{{string}}" : {
         "Value": "{{string}}"
      }
   },
   "ResourceId": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateOpsMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Metadata](#API_CreateOpsMetadata_RequestSyntax) **   <a name="systemsmanager-CreateOpsMetadata-request-Metadata"></a>
Metadata for a new Application Manager application.
Type: String to [MetadataValue](API_MetadataValue.md) object map
Map Entries: Maximum number of 5 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `^(?!\s*$).+`
Required: No

 ** [ResourceId](#API_CreateOpsMetadata_RequestSyntax) **   <a name="systemsmanager-CreateOpsMetadata-request-ResourceId"></a>
A resource ID for a new Application Manager application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^(?!\s*$).+`
Required: Yes

 ** [Tags](#API_CreateOpsMetadata_RequestSyntax) **   <a name="systemsmanager-CreateOpsMetadata-request-Tags"></a>
Optional metadata that you assign to a resource. You can specify a maximum of five tags for an OpsMetadata object. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag an OpsMetadata object to identify an environment or target AWS Region. In this case, you could specify the following key-value pairs:
+  `Key=Environment,Value=Production`
+  `Key=Region,Value=us-east-2`
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 1000 items.
Required: No

## Response Syntax
<a name="API_CreateOpsMetadata_ResponseSyntax"></a>

```
{
   "OpsMetadataArn": "string"
}
```

## Response Elements
<a name="API_CreateOpsMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OpsMetadataArn](#API_CreateOpsMetadata_ResponseSyntax) **   <a name="systemsmanager-CreateOpsMetadata-response-OpsMetadataArn"></a>
The Amazon Resource Name (ARN) of the OpsMetadata Object or blob created by the call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:(aws[a-zA-Z-]*)?:ssm:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:opsmetadata\/([a-zA-Z0-9-_\.\/]*)`

## Errors
<a name="API_CreateOpsMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** OpsMetadataAlreadyExistsException **
An OpsMetadata object already exists for the selected resource.
HTTP Status Code: 400

 ** OpsMetadataInvalidArgumentException **
One of the arguments passed is invalid.
HTTP Status Code: 400

 ** OpsMetadataLimitExceededException **
Your account reached the maximum number of OpsMetadata objects allowed by Application Manager. The maximum is 200 OpsMetadata objects. Delete one or more OpsMetadata object and try again.
HTTP Status Code: 400

 ** OpsMetadataTooManyUpdatesException **
The system is processing too many concurrent updates. Wait a few moments and try again.
HTTP Status Code: 400

## See Also
<a name="API_CreateOpsMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/CreateOpsMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/CreateOpsMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/CreateOpsMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/CreateOpsMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/CreateOpsMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/CreateOpsMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/CreateOpsMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/CreateOpsMetadata)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/CreateOpsMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/CreateOpsMetadata)
