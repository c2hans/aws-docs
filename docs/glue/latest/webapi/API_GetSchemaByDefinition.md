---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetSchemaByDefinition.html
---

# GetSchemaByDefinition
<a name="API_GetSchemaByDefinition"></a>

Retrieves a schema by the `SchemaDefinition`. The schema definition is sent to the Schema Registry, canonicalized, and hashed. If the hash is matched within the scope of the `SchemaName` or ARN (or the default registry, if none is supplied), that schema’s metadata is returned. Otherwise, a 404 or NotFound error is returned. Schema versions in `Deleted` statuses will not be included in the results.

## Request Syntax
<a name="API_GetSchemaByDefinition_RequestSyntax"></a>

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
<a name="API_GetSchemaByDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SchemaDefinition](#API_GetSchemaByDefinition_RequestSyntax) **   <a name="Glue-GetSchemaByDefinition-request-SchemaDefinition"></a>
The definition of the schema for which schema details are required.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 170000.
Pattern: `.*\S.*`
Required: Yes

 ** [SchemaId](#API_GetSchemaByDefinition_RequestSyntax) **   <a name="Glue-GetSchemaByDefinition-request-SchemaId"></a>
This is a wrapper structure to contain schema identity fields. The structure contains:
+ SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. One of `SchemaArn` or `SchemaName` has to be provided.
+ SchemaId$SchemaName: The name of the schema. One of `SchemaArn` or `SchemaName` has to be provided.
Type: [SchemaId](API_SchemaId.md) object
Required: Yes

## Response Syntax
<a name="API_GetSchemaByDefinition_ResponseSyntax"></a>

```
{
   "CreatedTime": "string",
   "DataFormat": "string",
   "SchemaArn": "string",
   "SchemaVersionId": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_GetSchemaByDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTime](#API_GetSchemaByDefinition_ResponseSyntax) **   <a name="Glue-GetSchemaByDefinition-response-CreatedTime"></a>
The date and time the schema was created.
Type: String

 ** [DataFormat](#API_GetSchemaByDefinition_ResponseSyntax) **   <a name="Glue-GetSchemaByDefinition-response-DataFormat"></a>
The data format of the schema definition. Currently `AVRO`, `JSON` and `PROTOBUF` are supported.
Type: String
Valid Values: `AVRO | JSON | PROTOBUF`

 ** [SchemaArn](#API_GetSchemaByDefinition_ResponseSyntax) **   <a name="Glue-GetSchemaByDefinition-response-SchemaArn"></a>
The Amazon Resource Name (ARN) of the schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Pattern: `arn:aws(-(cn|us-gov|iso(-[bef])?))?:glue:.*`

 ** [SchemaVersionId](#API_GetSchemaByDefinition_ResponseSyntax) **   <a name="Glue-GetSchemaByDefinition-response-SchemaVersionId"></a>
The schema ID of the schema version.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [Status](#API_GetSchemaByDefinition_ResponseSyntax) **   <a name="Glue-GetSchemaByDefinition-response-Status"></a>
The status of the schema version.
Type: String
Valid Values: `AVAILABLE | PENDING | FAILURE | DELETING`

## Errors
<a name="API_GetSchemaByDefinition_Errors"></a>

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
<a name="API_GetSchemaByDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetSchemaByDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetSchemaByDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetSchemaByDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetSchemaByDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetSchemaByDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetSchemaByDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetSchemaByDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetSchemaByDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetSchemaByDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetSchemaByDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
