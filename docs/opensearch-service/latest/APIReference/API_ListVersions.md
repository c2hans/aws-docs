---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListVersions.html
---

# ListVersions
<a name="API_ListVersions"></a>

Lists all versions of OpenSearch and Elasticsearch that Amazon OpenSearch Service supports.

## Request Syntax
<a name="API_ListVersions_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/versions?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListVersions_RequestSyntax) **   <a name="opensearchservice-ListVersions-request-uri-MaxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to get the next page of results.
Valid Range: Maximum value of 100.

 ** [NextToken](#API_ListVersions_RequestSyntax) **   <a name="opensearchservice-ListVersions-request-uri-NextToken"></a>
If your initial `ListVersions` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `ListVersions` operations, which returns results in the next page.

## Request Body
<a name="API_ListVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Versions": [ "string" ]
}
```

## Response Elements
<a name="API_ListVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListVersions_ResponseSyntax) **   <a name="opensearchservice-ListVersions-response-NextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.
Type: String

 ** [Versions](#API_ListVersions_ResponseSyntax) **   <a name="opensearchservice-ListVersions-response-Versions"></a>
A list of all versions of OpenSearch and Elasticsearch that Amazon OpenSearch Service supports.
Type: Array of strings
Length Constraints: Minimum length of 14. Maximum length of 18.
Pattern: `^Elasticsearch_[0-9]{1}\.[0-9]{1,2}$|^OpenSearch_[0-9]{1,2}\.[0-9]{1,2}$`

## Errors
<a name="API_ListVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## Examples
<a name="API_ListVersions_Examples"></a>

### Example
<a name="API_ListVersions_Example_1"></a>

This example illustrates one usage of ListVersions.

#### Sample Request
<a name="API_ListVersions_Example_1_Request"></a>

```
GET /2021-01-01/opensearch/versions HTTP/1.1
Host: es.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.15.13 Python/3.11.6 Windows/10 exe/AMD64 prompt/off command/opensearch.list-versions
X-Amz-Date: 20240205T211126Z
X-Amz-Security-Token: IQoJb3JpZ2luX2VjEI3wEaCXVz==
Authorization: AWS4-HMAC-SHA256 Credential=ASIAU/20240205/us-east-1/es/aws4_request, SignedHeaders=host;x-amz-date;x-amz-security-token, Signature=10e4bd0052c108fb022e79d4f122329d00a6d376054dadefcd81bb8df728d808
```

#### Sample Response
<a name="API_ListVersions_Example_1_Response"></a>

```
{
   "NextToken":null,
   "Versions":[
      "OpenSearch_2.11",
      "OpenSearch_2.9",
      "OpenSearch_2.7",
      "OpenSearch_2.5",
      "OpenSearch_2.3",
      "OpenSearch_1.3",
      "OpenSearch_1.2",
      "OpenSearch_1.1",
      "OpenSearch_1.0",
      "Elasticsearch_7.10",
      "Elasticsearch_7.9",
      "Elasticsearch_7.8",
      "Elasticsearch_7.7",
      "Elasticsearch_7.4",
      "Elasticsearch_7.1",
      "Elasticsearch_6.8",
      "Elasticsearch_6.7",
      "Elasticsearch_6.5",
      "Elasticsearch_6.4",
      "Elasticsearch_6.3",
      "Elasticsearch_6.2",
      "Elasticsearch_6.0",
      "Elasticsearch_5.6",
      "Elasticsearch_5.5",
      "Elasticsearch_5.3",
      "Elasticsearch_5.1",
      "Elasticsearch_2.3",
      "Elasticsearch_1.5"
   ]
}
```

## See Also
<a name="API_ListVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/ListVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/ListVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ListVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/ListVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ListVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/ListVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/ListVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/ListVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/ListVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ListVersions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
