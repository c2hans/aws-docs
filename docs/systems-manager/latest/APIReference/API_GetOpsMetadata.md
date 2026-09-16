---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetOpsMetadata.html
---

# GetOpsMetadata
<a name="API_GetOpsMetadata"></a>

View operational metadata related to an application in Application Manager.

## Request Syntax
<a name="API_GetOpsMetadata_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "OpsMetadataArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetOpsMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_GetOpsMetadata_RequestSyntax) **   <a name="systemsmanager-GetOpsMetadata-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** [NextToken](#API_GetOpsMetadata_RequestSyntax) **   <a name="systemsmanager-GetOpsMetadata-request-NextToken"></a>
A token to start the list. Use this token to get the next set of results.
Type: String
Required: No

 ** [OpsMetadataArn](#API_GetOpsMetadata_RequestSyntax) **   <a name="systemsmanager-GetOpsMetadata-request-OpsMetadataArn"></a>
The Amazon Resource Name (ARN) of an OpsMetadata Object to view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:(aws[a-zA-Z-]*)?:ssm:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:opsmetadata\/([a-zA-Z0-9-_\.\/]*)`
Required: Yes

## Response Syntax
<a name="API_GetOpsMetadata_ResponseSyntax"></a>

```
{
   "Metadata": {
      "string" : {
         "Value": "string"
      }
   },
   "NextToken": "string",
   "ResourceId": "string"
}
```

## Response Elements
<a name="API_GetOpsMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Metadata](#API_GetOpsMetadata_ResponseSyntax) **   <a name="systemsmanager-GetOpsMetadata-response-Metadata"></a>
OpsMetadata for an Application Manager application.
Type: String to [MetadataValue](API_MetadataValue.md) object map
Map Entries: Maximum number of 5 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `^(?!\s*$).+`

 ** [NextToken](#API_GetOpsMetadata_ResponseSyntax) **   <a name="systemsmanager-GetOpsMetadata-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String

 ** [ResourceId](#API_GetOpsMetadata_ResponseSyntax) **   <a name="systemsmanager-GetOpsMetadata-response-ResourceId"></a>
The resource ID of the Application Manager application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^(?!\s*$).+`

## Errors
<a name="API_GetOpsMetadata_Errors"></a>

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
<a name="API_GetOpsMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetOpsMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetOpsMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetOpsMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetOpsMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetOpsMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetOpsMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetOpsMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetOpsMetadata)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetOpsMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetOpsMetadata)
