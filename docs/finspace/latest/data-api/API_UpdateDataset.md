---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_UpdateDataset.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# UpdateDataset
<a name="API_UpdateDataset"></a>

Updates a FinSpace Dataset.

## Request Syntax
<a name="API_UpdateDataset_RequestSyntax"></a>

```
PUT /datasetsv2/{{datasetId}} HTTP/1.1
Content-type: application/json

{
   "alias": "{{string}}",
   "clientToken": "{{string}}",
   "datasetDescription": "{{string}}",
   "datasetTitle": "{{string}}",
   "kind": "{{string}}",
   "schemaDefinition": {
      "tabularSchemaConfig": {
         "columns": [
            {
               "columnDescription": "{{string}}",
               "columnName": "{{string}}",
               "dataType": "{{string}}"
            }
         ],
         "primaryKeyColumns": [ "{{string}}" ]
      }
   }
}
```

## URI Request Parameters
<a name="API_UpdateDataset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datasetId](#API_UpdateDataset_RequestSyntax) **   <a name="finspace-UpdateDataset-request-uri-datasetId"></a>
The unique identifier for the Dataset to update.
Length Constraints: Minimum length of 1. Maximum length of 26.
Required: Yes

## Request Body
<a name="API_UpdateDataset_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [datasetTitle](#API_UpdateDataset_RequestSyntax) **   <a name="finspace-UpdateDataset-request-datasetTitle"></a>
A display title for the Dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*\S.*`
Required: Yes

 ** [kind](#API_UpdateDataset_RequestSyntax) **   <a name="finspace-UpdateDataset-request-kind"></a>
The format in which the Dataset data is structured.
+  `TABULAR` – Data is structured in a tabular format.
+  `NON_TABULAR` – Data is structured in a non-tabular format.
Type: String
Valid Values: `TABULAR | NON_TABULAR`
Required: Yes

 ** [alias](#API_UpdateDataset_RequestSyntax) **   <a name="finspace-UpdateDataset-request-alias"></a>
The unique resource identifier for a Dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^alias\/\S+`
Required: No

 ** [clientToken](#API_UpdateDataset_RequestSyntax) **   <a name="finspace-UpdateDataset-request-clientToken"></a>
A token that ensures idempotency. This token expires in 10 minutes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

 ** [datasetDescription](#API_UpdateDataset_RequestSyntax) **   <a name="finspace-UpdateDataset-request-datasetDescription"></a>
A description for the Dataset.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `[\s\S]*`
Required: No

 ** [schemaDefinition](#API_UpdateDataset_RequestSyntax) **   <a name="finspace-UpdateDataset-request-schemaDefinition"></a>
Definition for a schema on a tabular Dataset.
Type: [SchemaUnion](API_SchemaUnion.md) object
Required: No

## Response Syntax
<a name="API_UpdateDataset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "datasetId": "string"
}
```

## Response Elements
<a name="API_UpdateDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [datasetId](#API_UpdateDataset_ResponseSyntax) **   <a name="finspace-UpdateDataset-response-datasetId"></a>
The unique identifier for updated Dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.

## Errors
<a name="API_UpdateDataset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with an existing resource.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2020-07-13/UpdateDataset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2020-07-13/UpdateDataset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/UpdateDataset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2020-07-13/UpdateDataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/UpdateDataset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2020-07-13/UpdateDataset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2020-07-13/UpdateDataset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2020-07-13/UpdateDataset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2020-07-13/UpdateDataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/UpdateDataset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
