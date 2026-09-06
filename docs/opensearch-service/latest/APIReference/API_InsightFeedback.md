---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_InsightFeedback.html
---

# InsightFeedback
<a name="API_InsightFeedback"></a>

Submits feedback for an existing insight in an Amazon OpenSearch Service domain. Allows users to provide a thumbs up or thumbs down rating and optional text feedback for a specific insight.

## Request Syntax
<a name="API_InsightFeedback_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/insight-feedback HTTP/1.1
Content-type: application/json

{
   "Entity": {
      "Type": "{{string}}",
      "Value": "{{string}}"
   },
   "FeedbackText": "{{string}}",
   "InsightId": "{{string}}",
   "Thumbs": "{{string}}"
}
```

## URI Request Parameters
<a name="API_InsightFeedback_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_InsightFeedback_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Entity](#API_InsightFeedback_RequestSyntax) **   <a name="opensearchservice-InsightFeedback-request-Entity"></a>
The entity for which to submit insight feedback. Specifies the type and value of the entity, such as a domain name.
Type: [InsightFeedbackEntity](API_InsightFeedbackEntity.md) object
Required: Yes

 ** [FeedbackText](#API_InsightFeedback_RequestSyntax) **   <a name="opensearchservice-InsightFeedback-request-FeedbackText"></a>
Optional text feedback providing additional details about the insight. Maximum length is 1000 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** [InsightId](#API_InsightFeedback_RequestSyntax) **   <a name="opensearchservice-InsightFeedback-request-InsightId"></a>
The unique identifier of the insight for which to submit feedback.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `\p{XDigit}{8}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{12}`
Required: Yes

 ** [Thumbs](#API_InsightFeedback_RequestSyntax) **   <a name="opensearchservice-InsightFeedback-request-Thumbs"></a>
The thumbs up or thumbs down feedback for the insight. Possible values are `Up` and `Down`.
Type: String
Valid Values: `Up | Down`
Required: Yes

## Response Syntax
<a name="API_InsightFeedback_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Status": "string"
}
```

## Response Elements
<a name="API_InsightFeedback_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Status](#API_InsightFeedback_ResponseSyntax) **   <a name="opensearchservice-InsightFeedback-response-Status"></a>
The status of the feedback submission. Possible values are `SUCCESS` and `ERROR`.
Type: String
Valid Values: `SUCCESS | ERROR`

## Errors
<a name="API_InsightFeedback_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** LimitExceededException **
An exception for trying to create more than the allowed number of resources or sub-resources.
HTTP Status Code: 409

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_InsightFeedback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/InsightFeedback)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/InsightFeedback)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/InsightFeedback)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/InsightFeedback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/InsightFeedback)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/InsightFeedback)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/InsightFeedback)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/InsightFeedback)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/InsightFeedback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/InsightFeedback)
