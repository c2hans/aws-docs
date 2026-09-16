---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_QuerySchemaVersionMetadata.html
---

# QuerySchemaVersionMetadata
<a name="API_QuerySchemaVersionMetadata"></a>

Queries for the schema version metadata information.

## Request Syntax
<a name="API_QuerySchemaVersionMetadata_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "MetadataList": [
      {
         "MetadataKey": "{{string}}",
         "MetadataValue": "{{string}}"
      }
   ],
   "NextToken": "{{string}}",
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
<a name="API_QuerySchemaVersionMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_QuerySchemaVersionMetadata_RequestSyntax) **   <a name="Glue-QuerySchemaVersionMetadata-request-MaxResults"></a>
Maximum number of results required per page. If the value is not supplied, this will be defaulted to 25 per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [MetadataList](#API_QuerySchemaVersionMetadata_RequestSyntax) **   <a name="Glue-QuerySchemaVersionMetadata-request-MetadataList"></a>
Search key-value pairs for metadata, if they are not provided all the metadata information will be fetched.
Type: Array of [MetadataKeyValuePair](API_MetadataKeyValuePair.md) objects
Required: No

 ** [NextToken](#API_QuerySchemaVersionMetadata_RequestSyntax) **   <a name="Glue-QuerySchemaVersionMetadata-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

 ** [SchemaId](#API_QuerySchemaVersionMetadata_RequestSyntax) **   <a name="Glue-QuerySchemaVersionMetadata-request-SchemaId"></a>
A wrapper structure that may contain the schema name and Amazon Resource Name (ARN).
Type: [SchemaId](API_SchemaId.md) object
Required: No

 ** [SchemaVersionId](#API_QuerySchemaVersionMetadata_RequestSyntax) **   <a name="Glue-QuerySchemaVersionMetadata-request-SchemaVersionId"></a>
The unique version ID of the schema version.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** [SchemaVersionNumber](#API_QuerySchemaVersionMetadata_RequestSyntax) **   <a name="Glue-QuerySchemaVersionMetadata-request-SchemaVersionNumber"></a>
The version number of the schema.
Type: [SchemaVersionNumber](API_SchemaVersionNumber.md) object
Required: No

## Response Syntax
<a name="API_QuerySchemaVersionMetadata_ResponseSyntax"></a>

```
{
   "MetadataInfoMap": {
      "string" : {
         "CreatedTime": "string",
         "MetadataValue": "string",
         "OtherMetadataValueList": [
            {
               "CreatedTime": "string",
               "MetadataValue": "string"
            }
         ]
      }
   },
   "NextToken": "string",
   "SchemaVersionId": "string"
}
```

## Response Elements
<a name="API_QuerySchemaVersionMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MetadataInfoMap](#API_QuerySchemaVersionMetadata_ResponseSyntax) **   <a name="Glue-QuerySchemaVersionMetadata-response-MetadataInfoMap"></a>
A map of a metadata key and associated values.
Type: String to [MetadataInfo](API_MetadataInfo.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9+-=._./@]+`

 ** [NextToken](#API_QuerySchemaVersionMetadata_ResponseSyntax) **   <a name="Glue-QuerySchemaVersionMetadata-response-NextToken"></a>
A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last.
Type: String

 ** [SchemaVersionId](#API_QuerySchemaVersionMetadata_ResponseSyntax) **   <a name="Glue-QuerySchemaVersionMetadata-response-SchemaVersionId"></a>
The unique version ID of the schema version.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_QuerySchemaVersionMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
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

## See Also
<a name="API_QuerySchemaVersionMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/QuerySchemaVersionMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/QuerySchemaVersionMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/QuerySchemaVersionMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/QuerySchemaVersionMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/QuerySchemaVersionMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/QuerySchemaVersionMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/QuerySchemaVersionMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/QuerySchemaVersionMetadata)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/QuerySchemaVersionMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/QuerySchemaVersionMetadata)
