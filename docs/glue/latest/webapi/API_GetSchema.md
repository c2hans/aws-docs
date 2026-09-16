---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetSchema.html
---

# GetSchema
<a name="API_GetSchema"></a>

Describes the specified schema in detail.

## Request Syntax
<a name="API_GetSchema_RequestSyntax"></a>

```
{
   "SchemaId": {
      "RegistryName": "{{string}}",
      "SchemaArn": "{{string}}",
      "SchemaName": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_GetSchema_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SchemaId](#API_GetSchema_RequestSyntax) **   <a name="Glue-GetSchema-request-SchemaId"></a>
This is a wrapper structure to contain schema identity fields. The structure contains:
+ SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. Either `SchemaArn` or `SchemaName` and `RegistryName` has to be provided.
+ SchemaId$SchemaName: The name of the schema. Either `SchemaArn` or `SchemaName` and `RegistryName` has to be provided.
Type: [SchemaId](API_SchemaId.md) object
Required: Yes

## Response Syntax
<a name="API_GetSchema_ResponseSyntax"></a>

```
{
   "Compatibility": "string",
   "CreatedTime": "string",
   "DataFormat": "string",
   "Description": "string",
   "LatestSchemaVersion": number,
   "NextSchemaVersion": number,
   "RegistryArn": "string",
   "RegistryName": "string",
   "SchemaArn": "string",
   "SchemaCheckpoint": number,
   "SchemaName": "string",
   "SchemaStatus": "string",
   "UpdatedTime": "string"
}
```

## Response Elements
<a name="API_GetSchema_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Compatibility](#API_GetSchema_ResponseSyntax) **   <a name="Glue-GetSchema-response-Compatibility"></a>
The compatibility mode of the schema.
Type: String
Valid Values: `NONE | DISABLED | BACKWARD | BACKWARD_ALL | FORWARD | FORWARD_ALL | FULL | FULL_ALL`

 ** [CreatedTime](#API_GetSchema_ResponseSyntax) **   <a name="Glue-GetSchema-response-CreatedTime"></a>
The date and time the schema was created.
Type: String

 ** [DataFormat](#API_GetSchema_ResponseSyntax) **   <a name="Glue-GetSchema-response-DataFormat"></a>
The data format of the schema definition. Currently `AVRO`, `JSON` and `PROTOBUF` are supported.
Type: String
Valid Values: `AVRO | JSON | PROTOBUF`

 ** [Description](#API_GetSchema_ResponseSyntax) **   <a name="Glue-GetSchema-response-Description"></a>
A description of schema if specified when created
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

 ** [LatestSchemaVersion](#API_GetSchema_ResponseSyntax) **   <a name="Glue-GetSchema-response-LatestSchemaVersion"></a>
The latest version of the schema associated with the returned schema definition.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.

 ** [NextSchemaVersion](#API_GetSchema_ResponseSyntax) **   <a name="Glue-GetSchema-response-NextSchemaVersion"></a>
The next version of the schema associated with the returned schema definition.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.

 ** [RegistryArn](#API_GetSchema_ResponseSyntax) **   <a name="Glue-GetSchema-response-RegistryArn"></a>
The Amazon Resource Name (ARN) of the registry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Pattern: `arn:aws(-(cn|us-gov|iso(-[bef])?))?:glue:.*`

 ** [RegistryName](#API_GetSchema_ResponseSyntax) **   <a name="Glue-GetSchema-response-RegistryName"></a>
The name of the registry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-_$#.]+`

 ** [SchemaArn](#API_GetSchema_ResponseSyntax) **   <a name="Glue-GetSchema-response-SchemaArn"></a>
The Amazon Resource Name (ARN) of the schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Pattern: `arn:aws(-(cn|us-gov|iso(-[bef])?))?:glue:.*`

 ** [SchemaCheckpoint](#API_GetSchema_ResponseSyntax) **   <a name="Glue-GetSchema-response-SchemaCheckpoint"></a>
The version number of the checkpoint (the last time the compatibility mode was changed).
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.

 ** [SchemaName](#API_GetSchema_ResponseSyntax) **   <a name="Glue-GetSchema-response-SchemaName"></a>
The name of the schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-_$#.]+`

 ** [SchemaStatus](#API_GetSchema_ResponseSyntax) **   <a name="Glue-GetSchema-response-SchemaStatus"></a>
The status of the schema.
Type: String
Valid Values: `AVAILABLE | PENDING | DELETING`

 ** [UpdatedTime](#API_GetSchema_ResponseSyntax) **   <a name="Glue-GetSchema-response-UpdatedTime"></a>
The date and time the schema was updated.
Type: String

## Errors
<a name="API_GetSchema_Errors"></a>

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
<a name="API_GetSchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetSchema)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetSchema)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetSchema)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetSchema)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetSchema)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetSchema)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetSchema)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetSchema)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetSchema)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetSchema)
