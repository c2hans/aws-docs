---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CreateSchema.html
---

# CreateSchema
<a name="API_CreateSchema"></a>

Creates a new schema set and registers the schema definition. Returns an error if the schema set already exists without actually registering the version.

When the schema set is created, a version checkpoint will be set to the first version. Compatibility mode "DISABLED" restricts any additional schema versions from being added after the first schema version. For all other compatibility modes, validation of compatibility settings will be applied only from the second version onwards when the `RegisterSchemaVersion` API is used.

When this API is called without a `RegistryId`, this will create an entry for a "default-registry" in the registry database tables, if it is not already present.

## Request Syntax
<a name="API_CreateSchema_RequestSyntax"></a>

```
{
   "Compatibility": "{{string}}",
   "DataFormat": "{{string}}",
   "Description": "{{string}}",
   "RegistryId": {
      "RegistryArn": "{{string}}",
      "RegistryName": "{{string}}"
   },
   "SchemaDefinition": "{{string}}",
   "SchemaName": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateSchema_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Compatibility](#API_CreateSchema_RequestSyntax) **   <a name="Glue-CreateSchema-request-Compatibility"></a>
The compatibility mode of the schema. The possible values are:
+  *NONE*: No compatibility mode applies. You can use this choice in development scenarios or if you do not know the compatibility mode that you want to apply to schemas. Any new version added will be accepted without undergoing a compatibility check.
+  *DISABLED*: This compatibility choice prevents versioning for a particular schema. You can use this choice to prevent future versioning of a schema.
+  *BACKWARD*: This compatibility choice is recommended as it allows data receivers to read both the current and one previous schema version. This means that for instance, a new schema version cannot drop data fields or change the type of these fields, so they can't be read by readers using the previous version.
+  *BACKWARD\_ALL*: This compatibility choice allows data receivers to read both the current and all previous schema versions. You can use this choice when you need to delete fields or add optional fields, and check compatibility against all previous schema versions.
+  *FORWARD*: This compatibility choice allows data receivers to read both the current and one next schema version, but not necessarily later versions. You can use this choice when you need to add fields or delete optional fields, but only check compatibility against the last schema version.
+  *FORWARD\_ALL*: This compatibility choice allows data receivers to read written by producers of any new registered schema. You can use this choice when you need to add fields or delete optional fields, and check compatibility against all previous schema versions.
+  *FULL*: This compatibility choice allows data receivers to read data written by producers using the previous or next version of the schema, but not necessarily earlier or later versions. You can use this choice when you need to add or remove optional fields, but only check compatibility against the last schema version.
+  *FULL\_ALL*: This compatibility choice allows data receivers to read data written by producers using all previous schema versions. You can use this choice when you need to add or remove optional fields, and check compatibility against all previous schema versions.
Type: String
Valid Values: `NONE | DISABLED | BACKWARD | BACKWARD_ALL | FORWARD | FORWARD_ALL | FULL | FULL_ALL`
Required: No

 ** [DataFormat](#API_CreateSchema_RequestSyntax) **   <a name="Glue-CreateSchema-request-DataFormat"></a>
The data format of the schema definition. Currently `AVRO`, `JSON` and `PROTOBUF` are supported.
Type: String
Valid Values: `AVRO | JSON | PROTOBUF`
Required: Yes

 ** [Description](#API_CreateSchema_RequestSyntax) **   <a name="Glue-CreateSchema-request-Description"></a>
An optional description of the schema. If description is not provided, there will not be any automatic default value for this.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** [RegistryId](#API_CreateSchema_RequestSyntax) **   <a name="Glue-CreateSchema-request-RegistryId"></a>
 This is a wrapper shape to contain the registry identity fields. If this is not provided, the default registry will be used. The ARN format for the same will be: `arn:aws:glue:us-east-2:<customer id>:registry/default-registry:random-5-letter-id`.
Type: [RegistryId](API_RegistryId.md) object
Required: No

 ** [SchemaDefinition](#API_CreateSchema_RequestSyntax) **   <a name="Glue-CreateSchema-request-SchemaDefinition"></a>
The schema definition using the `DataFormat` setting for `SchemaName`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 170000.
Pattern: `.*\S.*`
Required: No

 ** [SchemaName](#API_CreateSchema_RequestSyntax) **   <a name="Glue-CreateSchema-request-SchemaName"></a>
Name of the schema to be created of max length of 255, and may only contain letters, numbers, hyphen, underscore, dollar sign, or hash mark. No whitespace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-_$#.]+`
Required: Yes

 ** [Tags](#API_CreateSchema_RequestSyntax) **   <a name="Glue-CreateSchema-request-Tags"></a>
 AWS tags that contain a key value pair and may be searched by console, command line, or API. If specified, follows the AWS tags-on-create pattern.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateSchema_ResponseSyntax"></a>

```
{
   "Compatibility": "string",
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
   "SchemaVersionId": "string",
   "SchemaVersionStatus": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_CreateSchema_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Compatibility](#API_CreateSchema_ResponseSyntax) **   <a name="Glue-CreateSchema-response-Compatibility"></a>
The schema compatibility mode.
Type: String
Valid Values: `NONE | DISABLED | BACKWARD | BACKWARD_ALL | FORWARD | FORWARD_ALL | FULL | FULL_ALL`

 ** [DataFormat](#API_CreateSchema_ResponseSyntax) **   <a name="Glue-CreateSchema-response-DataFormat"></a>
The data format of the schema definition. Currently `AVRO`, `JSON` and `PROTOBUF` are supported.
Type: String
Valid Values: `AVRO | JSON | PROTOBUF`

 ** [Description](#API_CreateSchema_ResponseSyntax) **   <a name="Glue-CreateSchema-response-Description"></a>
A description of the schema if specified when created.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

 ** [LatestSchemaVersion](#API_CreateSchema_ResponseSyntax) **   <a name="Glue-CreateSchema-response-LatestSchemaVersion"></a>
The latest version of the schema associated with the returned schema definition.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.

 ** [NextSchemaVersion](#API_CreateSchema_ResponseSyntax) **   <a name="Glue-CreateSchema-response-NextSchemaVersion"></a>
The next version of the schema associated with the returned schema definition.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.

 ** [RegistryArn](#API_CreateSchema_ResponseSyntax) **   <a name="Glue-CreateSchema-response-RegistryArn"></a>
The Amazon Resource Name (ARN) of the registry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Pattern: `arn:aws(-(cn|us-gov|iso(-[bef])?))?:glue:.*`

 ** [RegistryName](#API_CreateSchema_ResponseSyntax) **   <a name="Glue-CreateSchema-response-RegistryName"></a>
The name of the registry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-_$#.]+`

 ** [SchemaArn](#API_CreateSchema_ResponseSyntax) **   <a name="Glue-CreateSchema-response-SchemaArn"></a>
The Amazon Resource Name (ARN) of the schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Pattern: `arn:aws(-(cn|us-gov|iso(-[bef])?))?:glue:.*`

 ** [SchemaCheckpoint](#API_CreateSchema_ResponseSyntax) **   <a name="Glue-CreateSchema-response-SchemaCheckpoint"></a>
The version number of the checkpoint (the last time the compatibility mode was changed).
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.

 ** [SchemaName](#API_CreateSchema_ResponseSyntax) **   <a name="Glue-CreateSchema-response-SchemaName"></a>
The name of the schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-_$#.]+`

 ** [SchemaStatus](#API_CreateSchema_ResponseSyntax) **   <a name="Glue-CreateSchema-response-SchemaStatus"></a>
The status of the schema.
Type: String
Valid Values: `AVAILABLE | PENDING | DELETING`

 ** [SchemaVersionId](#API_CreateSchema_ResponseSyntax) **   <a name="Glue-CreateSchema-response-SchemaVersionId"></a>
The unique identifier of the first schema version.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [SchemaVersionStatus](#API_CreateSchema_ResponseSyntax) **   <a name="Glue-CreateSchema-response-SchemaVersionStatus"></a>
The status of the first schema version created.
Type: String
Valid Values: `AVAILABLE | PENDING | FAILURE | DELETING`

 ** [Tags](#API_CreateSchema_ResponseSyntax) **   <a name="Glue-CreateSchema-response-Tags"></a>
The tags for the schema.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_CreateSchema_Errors"></a>

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

 ** ConcurrentModificationException **
Two processes are trying to modify a resource simultaneously.
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

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_CreateSchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/CreateSchema)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/CreateSchema)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CreateSchema)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/CreateSchema)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CreateSchema)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/CreateSchema)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/CreateSchema)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/CreateSchema)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/CreateSchema)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CreateSchema)
