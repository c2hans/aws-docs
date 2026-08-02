---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateUserConfig.html
---

# UpdateUserConfig
<a name="API_UpdateUserConfig"></a>

Updates the configuration settings for the specified user, including per-channel auto-accept and after contact work (ACW) timeout settings.

**Note**
This operation replaces the UpdateUserPhoneConfig API. While UpdateUserPhoneConfig applies the same ACW timeout to all channels, UpdateUserConfig allows you to set different auto-accept and ACW timeout values for each channel type.

## Request Syntax
<a name="API_UpdateUserConfig_RequestSyntax"></a>

```
POST /users/{{InstanceId}}/{{UserId}}/config HTTP/1.1
Content-type: application/json

{
   "AfterContactWorkConfigs": [
      {
         "AfterContactWorkConfig": {
            "AfterContactWorkTimeLimit": {{number}}
         },
         "AgentFirstCallbackAfterContactWorkConfig": {
            "AfterContactWorkTimeLimit": {{number}}
         },
         "Channel": "{{string}}"
      }
   ],
   "AutoAcceptConfigs": [
      {
         "AgentFirstCallbackAutoAccept": {{boolean}},
         "AutoAccept": {{boolean}},
         "Channel": "{{string}}"
      }
   ],
   "PersistentConnectionConfigs": [
      {
         "Channel": "{{string}}",
         "PersistentConnection": {{boolean}}
      }
   ],
   "PhoneNumberConfigs": [
      {
         "Channel": "{{string}}",
         "PhoneNumber": "{{string}}",
         "PhoneType": "{{string}}"
      }
   ],
   "VoiceEnhancementConfigs": [
      {
         "Channel": "{{string}}",
         "VoiceEnhancementMode": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateUserConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_UpdateUserConfig_RequestSyntax) **   <a name="connect-UpdateUserConfig-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [UserId](#API_UpdateUserConfig_RequestSyntax) **   <a name="connect-UpdateUserConfig-request-uri-UserId"></a>
The identifier of the user account.
Required: Yes

## Request Body
<a name="API_UpdateUserConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AfterContactWorkConfigs](#API_UpdateUserConfig_RequestSyntax) **   <a name="connect-UpdateUserConfig-request-AfterContactWorkConfigs"></a>
The list of after contact work (ACW) timeout configuration settings for each channel. ACW timeout specifies how many seconds agents have for after contact work, such as entering notes about the contact. The minimum setting is 1 second, and the maximum is 2,000,000 seconds (24 days). Enter 0 for an indefinite amount of time, meaning agents must manually choose to end ACW.
Type: Array of [AfterContactWorkConfigPerChannel](API_AfterContactWorkConfigPerChannel.md) objects
Required: No

 ** [AutoAcceptConfigs](#API_UpdateUserConfig_RequestSyntax) **   <a name="connect-UpdateUserConfig-request-AutoAcceptConfigs"></a>
The list of auto-accept configuration settings for each channel. When auto-accept is enabled for a channel, available agents are automatically connected to contacts from that channel without needing to manually accept. Auto-accept connects agents to contacts in less than one second.
Type: Array of [AutoAcceptConfig](API_AutoAcceptConfig.md) objects
Required: No

 ** [PersistentConnectionConfigs](#API_UpdateUserConfig_RequestSyntax) **   <a name="connect-UpdateUserConfig-request-PersistentConnectionConfigs"></a>
The list of persistent connection configuration settings for each channel.
Type: Array of [PersistentConnectionConfig](API_PersistentConnectionConfig.md) objects
Required: No

 ** [PhoneNumberConfigs](#API_UpdateUserConfig_RequestSyntax) **   <a name="connect-UpdateUserConfig-request-PhoneNumberConfigs"></a>
The list of phone number configuration settings for each channel.
Type: Array of [PhoneNumberConfig](API_PhoneNumberConfig.md) objects
Required: No

 ** [VoiceEnhancementConfigs](#API_UpdateUserConfig_RequestSyntax) **   <a name="connect-UpdateUserConfig-request-VoiceEnhancementConfigs"></a>
The list of voice enhancement configuration settings for each channel.
Type: Array of [VoiceEnhancementConfig](API_VoiceEnhancementConfig.md) objects
Required: No

## Response Syntax
<a name="API_UpdateUserConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateUserConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateUserConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConditionalOperationFailedException **
Request processing failed because dependent condition failed.
HTTP Status Code: 409

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

## Examples
<a name="API_UpdateUserConfig_Examples"></a>

### Request syntax
<a name="API_UpdateUserConfig_Example_1"></a>

This example illustrates one usage of UpdateUserConfig.

```
POST /users/{InstanceId}/{UserId}/config HTTP/1.1
Content-type: application/json

{
   "AfterContactWorkConfigs": [
      {
         "AfterContactWorkConfig": {
            "AfterContactWorkTimeLimit": number
         },
         "Channel": "CHAT"
      },
      {
         "AfterContactWorkConfig": {
            "AfterContactWorkTimeLimit": number
         },
         "Channel": "EMAIL"
      },
      {
         "AfterContactWorkConfig": {
            "AfterContactWorkTimeLimit": number
         },
         "Channel": "TASK"
      },
      {
         "AfterContactWorkConfig": {
            "AfterContactWorkTimeLimit": number
         },
         "AgentFirstCallbackAfterContactWorkConfig": {
            "AfterContactWorkTimeLimit": number
         },
         "Channel": "VOICE"
      }
   ],
   "AutoAcceptConfigs": [
      {
         "AutoAccept": boolean,
         "Channel": "CHAT"
      },
      {
         "AutoAccept": boolean,
         "Channel": "EMAIL"
      },
      {
         "AutoAccept": boolean,
         "Channel": "TASK"
      },
      {
         "AgentFirstCallbackAutoAccept": boolean,
         "AutoAccept": boolean,
         "Channel": "VOICE"
      }
   ],
   "PhoneNumberConfigs": [
      {
         "Channel": "VOICE",
         "PhoneNumber": "string",
         "PhoneType": "string"
      }
   ],
   "PersistentConnectionConfigs": [
      {
         "Channel": "VOICE",
         "PersistentConnection": boolean
      }
   ],
   "VoiceEnhancementConfigs": [
      {
         "Channel": "VOICE",
         "VoiceEnhancementMode": "string"
      }
   ]
}
```

## See Also
<a name="API_UpdateUserConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateUserConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateUserConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateUserConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateUserConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateUserConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateUserConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateUserConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateUserConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateUserConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateUserConfig)
