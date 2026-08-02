---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_ListMessages.html
---

# ListMessages
<a name="API_amazon-q-connect_ListMessages"></a>

Lists messages on an Amazon Q in Connect session.

## Request Syntax
<a name="API_amazon-q-connect_ListMessages_RequestSyntax"></a>

```
GET /assistants/{{assistantId}}/sessions/{{sessionId}}/messages?filter={{filter}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_amazon-q-connect_ListMessages_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assistantId](#API_amazon-q-connect_ListMessages_RequestSyntax) **   <a name="connect-amazon-q-connect_ListMessages-request-uri-assistantId"></a>
The identifier of the Amazon Q in Connect assistant.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [filter](#API_amazon-q-connect_ListMessages_RequestSyntax) **   <a name="connect-amazon-q-connect_ListMessages-request-uri-filter"></a>
The filter criteria for listing messages.
Valid Values: `ALL | TEXT_ONLY`

 ** [maxResults](#API_amazon-q-connect_ListMessages_RequestSyntax) **   <a name="connect-amazon-q-connect_ListMessages-request-uri-maxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_amazon-q-connect_ListMessages_RequestSyntax) **   <a name="connect-amazon-q-connect_ListMessages-request-uri-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [sessionId](#API_amazon-q-connect_ListMessages_RequestSyntax) **   <a name="connect-amazon-q-connect_ListMessages-request-uri-sessionId"></a>
The identifier of the Amazon Q in Connect session.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_ListMessages_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_amazon-q-connect_ListMessages_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "messages": [
      {
         "messageId": "string",
         "participant": "string",
         "timestamp": number,
         "value": { ... }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_amazon-q-connect_ListMessages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [messages](#API_amazon-q-connect_ListMessages_ResponseSyntax) **   <a name="connect-amazon-q-connect_ListMessages-response-messages"></a>
The message information.
Type: Array of [MessageOutput](API_amazon-q-connect_MessageOutput.md) objects

 ** [nextToken](#API_amazon-q-connect_ListMessages_ResponseSyntax) **   <a name="connect-amazon-q-connect_ListMessages-response-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_amazon-q-connect_ListMessages_Errors"></a>

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
<a name="API_amazon-q-connect_ListMessages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/ListMessages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/ListMessages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ListMessages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/ListMessages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ListMessages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/ListMessages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/ListMessages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/ListMessages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/ListMessages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ListMessages)
