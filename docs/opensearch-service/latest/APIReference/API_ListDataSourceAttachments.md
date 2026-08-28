---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListDataSourceAttachments.html
---

# ListDataSourceAttachments
<a name="API_ListDataSourceAttachments"></a>

Returns a paginated list of all data source attachments for an OpenSearch application, including attachments in all states (`PENDING`, `ATTACHED`, and `FAILED`).

## Request Syntax
<a name="API_ListDataSourceAttachments_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/application/{{id}}/listDataSourceAttachments HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListDataSourceAttachments_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_ListDataSourceAttachments_RequestSyntax) **   <a name="opensearchservice-ListDataSourceAttachments-request-uri-id"></a>
The unique identifier or name of the OpenSearch application to list attachments for.
Pattern: `[a-z0-9]{3,30}`
Required: Yes

## Request Body
<a name="API_ListDataSourceAttachments_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListDataSourceAttachments_RequestSyntax) **   <a name="opensearchservice-ListDataSourceAttachments-request-maxResults"></a>
The maximum number of results to return per page. The default is 50.
Type: Integer
Required: No

 ** [nextToken](#API_ListDataSourceAttachments_RequestSyntax) **   <a name="opensearchservice-ListDataSourceAttachments-request-nextToken"></a>
The pagination token from a previous call to retrieve the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListDataSourceAttachments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "attachments": [
      {
         "attachmentId": "string",
         "dataSourceArn": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDataSourceAttachments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [attachments](#API_ListDataSourceAttachments_ResponseSyntax) **   <a name="opensearchservice-ListDataSourceAttachments-response-attachments"></a>
A list of data source attachment summaries for the specified application.
Type: Array of [DataSourceAttachmentSummary](API_DataSourceAttachmentSummary.md) objects

 ** [nextToken](#API_ListDataSourceAttachments_ResponseSyntax) **   <a name="opensearchservice-ListDataSourceAttachments-response-nextToken"></a>
The pagination token to use in a subsequent call to retrieve the next set of results.
Type: String

## Errors
<a name="API_ListDataSourceAttachments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An error occurred because you don't have permissions to access the resource.
HTTP Status Code: 403

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_ListDataSourceAttachments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/ListDataSourceAttachments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/ListDataSourceAttachments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ListDataSourceAttachments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/ListDataSourceAttachments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ListDataSourceAttachments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/ListDataSourceAttachments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/ListDataSourceAttachments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/ListDataSourceAttachments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/ListDataSourceAttachments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ListDataSourceAttachments)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
