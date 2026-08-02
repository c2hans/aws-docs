---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_GetIndex.html
---

# GetIndex
<a name="API_GetIndex"></a>

Retrieves information about an index in an OpenSearch Serverless collection, including its schema definition. The index might be configured to conduct automatic semantic enrichment ingestion and search. For more information, see [About automatic semantic enrichment](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html#serverless-semantic-enrichment).

## Request Syntax
<a name="API_GetIndex_RequestSyntax"></a>

```
{
   "id": "{{string}}",
   "indexName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetIndex_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [id](#API_GetIndex_RequestSyntax) **   <a name="opensearchserverless-GetIndex-request-id"></a>
The unique identifier of the collection containing the index.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: Yes

 ** [indexName](#API_GetIndex_RequestSyntax) **   <a name="opensearchserverless-GetIndex-request-indexName"></a>
The name of the index to retrieve information about.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetIndex_ResponseSyntax"></a>

```
{
   "indexSchema": JSON value
}
```

## Response Elements
<a name="API_GetIndex_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [indexSchema](#API_GetIndex_ResponseSyntax) **   <a name="opensearchserverless-GetIndex-response-indexSchema"></a>
The JSON schema definition for the index, including field mappings and settings.
Type: JSON value

## Errors
<a name="API_GetIndex_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Thrown when accessing or deleting a resource that does not exist.
HTTP Status Code: 400

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_GetIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/GetIndex)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/GetIndex)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/GetIndex)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/GetIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/GetIndex)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/GetIndex)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/GetIndex)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/GetIndex)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/GetIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/GetIndex)
