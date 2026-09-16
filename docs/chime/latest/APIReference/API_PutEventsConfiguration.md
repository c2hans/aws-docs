---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_PutEventsConfiguration.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# PutEventsConfiguration
<a name="API_PutEventsConfiguration"></a>

Creates an events configuration that allows a bot to receive outgoing events sent by Amazon Chime. Choose either an HTTPS endpoint or a Lambda function ARN. For more information, see [Bot](API_Bot.md).

## Request Syntax
<a name="API_PutEventsConfiguration_RequestSyntax"></a>

```
PUT /accounts/{{accountId}}/bots/{{botId}}/events-configuration HTTP/1.1
Content-type: application/json

{
   "LambdaFunctionArn": "{{string}}",
   "OutboundEventsHTTPSEndpoint": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutEventsConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_PutEventsConfiguration_RequestSyntax) **   <a name="chime-PutEventsConfiguration-request-uri-AccountId"></a>
The Amazon Chime account ID.
Pattern: `.*\S.*`
Required: Yes

 ** [botId](#API_PutEventsConfiguration_RequestSyntax) **   <a name="chime-PutEventsConfiguration-request-uri-BotId"></a>
The bot ID.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_PutEventsConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [LambdaFunctionArn](#API_PutEventsConfiguration_RequestSyntax) **   <a name="chime-PutEventsConfiguration-request-LambdaFunctionArn"></a>
Lambda function ARN that allows the bot to receive outgoing events.
Type: String
Required: No

 ** [OutboundEventsHTTPSEndpoint](#API_PutEventsConfiguration_RequestSyntax) **   <a name="chime-PutEventsConfiguration-request-OutboundEventsHTTPSEndpoint"></a>
HTTPS endpoint that allows the bot to receive outgoing events.
Type: String
Required: No

## Response Syntax
<a name="API_PutEventsConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "EventsConfiguration": {
      "BotId": "string",
      "LambdaFunctionArn": "string",
      "OutboundEventsHTTPSEndpoint": "string"
   }
}
```

## Response Elements
<a name="API_PutEventsConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [EventsConfiguration](#API_PutEventsConfiguration_ResponseSyntax) **   <a name="chime-PutEventsConfiguration-response-EventsConfiguration"></a>
The configuration that allows a bot to receive outgoing events. Can be an HTTPS endpoint or an AWS Lambda function ARN.
Type: [EventsConfiguration](API_EventsConfiguration.md) object

## Errors
<a name="API_PutEventsConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

 ** ResourceLimitExceededException **
The request exceeds the resource limit.
HTTP Status Code: 400

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** UnauthorizedClientException **
The client is not currently authorized to make the request.
HTTP Status Code: 401

## See Also
<a name="API_PutEventsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/PutEventsConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/PutEventsConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/PutEventsConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/PutEventsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/PutEventsConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/PutEventsConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/PutEventsConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/PutEventsConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/PutEventsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/PutEventsConfiguration)
