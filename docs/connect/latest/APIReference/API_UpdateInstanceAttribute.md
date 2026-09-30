---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateInstanceAttribute.html
---

# UpdateInstanceAttribute
<a name="API_UpdateInstanceAttribute"></a>

This API is in preview release for Connect Customer and is subject to change.

Updates the value for the specified attribute type.

## Request Syntax
<a name="API_UpdateInstanceAttribute_RequestSyntax"></a>

```
POST /instance/{{InstanceId}}/attribute/{{AttributeType}} HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Value": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateInstanceAttribute_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AttributeType](#API_UpdateInstanceAttribute_RequestSyntax) **   <a name="connect-UpdateInstanceAttribute-request-uri-AttributeType"></a>
The type of attribute.
Only allowlisted customers can consume USE\_CUSTOM\_TTS\_VOICES. To access this feature, contact AWS Support for allowlisting.
If you set the attribute type as `MESSAGE_STREAMING`, you need to update the Lex bot alias resource based policy to include the `lex:RecognizeMessageAsync` action for the connect instance ARN resource.
If you set the attribute type `AUTO_MUTE_AGENT_ON_HOLD` to `true`, the system automatically mutes agents while they're on hold and unmutes them when they resume the contact. Agents can't change their mute state while on hold.
Valid Values: `INBOUND_CALLS | OUTBOUND_CALLS | CONTACTFLOW_LOGS | CONTACT_LENS | AUTO_RESOLVE_BEST_VOICES | USE_CUSTOM_TTS_VOICES | EARLY_MEDIA | MULTI_PARTY_CONFERENCE | AUTO_MUTE_AGENT_ON_HOLD | HIGH_VOLUME_OUTBOUND | ENHANCED_CONTACT_MONITORING | ENHANCED_CHAT_MONITORING | MULTI_PARTY_CHAT_CONFERENCE | MESSAGE_STREAMING`
Required: Yes

 ** [InstanceId](#API_UpdateInstanceAttribute_RequestSyntax) **   <a name="connect-UpdateInstanceAttribute-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_UpdateInstanceAttribute_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_UpdateInstanceAttribute_RequestSyntax) **   <a name="connect-UpdateInstanceAttribute-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [Value](#API_UpdateInstanceAttribute_RequestSyntax) **   <a name="connect-UpdateInstanceAttribute-request-Value"></a>
The value for the attribute. Maximum character limit is 100.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_UpdateInstanceAttribute_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateInstanceAttribute_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateInstanceAttribute_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateInstanceAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateInstanceAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateInstanceAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateInstanceAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateInstanceAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateInstanceAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateInstanceAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateInstanceAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateInstanceAttribute)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateInstanceAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateInstanceAttribute)
