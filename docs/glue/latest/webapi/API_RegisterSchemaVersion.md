---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_RegisterSchemaVersion.html
---

# RegisterSchemaVersion
<a name="API_RegisterSchemaVersion"></a>

Adds a new version to the existing schema. Returns an error if new version of schema does not meet the compatibility requirements of the schema set. This API will not create a new schema set and will return a 404 error if the schema set is not already present in the Schema Registry.

If this is the first schema definition to be registered in the Schema Registry, this API will store the schema version and return immediately. Otherwise, this call has the potential to run longer than other operations due to compatibility modes. You can call the `GetSchemaVersion` API with the `SchemaVersionId` to check compatibility modes.

If the same schema definition is already stored in Schema Registry as a version, the schema ID of the existing schema is returned to the caller.

## Request Syntax
<a name="API_RegisterSchemaVersion_RequestSyntax"></a>

```
{
   "SchemaDefinition": "{{string}}",
   "SchemaId": {
      "RegistryName": "{{string}}",
      "SchemaArn": "{{string}}",
      "SchemaName": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_RegisterSchemaVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SchemaDefinition](#API_RegisterSchemaVersion_RequestSyntax) **   <a name="Glue-RegisterSchemaVersion-request-SchemaDefinition"></a>
The schema definition using the `DataFormat` setting for the `SchemaName`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 170000.
Pattern: `.*\S.*`
Required: Yes

 ** [SchemaId](#API_RegisterSchemaVersion_RequestSyntax) **   <a name="Glue-RegisterSchemaVersion-request-SchemaId"></a>
This is a wrapper structure to contain schema identity fields. The structure contains:
+ SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. Either `SchemaArn` or `SchemaName` and `RegistryName` has to be provided.
+ SchemaId$SchemaName: The name of the schema. Either `SchemaArn` or `SchemaName` and `RegistryName` has to be provided.
Type: [SchemaId](API_SchemaId.md) object
Required: Yes

## Response Syntax
<a name="API_RegisterSchemaVersion_ResponseSyntax"></a>

```
{
   "SchemaVersionId": "string",
   "Status": "string",
   "VersionNumber": number
}
```

## Response Elements
<a name="API_RegisterSchemaVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SchemaVersionId](#API_RegisterSchemaVersion_ResponseSyntax) **   <a name="Glue-RegisterSchemaVersion-response-SchemaVersionId"></a>
The unique ID that represents the version of this schema.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [Status](#API_RegisterSchemaVersion_ResponseSyntax) **   <a name="Glue-RegisterSchemaVersion-response-Status"></a>
The status of the schema version.
Type: String
Valid Values: `AVAILABLE | PENDING | FAILURE | DELETING`

 ** [VersionNumber](#API_RegisterSchemaVersion_ResponseSyntax) **   <a name="Glue-RegisterSchemaVersion-response-VersionNumber"></a>
The version of this schema (for sync flow only, in case this is the first version).
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.

## Errors
<a name="API_RegisterSchemaVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
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
<a name="API_RegisterSchemaVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/RegisterSchemaVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/RegisterSchemaVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/RegisterSchemaVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/RegisterSchemaVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/RegisterSchemaVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/RegisterSchemaVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/RegisterSchemaVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/RegisterSchemaVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/RegisterSchemaVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/RegisterSchemaVersion)
