---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ListSchemas.html
---

# ListSchemas
<a name="API_ListSchemas"></a>

Returns a list of schemas with minimal details. Schemas in Deleting status will not be included in the results. Empty results will be returned if there are no schemas available.

When the `RegistryId` is not provided, all the schemas across registries will be part of the API response.

## Request Syntax
<a name="API_ListSchemas_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "RegistryId": {
      "RegistryArn": "{{string}}",
      "RegistryName": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_ListSchemas_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListSchemas_RequestSyntax) **   <a name="Glue-ListSchemas-request-MaxResults"></a>
Maximum number of results required per page. If the value is not supplied, this will be defaulted to 25 per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListSchemas_RequestSyntax) **   <a name="Glue-ListSchemas-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

 ** [RegistryId](#API_ListSchemas_RequestSyntax) **   <a name="Glue-ListSchemas-request-RegistryId"></a>
A wrapper structure that may contain the registry name and Amazon Resource Name (ARN).
Type: [RegistryId](API_RegistryId.md) object
Required: No

## Response Syntax
<a name="API_ListSchemas_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Schemas": [
      {
         "CreatedTime": "string",
         "Description": "string",
         "RegistryName": "string",
         "SchemaArn": "string",
         "SchemaName": "string",
         "SchemaStatus": "string",
         "UpdatedTime": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSchemas_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListSchemas_ResponseSyntax) **   <a name="Glue-ListSchemas-response-NextToken"></a>
A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last.
Type: String

 ** [Schemas](#API_ListSchemas_ResponseSyntax) **   <a name="Glue-ListSchemas-response-Schemas"></a>
An array of `SchemaListItem` objects containing details of each schema.
Type: Array of [SchemaListItem](API_SchemaListItem.md) objects

## Errors
<a name="API_ListSchemas_Errors"></a>

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
<a name="API_ListSchemas_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/ListSchemas)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/ListSchemas)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ListSchemas)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/ListSchemas)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ListSchemas)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/ListSchemas)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/ListSchemas)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/ListSchemas)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/ListSchemas)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ListSchemas)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
