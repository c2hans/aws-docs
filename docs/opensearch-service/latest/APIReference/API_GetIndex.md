---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetIndex.html
---

# GetIndex
<a name="API_GetIndex"></a>

Retrieves information about an OpenSearch index including its schema and semantic enrichment configuration. Use this operation to view the current index structure and semantic search settings.

## Request Syntax
<a name="API_GetIndex_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/domain/{{DomainName}}/index/{{IndexName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetIndex_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_GetIndex_RequestSyntax) **   <a name="opensearchservice-GetIndex-request-uri-DomainName"></a>
The name of an OpenSearch Service domain. Domain names are unique across the domains owned by an account within an AWS Region.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

 ** [IndexName](#API_GetIndex_RequestSyntax) **   <a name="opensearchservice-GetIndex-request-uri-IndexName"></a>
The name of the index to retrieve information about.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(?!\.\.?$)[^_ ,:"+/*\\|?#><A-Z-][^ ,:"+/*\\|?#><A-Z]*$`
Required: Yes

## Request Body
<a name="API_GetIndex_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetIndex_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "IndexSchema": JSON value
}
```

## Response Elements
<a name="API_GetIndex_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IndexSchema](#API_GetIndex_ResponseSyntax) **   <a name="opensearchservice-GetIndex-response-IndexSchema"></a>
The JSON schema of the index including mappings, settings, and semantic enrichment configuration.
Type: JSON value

## Errors
<a name="API_GetIndex_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An error occurred because you don't have permissions to access the resource.
HTTP Status Code: 403

 ** DependencyFailureException **
An exception for when a failure in one of the dependencies results in the service being unable to fetch details about the resource.
HTTP Status Code: 424

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ThrottlingException **
The request was denied due to request throttling. Reduce the frequency of your requests and try again.
HTTP Status Code: 429

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_GetIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/GetIndex)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/GetIndex)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/GetIndex)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/GetIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/GetIndex)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/GetIndex)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/GetIndex)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/GetIndex)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/GetIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/GetIndex)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
