---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListNotebooks.html
---

# ListNotebooks
<a name="API_ListNotebooks"></a>

Lists [notebooks](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html) in Amazon SageMaker Unified Studio.

## Request Syntax
<a name="API_ListNotebooks_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/notebooks?maxResults={{maxResults}}&nextToken={{nextToken}}&owningProjectIdentifier={{owningProjectIdentifier}}&sortBy={{sortBy}}&sortOrder={{sortOrder}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListNotebooks_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_ListNotebooks_RequestSyntax) **   <a name="datazone-ListNotebooks-request-uri-domainIdentifier"></a>
The identifier of the Amazon SageMaker Unified Studio domain in which to list notebooks.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [maxResults](#API_ListNotebooks_RequestSyntax) **   <a name="datazone-ListNotebooks-request-uri-maxResults"></a>
The maximum number of notebooks to return in a single call. When the number of notebooks exceeds the value of `MaxResults`, the response contains a `NextToken` value.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListNotebooks_RequestSyntax) **   <a name="datazone-ListNotebooks-request-uri-nextToken"></a>
When the number of notebooks is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of notebooks, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListNotebooks` to list the next set of notebooks.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [owningProjectIdentifier](#API_ListNotebooks_RequestSyntax) **   <a name="datazone-ListNotebooks-request-uri-owningProjectIdentifier"></a>
The identifier of the project that owns the notebooks.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [sortBy](#API_ListNotebooks_RequestSyntax) **   <a name="datazone-ListNotebooks-request-uri-sortBy"></a>
The field to sort the results by.
Valid Values: `CREATED_AT | UPDATED_AT`

 ** [sortOrder](#API_ListNotebooks_RequestSyntax) **   <a name="datazone-ListNotebooks-request-uri-sortOrder"></a>
The sort order for the results.
Valid Values: `ASCENDING | DESCENDING`

 ** [status](#API_ListNotebooks_RequestSyntax) **   <a name="datazone-ListNotebooks-request-uri-status"></a>
The status to filter notebooks by.
Valid Values: `ACTIVE | ARCHIVED | SYNC_IN_PROGRESS | SYNC_FAILED`

## Request Body
<a name="API_ListNotebooks_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListNotebooks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "createdAt": number,
         "createdBy": "string",
         "description": "string",
         "domainId": "string",
         "id": "string",
         "name": "string",
         "owningProjectId": "string",
         "status": "string",
         "updatedAt": number,
         "updatedBy": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListNotebooks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListNotebooks_ResponseSyntax) **   <a name="datazone-ListNotebooks-response-items"></a>
The results of the `ListNotebooks` action.
Type: Array of [NotebookSummary](API_NotebookSummary.md) objects

 ** [nextToken](#API_ListNotebooks_ResponseSyntax) **   <a name="datazone-ListNotebooks-response-nextToken"></a>
When the number of notebooks is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of notebooks, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListNotebooks` to list the next set of notebooks.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListNotebooks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListNotebooks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListNotebooks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListNotebooks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListNotebooks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListNotebooks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListNotebooks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListNotebooks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListNotebooks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListNotebooks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListNotebooks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListNotebooks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
