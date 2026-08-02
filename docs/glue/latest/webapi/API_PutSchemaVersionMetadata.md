---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_PutSchemaVersionMetadata.html
---

# PutSchemaVersionMetadata
<a name="API_PutSchemaVersionMetadata"></a>

Puts the metadata key value pair for a specified schema version ID. A maximum of 10 key value pairs will be allowed per schema version. They can be added over one or more calls.

## Request Syntax
<a name="API_PutSchemaVersionMetadata_RequestSyntax"></a>

```
{
   "MetadataKeyValue": {
      "MetadataKey": "{{string}}",
      "MetadataValue": "{{string}}"
   },
   "SchemaId": {
      "RegistryName": "{{string}}",
      "SchemaArn": "{{string}}",
      "SchemaName": "{{string}}"
   },
   "SchemaVersionId": "{{string}}",
   "SchemaVersionNumber": {
      "LatestVersion": {{boolean}},
      "VersionNumber": {{number}}
   }
}
```

## Request Parameters
<a name="API_PutSchemaVersionMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MetadataKeyValue](#API_PutSchemaVersionMetadata_RequestSyntax) **   <a name="Glue-PutSchemaVersionMetadata-request-MetadataKeyValue"></a>
The metadata key's corresponding value.
Type: [MetadataKeyValuePair](API_MetadataKeyValuePair.md) object
Required: Yes

 ** [SchemaId](#API_PutSchemaVersionMetadata_RequestSyntax) **   <a name="Glue-PutSchemaVersionMetadata-request-SchemaId"></a>
The unique ID for the schema.
Type: [SchemaId](API_SchemaId.md) object
Required: No

 ** [SchemaVersionId](#API_PutSchemaVersionMetadata_RequestSyntax) **   <a name="Glue-PutSchemaVersionMetadata-request-SchemaVersionId"></a>
The unique version ID of the schema version.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** [SchemaVersionNumber](#API_PutSchemaVersionMetadata_RequestSyntax) **   <a name="Glue-PutSchemaVersionMetadata-request-SchemaVersionNumber"></a>
The version number of the schema.
Type: [SchemaVersionNumber](API_SchemaVersionNumber.md) object
Required: No

## Response Syntax
<a name="API_PutSchemaVersionMetadata_ResponseSyntax"></a>

```
{
   "LatestVersion": boolean,
   "MetadataKey": "string",
   "MetadataValue": "string",
   "RegistryName": "string",
   "SchemaArn": "string",
   "SchemaName": "string",
   "SchemaVersionId": "string",
   "VersionNumber": number
}
```

## Response Elements
<a name="API_PutSchemaVersionMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LatestVersion](#API_PutSchemaVersionMetadata_ResponseSyntax) **   <a name="Glue-PutSchemaVersionMetadata-response-LatestVersion"></a>
The latest version of the schema.
Type: Boolean

 ** [MetadataKey](#API_PutSchemaVersionMetadata_ResponseSyntax) **   <a name="Glue-PutSchemaVersionMetadata-response-MetadataKey"></a>
The metadata key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9+-=._./@]+`

 ** [MetadataValue](#API_PutSchemaVersionMetadata_ResponseSyntax) **   <a name="Glue-PutSchemaVersionMetadata-response-MetadataValue"></a>
The value of the metadata key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9+-=._./@]+`

 ** [RegistryName](#API_PutSchemaVersionMetadata_ResponseSyntax) **   <a name="Glue-PutSchemaVersionMetadata-response-RegistryName"></a>
The name for the registry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-_$#.]+`

 ** [SchemaArn](#API_PutSchemaVersionMetadata_ResponseSyntax) **   <a name="Glue-PutSchemaVersionMetadata-response-SchemaArn"></a>
The Amazon Resource Name (ARN) for the schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Pattern: `arn:aws(-(cn|us-gov|iso(-[bef])?))?:glue:.*`

 ** [SchemaName](#API_PutSchemaVersionMetadata_ResponseSyntax) **   <a name="Glue-PutSchemaVersionMetadata-response-SchemaName"></a>
The name for the schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-_$#.]+`

 ** [SchemaVersionId](#API_PutSchemaVersionMetadata_ResponseSyntax) **   <a name="Glue-PutSchemaVersionMetadata-response-SchemaVersionId"></a>
The unique version ID of the schema version.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [VersionNumber](#API_PutSchemaVersionMetadata_ResponseSyntax) **   <a name="Glue-PutSchemaVersionMetadata-response-VersionNumber"></a>
The version number of the schema.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.

## Errors
<a name="API_PutSchemaVersionMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** AlreadyExistsException **
A resource to be created or added already exists.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_PutSchemaVersionMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/PutSchemaVersionMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/PutSchemaVersionMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/PutSchemaVersionMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/PutSchemaVersionMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/PutSchemaVersionMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/PutSchemaVersionMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/PutSchemaVersionMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/PutSchemaVersionMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/PutSchemaVersionMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/PutSchemaVersionMetadata)
