---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteAccountDefaultProtectConfiguration.html
---

# DeleteAccountDefaultProtectConfiguration
<a name="API_DeleteAccountDefaultProtectConfiguration"></a>

Removes the current account default protect configuration.

## Response Syntax
<a name="API_DeleteAccountDefaultProtectConfiguration_ResponseSyntax"></a>

```
{
   "DefaultProtectConfigurationArn": "string",
   "DefaultProtectConfigurationId": "string"
}
```

## Response Elements
<a name="API_DeleteAccountDefaultProtectConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DefaultProtectConfigurationArn](#API_DeleteAccountDefaultProtectConfiguration_ResponseSyntax) **   <a name="pinpoint-DeleteAccountDefaultProtectConfiguration-response-DefaultProtectConfigurationArn"></a>
The Amazon Resource Name (ARN) of the account default protect configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:\S+`

 ** [DefaultProtectConfigurationId](#API_DeleteAccountDefaultProtectConfiguration_ResponseSyntax) **   <a name="pinpoint-DeleteAccountDefaultProtectConfiguration-response-DefaultProtectConfigurationId"></a>
The unique identifier of the account default protect configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`

## Errors
<a name="API_DeleteAccountDefaultProtectConfiguration_Errors"></a>

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
<a name="API_DeleteAccountDefaultProtectConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DeleteAccountDefaultProtectConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DeleteAccountDefaultProtectConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DeleteAccountDefaultProtectConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DeleteAccountDefaultProtectConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DeleteAccountDefaultProtectConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DeleteAccountDefaultProtectConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DeleteAccountDefaultProtectConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DeleteAccountDefaultProtectConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DeleteAccountDefaultProtectConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DeleteAccountDefaultProtectConfiguration)
