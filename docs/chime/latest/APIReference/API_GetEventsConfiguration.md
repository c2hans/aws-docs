---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_GetEventsConfiguration.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# GetEventsConfiguration
<a name="API_GetEventsConfiguration"></a>

Gets details for an events configuration that allows a bot to receive outgoing events, such as an HTTPS endpoint or Lambda function ARN.

## Request Syntax
<a name="API_GetEventsConfiguration_RequestSyntax"></a>

```
GET /accounts/{{accountId}}/bots/{{botId}}/events-configuration HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEventsConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_GetEventsConfiguration_RequestSyntax) **   <a name="chime-GetEventsConfiguration-request-uri-AccountId"></a>
The Amazon Chime account ID.
Pattern: `.*\S.*`
Required: Yes

 ** [botId](#API_GetEventsConfiguration_RequestSyntax) **   <a name="chime-GetEventsConfiguration-request-uri-BotId"></a>
The bot ID.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_GetEventsConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEventsConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_GetEventsConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EventsConfiguration](#API_GetEventsConfiguration_ResponseSyntax) **   <a name="chime-GetEventsConfiguration-response-EventsConfiguration"></a>
The events configuration details.
Type: [EventsConfiguration](API_EventsConfiguration.md) object

## Errors
<a name="API_GetEventsConfiguration_Errors"></a>

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
<a name="API_GetEventsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/GetEventsConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/GetEventsConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/GetEventsConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/GetEventsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/GetEventsConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/GetEventsConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/GetEventsConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/GetEventsConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/GetEventsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/GetEventsConfiguration)
