---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CheckSchemaVersionValidity.html
---

# CheckSchemaVersionValidity
<a name="API_CheckSchemaVersionValidity"></a>

Validates the supplied schema. This call has no side effects, it simply validates using the supplied schema using `DataFormat` as the format. Since it does not take a schema set name, no compatibility checks are performed.

## Request Syntax
<a name="API_CheckSchemaVersionValidity_RequestSyntax"></a>

```
{
   "DataFormat": "{{string}}",
   "SchemaDefinition": "{{string}}"
}
```

## Request Parameters
<a name="API_CheckSchemaVersionValidity_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DataFormat](#API_CheckSchemaVersionValidity_RequestSyntax) **   <a name="Glue-CheckSchemaVersionValidity-request-DataFormat"></a>
The data format of the schema definition. Currently `AVRO`, `JSON` and `PROTOBUF` are supported.
Type: String
Valid Values: `AVRO | JSON | PROTOBUF`
Required: Yes

 ** [SchemaDefinition](#API_CheckSchemaVersionValidity_RequestSyntax) **   <a name="Glue-CheckSchemaVersionValidity-request-SchemaDefinition"></a>
The definition of the schema that has to be validated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 170000.
Pattern: `.*\S.*`
Required: Yes

## Response Syntax
<a name="API_CheckSchemaVersionValidity_ResponseSyntax"></a>

```
{
   "Error": "string",
   "Valid": boolean
}
```

## Response Elements
<a name="API_CheckSchemaVersionValidity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Error](#API_CheckSchemaVersionValidity_ResponseSyntax) **   <a name="Glue-CheckSchemaVersionValidity-response-Error"></a>
A validation failure error message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5000.

 ** [Valid](#API_CheckSchemaVersionValidity_ResponseSyntax) **   <a name="Glue-CheckSchemaVersionValidity-response-Valid"></a>
Return true, if the schema is valid and false otherwise.
Type: Boolean

## Errors
<a name="API_CheckSchemaVersionValidity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
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
<a name="API_CheckSchemaVersionValidity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/CheckSchemaVersionValidity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/CheckSchemaVersionValidity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CheckSchemaVersionValidity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/CheckSchemaVersionValidity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CheckSchemaVersionValidity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/CheckSchemaVersionValidity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/CheckSchemaVersionValidity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/CheckSchemaVersionValidity)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/CheckSchemaVersionValidity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CheckSchemaVersionValidity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
