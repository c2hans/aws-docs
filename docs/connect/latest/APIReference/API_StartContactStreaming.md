---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_StartContactStreaming.html
---

# StartContactStreaming
<a name="API_StartContactStreaming"></a>

 Initiates real-time message streaming for a new chat contact.

 For more information about message streaming, see [Enable real-time chat message streaming](https://docs.aws.amazon.com/connect/latest/adminguide/chat-message-streaming.html) in the *Connect Customer Administrator Guide*.

For more information about chat, see the following topics in the *Connect Customer Administrator Guide*:
+  [Concepts: Web and mobile messaging capabilities in Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/web-and-mobile-chat.html)
+  [Connect Customer Chat security best practices](https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat)

## Request Syntax
<a name="API_StartContactStreaming_RequestSyntax"></a>

```
POST /contact/start-streaming HTTP/1.1
Content-type: application/json

{
   "ChatStreamingConfiguration": {
      "StreamingEndpointArn": "{{string}}"
   },
   "ClientToken": "{{string}}",
   "ContactId": "{{string}}",
   "InstanceId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartContactStreaming_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartContactStreaming_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ChatStreamingConfiguration](#API_StartContactStreaming_RequestSyntax) **   <a name="connect-StartContactStreaming-request-ChatStreamingConfiguration"></a>
The streaming configuration, such as the Amazon SNS streaming endpoint.
Type: [ChatStreamingConfiguration](API_ChatStreamingConfiguration.md) object
Required: Yes

 ** [ClientToken](#API_StartContactStreaming_RequestSyntax) **   <a name="connect-StartContactStreaming-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: Yes

 ** [ContactId](#API_StartContactStreaming_RequestSyntax) **   <a name="connect-StartContactStreaming-request-ContactId"></a>
The identifier of the contact. This is the identifier of the contact associated with the first interaction with the contact center.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_StartContactStreaming_RequestSyntax) **   <a name="connect-StartContactStreaming-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_StartContactStreaming_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "StreamingId": "string"
}
```

## Response Elements
<a name="API_StartContactStreaming_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StreamingId](#API_StartContactStreaming_ResponseSyntax) **   <a name="connect-StartContactStreaming-response-StreamingId"></a>
The identifier of the streaming configuration enabled.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

## Errors
<a name="API_StartContactStreaming_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** LimitExceededException **
The allowed limit for the resource has been exceeded.
 ** Message **
The message about the limit.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

## See Also
<a name="API_StartContactStreaming_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/StartContactStreaming)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/StartContactStreaming)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/StartContactStreaming)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/StartContactStreaming)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/StartContactStreaming)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/StartContactStreaming)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/StartContactStreaming)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/StartContactStreaming)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/StartContactStreaming)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/StartContactStreaming)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
