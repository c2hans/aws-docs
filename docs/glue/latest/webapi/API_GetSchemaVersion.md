---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetSchemaVersion.html
---

# GetSchemaVersion
<a name="API_GetSchemaVersion"></a>

Get the specified schema by its unique ID assigned when a version of the schema is created or registered. Schema versions in Deleted status will not be included in the results.

## Request Syntax
<a name="API_GetSchemaVersion_RequestSyntax"></a>

```
{
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
<a name="API_GetSchemaVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SchemaId](#API_GetSchemaVersion_RequestSyntax) **   <a name="Glue-GetSchemaVersion-request-SchemaId"></a>
This is a wrapper structure to contain schema identity fields. The structure contains:
+ SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. Either `SchemaArn` or `SchemaName` and `RegistryName` has to be provided.
+ SchemaId$SchemaName: The name of the schema. Either `SchemaArn` or `SchemaName` and `RegistryName` has to be provided.
Type: [SchemaId](API_SchemaId.md) object
Required: No

 ** [SchemaVersionId](#API_GetSchemaVersion_RequestSyntax) **   <a name="Glue-GetSchemaVersion-request-SchemaVersionId"></a>
The `SchemaVersionId` of the schema version. This field is required for fetching by schema ID. Either this or the `SchemaId` wrapper has to be provided.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** [SchemaVersionNumber](#API_GetSchemaVersion_RequestSyntax) **   <a name="Glue-GetSchemaVersion-request-SchemaVersionNumber"></a>
The version number of the schema.
Type: [SchemaVersionNumber](API_SchemaVersionNumber.md) object
Required: No

## Response Syntax
<a name="API_GetSchemaVersion_ResponseSyntax"></a>

```
{
   "CreatedTime": "string",
   "DataFormat": "string",
   "SchemaArn": "string",
   "SchemaDefinition": "string",
   "SchemaVersionId": "string",
   "Status": "string",
   "VersionNumber": number
}
```

## Response Elements
<a name="API_GetSchemaVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTime](#API_GetSchemaVersion_ResponseSyntax) **   <a name="Glue-GetSchemaVersion-response-CreatedTime"></a>
The date and time the schema version was created.
Type: String

 ** [DataFormat](#API_GetSchemaVersion_ResponseSyntax) **   <a name="Glue-GetSchemaVersion-response-DataFormat"></a>
The data format of the schema definition. Currently `AVRO`, `JSON` and `PROTOBUF` are supported.
Type: String
Valid Values: `AVRO | JSON | PROTOBUF`

 ** [SchemaArn](#API_GetSchemaVersion_ResponseSyntax) **   <a name="Glue-GetSchemaVersion-response-SchemaArn"></a>
The Amazon Resource Name (ARN) of the schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Pattern: `arn:aws(-(cn|us-gov|iso(-[bef])?))?:glue:.*`

 ** [SchemaDefinition](#API_GetSchemaVersion_ResponseSyntax) **   <a name="Glue-GetSchemaVersion-response-SchemaDefinition"></a>
The schema definition for the schema ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 170000.
Pattern: `.*\S.*`

 ** [SchemaVersionId](#API_GetSchemaVersion_ResponseSyntax) **   <a name="Glue-GetSchemaVersion-response-SchemaVersionId"></a>
The `SchemaVersionId` of the schema version.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [Status](#API_GetSchemaVersion_ResponseSyntax) **   <a name="Glue-GetSchemaVersion-response-Status"></a>
The status of the schema version.
Type: String
Valid Values: `AVAILABLE | PENDING | FAILURE | DELETING`

 ** [VersionNumber](#API_GetSchemaVersion_ResponseSyntax) **   <a name="Glue-GetSchemaVersion-response-VersionNumber"></a>
The version number of the schema.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.

## Errors
<a name="API_GetSchemaVersion_Errors"></a>

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

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetSchemaVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetSchemaVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetSchemaVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetSchemaVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetSchemaVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetSchemaVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetSchemaVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetSchemaVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetSchemaVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetSchemaVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetSchemaVersion)
