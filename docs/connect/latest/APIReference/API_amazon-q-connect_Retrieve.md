---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_Retrieve.html
---

# Retrieve
<a name="API_amazon-q-connect_Retrieve"></a>

Retrieves content from knowledge sources based on a query.

## Request Syntax
<a name="API_amazon-q-connect_Retrieve_RequestSyntax"></a>

```
POST /assistants/{{assistantId}}/retrieve HTTP/1.1
Content-type: application/json

{
   "retrievalConfiguration": {
      "filter": { ... },
      "knowledgeSource": { ... },
      "numberOfResults": {{number}},
      "overrideKnowledgeBaseSearchType": "{{string}}"
   },
   "retrievalQuery": "{{string}}"
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_Retrieve_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assistantId](#API_amazon-q-connect_Retrieve_RequestSyntax) **   <a name="connect-amazon-q-connect_Retrieve-request-uri-assistantId"></a>
The identifier of the Amazon Q in Connect assistant for content retrieval.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_Retrieve_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [retrievalConfiguration](#API_amazon-q-connect_Retrieve_RequestSyntax) **   <a name="connect-amazon-q-connect_Retrieve-request-retrievalConfiguration"></a>
The configuration for the content retrieval operation.
Type: [RetrievalConfiguration](API_amazon-q-connect_RetrievalConfiguration.md) object
Required: Yes

 ** [retrievalQuery](#API_amazon-q-connect_Retrieve_RequestSyntax) **   <a name="connect-amazon-q-connect_Retrieve-request-retrievalQuery"></a>
The query for content retrieval.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

## Response Syntax
<a name="API_amazon-q-connect_Retrieve_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "results": [
      {
         "associationId": "string",
         "contentText": "string",
         "referenceType": "string",
         "sourceId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_amazon-q-connect_Retrieve_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [results](#API_amazon-q-connect_Retrieve_ResponseSyntax) **   <a name="connect-amazon-q-connect_Retrieve-response-results"></a>
The results of the content retrieval operation.
Type: Array of [RetrieveResult](API_amazon-q-connect_RetrieveResult.md) objects

## Errors
<a name="API_amazon-q-connect_Retrieve_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource. For example, if you're using a `Create` API (such as `CreateAssistant`) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.
HTTP Status Code: 409

 ** DependencyFailedException **
The request failed because it depends on another request that failed.
HTTP Status Code: 424

 ** RequestTimeoutException **
The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the date stamp on the request is more than 15 minutes in the future.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_Retrieve_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/Retrieve)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/Retrieve)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/Retrieve)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/Retrieve)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/Retrieve)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/Retrieve)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/Retrieve)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/Retrieve)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/Retrieve)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/Retrieve)
