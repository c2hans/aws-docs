---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_ListDatasets.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# ListDatasets
<a name="API_ListDatasets"></a>

Lists all of the active Datasets that a user has access to.

## Request Syntax
<a name="API_ListDatasets_RequestSyntax"></a>

```
GET /datasetsv2?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDatasets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListDatasets_RequestSyntax) **   <a name="finspace-ListDatasets-request-uri-maxResults"></a>
The maximum number of results per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListDatasets_RequestSyntax) **   <a name="finspace-ListDatasets-request-uri-nextToken"></a>
A token that indicates where a results page should begin.

## Request Body
<a name="API_ListDatasets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDatasets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "datasets": [
      {
         "alias": "string",
         "createTime": number,
         "datasetArn": "string",
         "datasetDescription": "string",
         "datasetId": "string",
         "datasetTitle": "string",
         "kind": "string",
         "lastModifiedTime": number,
         "ownerInfo": {
            "email": "string",
            "name": "string",
            "phoneNumber": "string"
         },
         "schemaDefinition": {
            "tabularSchemaConfig": {
               "columns": [
                  {
                     "columnDescription": "string",
                     "columnName": "string",
                     "dataType": "string"
                  }
               ],
               "primaryKeyColumns": [ "string" ]
            }
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDatasets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [datasets](#API_ListDatasets_ResponseSyntax) **   <a name="finspace-ListDatasets-response-datasets"></a>
List of Datasets.
Type: Array of [Dataset](API_Dataset.md) objects

 ** [nextToken](#API_ListDatasets_ResponseSyntax) **   <a name="finspace-ListDatasets-response-nextToken"></a>
A token that indicates where a results page should begin.
Type: String

## Errors
<a name="API_ListDatasets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_ListDatasets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2020-07-13/ListDatasets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2020-07-13/ListDatasets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/ListDatasets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2020-07-13/ListDatasets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/ListDatasets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2020-07-13/ListDatasets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2020-07-13/ListDatasets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2020-07-13/ListDatasets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2020-07-13/ListDatasets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/ListDatasets)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
