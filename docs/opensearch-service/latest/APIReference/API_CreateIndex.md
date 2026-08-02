---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreateIndex.html
---

# CreateIndex
<a name="API_CreateIndex"></a>

Creates an OpenSearch index with optional automatic semantic enrichment for specified text fields. Automatic semantic enrichment enables semantic search capabilities without requiring machine learning expertise, improving search relevance by up to 20% by understanding search intent and contextual meaning beyond keyword matching. The semantic enrichment process has zero impact on search latency as sparse encodings are stored directly within the index during indexing. For more information, see [Automatic semantic enrichment](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/opensearch-semantic-enrichment.html).

## Request Syntax
<a name="API_CreateIndex_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/domain/{{DomainName}}/index HTTP/1.1
Content-type: application/json

{
   "IndexName": "{{string}}",
   "IndexSchema": {{JSON value}}
}
```

## URI Request Parameters
<a name="API_CreateIndex_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_CreateIndex_RequestSyntax) **   <a name="opensearchservice-CreateIndex-request-uri-DomainName"></a>
The name of an OpenSearch Service domain. Domain names are unique across the domains owned by an account within an AWS Region.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_CreateIndex_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [IndexName](#API_CreateIndex_RequestSyntax) **   <a name="opensearchservice-CreateIndex-request-IndexName"></a>
The name of the index to create. Must be between 1 and 255 characters and follow OpenSearch naming conventions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(?!\.\.?$)[^_ ,:"+/*\\|?#><A-Z-][^ ,:"+/*\\|?#><A-Z]*$`
Required: Yes

 ** [IndexSchema](#API_CreateIndex_RequestSyntax) **   <a name="opensearchservice-CreateIndex-request-IndexSchema"></a>
The JSON schema defining index mappings, settings, and semantic enrichment configuration. The schema specifies which text fields should be automatically enriched for semantic search capabilities and includes OpenSearch index configuration parameters.
Type: JSON value
Required: Yes

## Response Syntax
<a name="API_CreateIndex_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Status": "string"
}
```

## Response Elements
<a name="API_CreateIndex_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Status](#API_CreateIndex_ResponseSyntax) **   <a name="opensearchservice-CreateIndex-response-Status"></a>
The status of the index creation operation.
Type: String
Valid Values: `CREATED | UPDATED | DELETED`

## Errors
<a name="API_CreateIndex_Errors"></a>

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

 ** ResourceAlreadyExistsException **
An exception for creating a resource that already exists.
HTTP Status Code: 409

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
<a name="API_CreateIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/CreateIndex)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/CreateIndex)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/CreateIndex)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/CreateIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/CreateIndex)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/CreateIndex)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/CreateIndex)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/CreateIndex)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/CreateIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/CreateIndex)
