---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateIndex.html
---

# UpdateIndex
<a name="API_UpdateIndex"></a>

Updates an existing index in an OpenSearch Serverless collection. This operation allows you to modify the index schema, including adding new fields or changing field mappings. You can also enable automatic semantic enrichment ingestion and search. For more information, see [About automatic semantic enrichment](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html#serverless-semantic-enrichment).

## Request Syntax
<a name="API_UpdateIndex_RequestSyntax"></a>

```
{
   "id": "{{string}}",
   "indexName": "{{string}}",
   "indexSchema": {{JSON value}}
}
```

## Request Parameters
<a name="API_UpdateIndex_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [id](#API_UpdateIndex_RequestSyntax) **   <a name="opensearchserverless-UpdateIndex-request-id"></a>
The unique identifier of the collection containing the index to update.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: Yes

 ** [indexName](#API_UpdateIndex_RequestSyntax) **   <a name="opensearchserverless-UpdateIndex-request-indexName"></a>
The name of the index to update.
Type: String
Required: Yes

 ** [indexSchema](#API_UpdateIndex_RequestSyntax) **   <a name="opensearchserverless-UpdateIndex-request-indexSchema"></a>
The updated JSON schema definition for the index, including field mappings and settings.
Type: JSON value
Required: No

## Response Elements
<a name="API_UpdateIndex_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateIndex_Errors"></a>

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
<a name="API_UpdateIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/UpdateIndex)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/UpdateIndex)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/UpdateIndex)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/UpdateIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/UpdateIndex)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/UpdateIndex)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/UpdateIndex)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/UpdateIndex)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/UpdateIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/UpdateIndex)
