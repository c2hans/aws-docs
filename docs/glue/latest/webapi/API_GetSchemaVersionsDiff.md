---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetSchemaVersionsDiff.html
---

# GetSchemaVersionsDiff
<a name="API_GetSchemaVersionsDiff"></a>

Fetches the schema version difference in the specified difference type between two stored schema versions in the Schema Registry.

This API allows you to compare two schema versions between two schema definitions under the same schema.

## Request Syntax
<a name="API_GetSchemaVersionsDiff_RequestSyntax"></a>

```
{
   "FirstSchemaVersionNumber": {
      "LatestVersion": {{boolean}},
      "VersionNumber": {{number}}
   },
   "SchemaDiffType": "{{string}}",
   "SchemaId": {
      "RegistryName": "{{string}}",
      "SchemaArn": "{{string}}",
      "SchemaName": "{{string}}"
   },
   "SecondSchemaVersionNumber": {
      "LatestVersion": {{boolean}},
      "VersionNumber": {{number}}
   }
}
```

## Request Parameters
<a name="API_GetSchemaVersionsDiff_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FirstSchemaVersionNumber](#API_GetSchemaVersionsDiff_RequestSyntax) **   <a name="Glue-GetSchemaVersionsDiff-request-FirstSchemaVersionNumber"></a>
The first of the two schema versions to be compared.
Type: [SchemaVersionNumber](API_SchemaVersionNumber.md) object
Required: Yes

 ** [SchemaDiffType](#API_GetSchemaVersionsDiff_RequestSyntax) **   <a name="Glue-GetSchemaVersionsDiff-request-SchemaDiffType"></a>
Refers to `SYNTAX_DIFF`, which is the currently supported diff type.
Type: String
Valid Values: `SYNTAX_DIFF`
Required: Yes

 ** [SchemaId](#API_GetSchemaVersionsDiff_RequestSyntax) **   <a name="Glue-GetSchemaVersionsDiff-request-SchemaId"></a>
This is a wrapper structure to contain schema identity fields. The structure contains:
+ SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. One of `SchemaArn` or `SchemaName` has to be provided.
+ SchemaId$SchemaName: The name of the schema. One of `SchemaArn` or `SchemaName` has to be provided.
Type: [SchemaId](API_SchemaId.md) object
Required: Yes

 ** [SecondSchemaVersionNumber](#API_GetSchemaVersionsDiff_RequestSyntax) **   <a name="Glue-GetSchemaVersionsDiff-request-SecondSchemaVersionNumber"></a>
The second of the two schema versions to be compared.
Type: [SchemaVersionNumber](API_SchemaVersionNumber.md) object
Required: Yes

## Response Syntax
<a name="API_GetSchemaVersionsDiff_ResponseSyntax"></a>

```
{
   "Diff": "string"
}
```

## Response Elements
<a name="API_GetSchemaVersionsDiff_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Diff](#API_GetSchemaVersionsDiff_ResponseSyntax) **   <a name="Glue-GetSchemaVersionsDiff-response-Diff"></a>
The difference between schemas as a string in JsonPatch format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 340000.
Pattern: `.*\S.*`

## Errors
<a name="API_GetSchemaVersionsDiff_Errors"></a>

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
<a name="API_GetSchemaVersionsDiff_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetSchemaVersionsDiff)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetSchemaVersionsDiff)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetSchemaVersionsDiff)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetSchemaVersionsDiff)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetSchemaVersionsDiff)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetSchemaVersionsDiff)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetSchemaVersionsDiff)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetSchemaVersionsDiff)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetSchemaVersionsDiff)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetSchemaVersionsDiff)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
