---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ListSchemaMappings.html
---

# ListSchemaMappings
<a name="API_ListSchemaMappings"></a>

Returns a list of all the `SchemaMappings` that have been created for an AWS account.

## Request Syntax
<a name="API_ListSchemaMappings_RequestSyntax"></a>

```
GET /schemas?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSchemaMappings_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListSchemaMappings_RequestSyntax) **   <a name="API-ListSchemaMappings-request-uri-maxResults"></a>
The maximum number of objects returned per page.
Valid Range: Maximum value of 25.

 ** [nextToken](#API_ListSchemaMappings_RequestSyntax) **   <a name="API-ListSchemaMappings-request-uri-nextToken"></a>
The pagination token from the previous API call.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z_0-9-=+/]*`

## Request Body
<a name="API_ListSchemaMappings_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSchemaMappings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "schemaList": [
      {
         "createdAt": number,
         "hasWorkflows": boolean,
         "schemaArn": "string",
         "schemaName": "string",
         "updatedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_ListSchemaMappings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSchemaMappings_ResponseSyntax) **   <a name="API-ListSchemaMappings-response-nextToken"></a>
The pagination token from the previous API call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z_0-9-=+/]*`

 ** [schemaList](#API_ListSchemaMappings_ResponseSyntax) **   <a name="API-ListSchemaMappings-response-schemaList"></a>
A list of `SchemaMappingSummary` objects, each of which contain the fields `SchemaName`, `SchemaArn`, `CreatedAt`, `UpdatedAt`.
Type: Array of [SchemaMappingSummary](API_SchemaMappingSummary.md) objects

## Errors
<a name="API_ListSchemaMappings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Entity Resolution service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by AWS Entity Resolution.
HTTP Status Code: 400

## See Also
<a name="API_ListSchemaMappings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/ListSchemaMappings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/ListSchemaMappings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/ListSchemaMappings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/ListSchemaMappings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/ListSchemaMappings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/ListSchemaMappings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/ListSchemaMappings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/ListSchemaMappings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/ListSchemaMappings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/ListSchemaMappings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
