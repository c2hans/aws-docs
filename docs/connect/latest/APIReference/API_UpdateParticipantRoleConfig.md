---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateParticipantRoleConfig.html
---

# UpdateParticipantRoleConfig
<a name="API_UpdateParticipantRoleConfig"></a>

Updates timeouts for when human chat participants are to be considered idle, and when agents are automatically disconnected from a chat due to idleness. You can set four timers:
+ Customer idle timeout
+ Customer auto-disconnect timeout
+ Agent idle timeout
+ Agent auto-disconnect timeout

For more information about how chat timeouts work, see [Set up chat timeouts for human participants](https://docs.aws.amazon.com/connect/latest/adminguide/setup-chat-timeouts.html).

## Request Syntax
<a name="API_UpdateParticipantRoleConfig_RequestSyntax"></a>

```
PUT /contact/participant-role-config/{{InstanceId}}/{{ContactId}} HTTP/1.1
Content-type: application/json

{
   "ChannelConfiguration": { ... }
}
```

## URI Request Parameters
<a name="API_UpdateParticipantRoleConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactId](#API_UpdateParticipantRoleConfig_RequestSyntax) **   <a name="connect-UpdateParticipantRoleConfig-request-uri-ContactId"></a>
The identifier of the contact in this instance of Connect Customer.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_UpdateParticipantRoleConfig_RequestSyntax) **   <a name="connect-UpdateParticipantRoleConfig-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_UpdateParticipantRoleConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ChannelConfiguration](#API_UpdateParticipantRoleConfig_RequestSyntax) **   <a name="connect-UpdateParticipantRoleConfig-request-ChannelConfiguration"></a>
The Connect Customer channel you want to configure.
Type: [UpdateParticipantRoleConfigChannelInfo](API_UpdateParticipantRoleConfigChannelInfo.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_UpdateParticipantRoleConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateParticipantRoleConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateParticipantRoleConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

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
<a name="API_UpdateParticipantRoleConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateParticipantRoleConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateParticipantRoleConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateParticipantRoleConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateParticipantRoleConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateParticipantRoleConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateParticipantRoleConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateParticipantRoleConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateParticipantRoleConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateParticipantRoleConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateParticipantRoleConfig)
