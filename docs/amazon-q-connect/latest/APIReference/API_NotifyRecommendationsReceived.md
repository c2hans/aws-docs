---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_NotifyRecommendationsReceived.html
---

# NotifyRecommendationsReceived
<a name="API_amazon-q-connect_NotifyRecommendationsReceived"></a>

Removes the specified recommendations from the specified assistant's queue of newly available recommendations. You can use this API in conjunction with [GetRecommendations](https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_GetRecommendations.html) and a `waitTimeSeconds` input for long-polling behavior and avoiding duplicate recommendations.

## Request Syntax
<a name="API_amazon-q-connect_NotifyRecommendationsReceived_RequestSyntax"></a>

```
POST /assistants/{{assistantId}}/sessions/{{sessionId}}/recommendations/notify HTTP/1.1
Content-type: application/json

{
   "recommendationIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_NotifyRecommendationsReceived_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assistantId](#API_amazon-q-connect_NotifyRecommendationsReceived_RequestSyntax) **   <a name="connect-amazon-q-connect_NotifyRecommendationsReceived-request-uri-assistantId"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [sessionId](#API_amazon-q-connect_NotifyRecommendationsReceived_RequestSyntax) **   <a name="connect-amazon-q-connect_NotifyRecommendationsReceived-request-uri-sessionId"></a>
The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_NotifyRecommendationsReceived_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [recommendationIds](#API_amazon-q-connect_NotifyRecommendationsReceived_RequestSyntax) **   <a name="connect-amazon-q-connect_NotifyRecommendationsReceived-request-recommendationIds"></a>
The identifiers of the recommendations.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_amazon-q-connect_NotifyRecommendationsReceived_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "message": "string",
         "recommendationId": "string"
      }
   ],
   "recommendationIds": [ "string" ]
}
```

## Response Elements
<a name="API_amazon-q-connect_NotifyRecommendationsReceived_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_amazon-q-connect_NotifyRecommendationsReceived_ResponseSyntax) **   <a name="connect-amazon-q-connect_NotifyRecommendationsReceived-response-errors"></a>
The identifiers of recommendations that are causing errors.
Type: Array of [NotifyRecommendationsReceivedError](API_amazon-q-connect_NotifyRecommendationsReceivedError.md) objects

 ** [recommendationIds](#API_amazon-q-connect_NotifyRecommendationsReceived_ResponseSyntax) **   <a name="connect-amazon-q-connect_NotifyRecommendationsReceived-response-recommendationIds"></a>
The identifiers of the recommendations.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_amazon-q-connect_NotifyRecommendationsReceived_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_NotifyRecommendationsReceived_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/NotifyRecommendationsReceived)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/NotifyRecommendationsReceived)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/NotifyRecommendationsReceived)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/NotifyRecommendationsReceived)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/NotifyRecommendationsReceived)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/NotifyRecommendationsReceived)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/NotifyRecommendationsReceived)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/NotifyRecommendationsReceived)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/NotifyRecommendationsReceived)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/NotifyRecommendationsReceived)
