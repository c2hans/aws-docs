---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListApplications.html
---

# ListApplications
<a name="API_ListApplications"></a>

Lists all OpenSearch applications under your account.

## Request Syntax
<a name="API_ListApplications_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/list-applications?maxResults={{maxResults}}&nextToken={{nextToken}}&statuses={{statuses}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListApplications_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListApplications_RequestSyntax) **   <a name="opensearchservice-ListApplications-request-uri-maxResults"></a>
An optional parameter that specifies the maximum number of results to return for a given request.
Valid Range: Maximum value of 100.

 ** [nextToken](#API_ListApplications_RequestSyntax) **   <a name="opensearchservice-ListApplications-request-uri-nextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.

 ** [statuses](#API_ListApplications_RequestSyntax) **   <a name="opensearchservice-ListApplications-request-uri-statuses"></a>
Filters the list of OpenSearch applications by status. Possible values: `CREATING`, `UPDATING`, `DELETING`, `FAILED`, `ACTIVE`, and `DELETED`.
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | FAILED`

## Request Body
<a name="API_ListApplications_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListApplications_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApplicationSummaries": [
      {
         "arn": "string",
         "createdAt": number,
         "endpoint": "string",
         "id": "string",
         "lastUpdatedAt": number,
         "name": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListApplications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationSummaries](#API_ListApplications_ResponseSyntax) **   <a name="opensearchservice-ListApplications-response-ApplicationSummaries"></a>
Summarizes OpenSearch applications, including ID, ARN, name, endpoint, status, creation time, and last update time.
Type: Array of [ApplicationSummary](API_ApplicationSummary.md) objects

 ** [nextToken](#API_ListApplications_ResponseSyntax) **   <a name="opensearchservice-ListApplications-response-nextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.
Type: String

## Errors
<a name="API_ListApplications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An error occurred because you don't have permissions to access the resource.
HTTP Status Code: 403

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

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
<a name="API_ListApplications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/ListApplications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/ListApplications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ListApplications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/ListApplications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ListApplications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/ListApplications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/ListApplications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/ListApplications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/ListApplications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ListApplications)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
