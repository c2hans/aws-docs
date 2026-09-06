---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_AssociateChannelFlow.html
---

# AssociateChannelFlow
<a name="API_messaging-chime_AssociateChannelFlow"></a>

Associates a channel flow with a channel. Once associated, all messages to that channel go through channel flow processors. To stop processing, use the `DisassociateChannelFlow` API.

**Note**
Only administrators or channel moderators can associate a channel flow. The `x-amz-chime-bearer` request header is mandatory. Use the ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call as the value in the header.

## Request Syntax
<a name="API_messaging-chime_AssociateChannelFlow_RequestSyntax"></a>

```
PUT /channels/{{channelArn}}/channel-flow HTTP/1.1
x-amz-chime-bearer: {{ChimeBearer}}
Content-type: application/json

{
   "ChannelFlowArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_messaging-chime_AssociateChannelFlow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [channelArn](#API_messaging-chime_AssociateChannelFlow_RequestSyntax) **   <a name="chimesdk-messaging-chime_AssociateChannelFlow-request-uri-ChannelArn"></a>
The ARN of the channel.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [ChimeBearer](#API_messaging-chime_AssociateChannelFlow_RequestSyntax) **   <a name="chimesdk-messaging-chime_AssociateChannelFlow-request-ChimeBearer"></a>
The `AppInstanceUserArn` of the user making the API call.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## Request Body
<a name="API_messaging-chime_AssociateChannelFlow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ChannelFlowArn](#API_messaging-chime_AssociateChannelFlow_RequestSyntax) **   <a name="chimesdk-messaging-chime_AssociateChannelFlow-request-ChannelFlowArn"></a>
The ARN of the channel flow.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## Response Syntax
<a name="API_messaging-chime_AssociateChannelFlow_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_messaging-chime_AssociateChannelFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_messaging-chime_AssociateChannelFlow_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
HTTP Status Code: 409

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The client exceeded its request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client is not currently authorized to make the request.
HTTP Status Code: 401

## See Also
<a name="API_messaging-chime_AssociateChannelFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-messaging-2021-05-15/AssociateChannelFlow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-messaging-2021-05-15/AssociateChannelFlow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/AssociateChannelFlow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-messaging-2021-05-15/AssociateChannelFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/AssociateChannelFlow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-messaging-2021-05-15/AssociateChannelFlow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-messaging-2021-05-15/AssociateChannelFlow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-messaging-2021-05-15/AssociateChannelFlow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-messaging-2021-05-15/AssociateChannelFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/AssociateChannelFlow)
