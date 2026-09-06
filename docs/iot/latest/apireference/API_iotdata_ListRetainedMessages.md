---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_ListRetainedMessages.html
---

# ListRetainedMessages
<a name="API_iotdata_ListRetainedMessages"></a>

Lists summary information about the retained messages stored for the account.

This action returns only the topic names of the retained messages. It doesn't return any message payloads. Although this action doesn't return a message payload, it can still incur messaging costs.

To get the message payload of a retained message, call [GetRetainedMessage](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_GetRetainedMessage.html) with the topic name of the retained message.

Requires permission to access the [ListRetainedMessages](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html) action.

For more information about messaging costs, see [AWS IoT Core pricing - Messaging](http://aws.amazon.com/iot-core/pricing/#Messaging).

## Request Syntax
<a name="API_iotdata_ListRetainedMessages_RequestSyntax"></a>

```
GET /retainedMessage?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_iotdata_ListRetainedMessages_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_iotdata_ListRetainedMessages_RequestSyntax) **   <a name="iot-iotdata_ListRetainedMessages-request-uri-maxResults"></a>
The maximum number of results to return at one time.
Valid Range: Minimum value of 1. Maximum value of 200.

 ** [nextToken](#API_iotdata_ListRetainedMessages_RequestSyntax) **   <a name="iot-iotdata_ListRetainedMessages-request-uri-nextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.

## Request Body
<a name="API_iotdata_ListRetainedMessages_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_iotdata_ListRetainedMessages_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "retainedTopics": [
      {
         "lastModifiedTime": number,
         "payloadSize": number,
         "qos": number,
         "topic": "string"
      }
   ]
}
```

## Response Elements
<a name="API_iotdata_ListRetainedMessages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_iotdata_ListRetainedMessages_ResponseSyntax) **   <a name="iot-iotdata_ListRetainedMessages-response-nextToken"></a>
The token for the next set of results, or null if there are no additional results.
Type: String

 ** [retainedTopics](#API_iotdata_ListRetainedMessages_ResponseSyntax) **   <a name="iot-iotdata_ListRetainedMessages-response-retainedTopics"></a>
A summary list the account's retained messages. The information returned doesn't include the message payloads of the retained messages.
Type: Array of [RetainedMessageSummary](API_iotdata_RetainedMessageSummary.md) objects

## Errors
<a name="API_iotdata_ListRetainedMessages_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** MethodNotAllowedException **
The specified combination of HTTP verb and URI is not supported.
 ** message **
The message for the exception.
HTTP Status Code: 405

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 429

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_iotdata_ListRetainedMessages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-data-2015-05-28/ListRetainedMessages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-data-2015-05-28/ListRetainedMessages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-data-2015-05-28/ListRetainedMessages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-data-2015-05-28/ListRetainedMessages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-data-2015-05-28/ListRetainedMessages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-data-2015-05-28/ListRetainedMessages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-data-2015-05-28/ListRetainedMessages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-data-2015-05-28/ListRetainedMessages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-data-2015-05-28/ListRetainedMessages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-data-2015-05-28/ListRetainedMessages)
