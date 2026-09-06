---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SetDefaultSenderId.html
---

# SetDefaultSenderId
<a name="API_SetDefaultSenderId"></a>

Sets default sender ID on a configuration set.

When sending a text message to a destination country that supports sender IDs, the default sender ID on the configuration set specified will be used if no dedicated origination phone numbers or registered sender IDs are available in your account.

## Request Syntax
<a name="API_SetDefaultSenderId_RequestSyntax"></a>

```
{
   "ConfigurationSetName": "{{string}}",
   "SenderId": "{{string}}"
}
```

## Request Parameters
<a name="API_SetDefaultSenderId_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ConfigurationSetName](#API_SetDefaultSenderId_RequestSyntax) **   <a name="pinpoint-SetDefaultSenderId-request-ConfigurationSetName"></a>
The configuration set to updated with a new default SenderId. This field can be the ConsigurationSetName or ConfigurationSetArn.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

 ** [SenderId](#API_SetDefaultSenderId_RequestSyntax) **   <a name="pinpoint-SetDefaultSenderId-request-SenderId"></a>
The current sender ID for the configuration set. When sending a text message to a destination country which supports SenderIds, the default sender ID on the configuration set specified on [SendTextMessage](API_SendTextMessage.md) will be used if no dedicated origination phone numbers or registered SenderIds are available in your account, instead of a generic sender ID, such as 'NOTICE'.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 11.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

## Response Syntax
<a name="API_SetDefaultSenderId_ResponseSyntax"></a>

```
{
   "ConfigurationSetArn": "string",
   "ConfigurationSetName": "string",
   "SenderId": "string"
}
```

## Response Elements
<a name="API_SetDefaultSenderId_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigurationSetArn](#API_SetDefaultSenderId_ResponseSyntax) **   <a name="pinpoint-SetDefaultSenderId-response-ConfigurationSetArn"></a>
The Amazon Resource Name (ARN) of the updated configuration set.
Type: String

 ** [ConfigurationSetName](#API_SetDefaultSenderId_ResponseSyntax) **   <a name="pinpoint-SetDefaultSenderId-response-ConfigurationSetName"></a>
The name of the configuration set that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

 ** [SenderId](#API_SetDefaultSenderId_ResponseSyntax) **   <a name="pinpoint-SetDefaultSenderId-response-SenderId"></a>
The default sender ID to set for the ConfigurationSet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 11.
Pattern: `[A-Za-z0-9_-]+`

## Errors
<a name="API_SetDefaultSenderId_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because you don't have sufficient permissions to access the resource.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

 ** InternalServerException **
The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.
 ** RequestId **
The unique identifier of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A requested resource couldn't be found.
 ** ResourceId **
The unique identifier of the resource.
 ** ResourceType **
The type of resource that caused the exception.
HTTP Status Code: 400

 ** ThrottlingException **
An error that occurred because too many requests were sent during a certain amount of time.
HTTP Status Code: 400

 ** ValidationException **
A validation exception for a field.
 ** Fields **
The field that failed validation.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_SetDefaultSenderId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/SetDefaultSenderId)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/SetDefaultSenderId)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/SetDefaultSenderId)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/SetDefaultSenderId)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/SetDefaultSenderId)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/SetDefaultSenderId)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/SetDefaultSenderId)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/SetDefaultSenderId)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/SetDefaultSenderId)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/SetDefaultSenderId)
