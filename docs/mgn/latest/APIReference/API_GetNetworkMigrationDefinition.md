---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_GetNetworkMigrationDefinition.html
---

# GetNetworkMigrationDefinition
<a name="API_GetNetworkMigrationDefinition"></a>

Retrieves the details of a network migration definition including source and target configurations.

## Request Syntax
<a name="API_GetNetworkMigrationDefinition_RequestSyntax"></a>

```
POST /network-migration/GetNetworkMigrationDefinition HTTP/1.1
Content-type: application/json

{
   "networkMigrationDefinitionID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetNetworkMigrationDefinition_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetNetworkMigrationDefinition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [networkMigrationDefinitionID](#API_GetNetworkMigrationDefinition_RequestSyntax) **   <a name="mgn-GetNetworkMigrationDefinition-request-networkMigrationDefinitionID"></a>
The unique identifier of the network migration definition to retrieve.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `nmd-[0-9a-zA-Z]{17}`
Required: Yes

## Response Syntax
<a name="API_GetNetworkMigrationDefinition_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "createdAt": number,
   "description": "string",
   "name": "string",
   "networkMigrationDefinitionID": "string",
   "scopeTags": {
      "string" : "string"
   },
   "sourceConfigurations": [
      {
         "sourceEnvironment": "string",
         "sourceS3Configuration": {
            "s3Bucket": "string",
            "s3BucketOwner": "string",
            "s3Key": "string"
         }
      }
   ],
   "tags": {
      "string" : "string"
   },
   "targetDeployment": "string",
   "targetNetwork": {
      "inboundCidr": "string",
      "inspectionCidr": "string",
      "outboundCidr": "string",
      "topology": "string"
   },
   "targetS3Configuration": {
      "s3Bucket": "string",
      "s3BucketOwner": "string"
   },
   "updatedAt": number
}
```

## Response Elements
<a name="API_GetNetworkMigrationDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetNetworkMigrationDefinition_ResponseSyntax) **   <a name="mgn-GetNetworkMigrationDefinition-response-arn"></a>
The Amazon Resource Name (ARN) of the network migration definition.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [createdAt](#API_GetNetworkMigrationDefinition_ResponseSyntax) **   <a name="mgn-GetNetworkMigrationDefinition-response-createdAt"></a>
The timestamp when the network migration definition was created.
Type: Timestamp

 ** [description](#API_GetNetworkMigrationDefinition_ResponseSyntax) **   <a name="mgn-GetNetworkMigrationDefinition-response-description"></a>
A description of the network migration definition.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 600.
Pattern: `[^\x00]*`

 ** [name](#API_GetNetworkMigrationDefinition_ResponseSyntax) **   <a name="mgn-GetNetworkMigrationDefinition-response-name"></a>
The name of the network migration definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\s\x00]( *[^\s\x00])*`

 ** [networkMigrationDefinitionID](#API_GetNetworkMigrationDefinition_ResponseSyntax) **   <a name="mgn-GetNetworkMigrationDefinition-response-networkMigrationDefinitionID"></a>
The unique identifier of the network migration definition.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `nmd-[0-9a-zA-Z]{17}`

 ** [scopeTags](#API_GetNetworkMigrationDefinition_ResponseSyntax) **   <a name="mgn-GetNetworkMigrationDefinition-response-scopeTags"></a>
Scope tags for the network migration definition.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 40 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z0-9\s+\-=._:/@]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s+\-=._:/@]*`

 ** [sourceConfigurations](#API_GetNetworkMigrationDefinition_ResponseSyntax) **   <a name="mgn-GetNetworkMigrationDefinition-response-sourceConfigurations"></a>
A list of source configurations for the network migration.
Type: Array of [SourceConfiguration](API_SourceConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2 items.

 ** [tags](#API_GetNetworkMigrationDefinition_ResponseSyntax) **   <a name="mgn-GetNetworkMigrationDefinition-response-tags"></a>
Tags assigned to the network migration definition.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [targetDeployment](#API_GetNetworkMigrationDefinition_ResponseSyntax) **   <a name="mgn-GetNetworkMigrationDefinition-response-targetDeployment"></a>
The target deployment configuration for the migrated network.
Type: String
Valid Values: `SINGLE_ACCOUNT | MULTI_ACCOUNT`

 ** [targetNetwork](#API_GetNetworkMigrationDefinition_ResponseSyntax) **   <a name="mgn-GetNetworkMigrationDefinition-response-targetNetwork"></a>
The target network configuration including topology and CIDR ranges.
Type: [TargetNetwork](API_TargetNetwork.md) object

 ** [targetS3Configuration](#API_GetNetworkMigrationDefinition_ResponseSyntax) **   <a name="mgn-GetNetworkMigrationDefinition-response-targetS3Configuration"></a>
The S3 configuration for storing the target network artifacts.
Type: [TargetS3Configuration](API_TargetS3Configuration.md) object

 ** [updatedAt](#API_GetNetworkMigrationDefinition_ResponseSyntax) **   <a name="mgn-GetNetworkMigrationDefinition-response-updatedAt"></a>
The timestamp when the network migration definition was last updated.
Type: Timestamp

## Errors
<a name="API_GetNetworkMigrationDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Operation denied due to a file permission or access check error.
HTTP Status Code: 403

 ** ResourceNotFoundException **
Resource not found exception.
 ** resourceId **
Resource ID not found error.
 ** resourceType **
Resource type not found error.
HTTP Status Code: 404

## See Also
<a name="API_GetNetworkMigrationDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/GetNetworkMigrationDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/GetNetworkMigrationDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/GetNetworkMigrationDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/GetNetworkMigrationDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/GetNetworkMigrationDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/GetNetworkMigrationDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/GetNetworkMigrationDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/GetNetworkMigrationDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/GetNetworkMigrationDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/GetNetworkMigrationDefinition)
