---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteVoiceMessageSpendLimitOverride.html
---

# DeleteVoiceMessageSpendLimitOverride
<a name="API_DeleteVoiceMessageSpendLimitOverride"></a>

Deletes an account level monthly spend limit override for sending voice messages. Deleting a spend limit override sets the `EnforcedLimit` equal to the `MaxLimit`, which is controlled by AWS. For more information on spending limits (quotas) see [Quotas ](https://docs.aws.amazon.com/sms-voice/latest/userguide/quotas.html) in the * AWS End User Messaging SMS User Guide*.

## Response Syntax
<a name="API_DeleteVoiceMessageSpendLimitOverride_ResponseSyntax"></a>

```
{
   "MonthlyLimit": number
}
```

## Response Elements
<a name="API_DeleteVoiceMessageSpendLimitOverride_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MonthlyLimit](#API_DeleteVoiceMessageSpendLimitOverride_ResponseSyntax) **   <a name="pinpoint-DeleteVoiceMessageSpendLimitOverride-response-MonthlyLimit"></a>
The current monthly limit, in US dollars.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 1000000000.

## Errors
<a name="API_DeleteVoiceMessageSpendLimitOverride_Errors"></a>

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
<a name="API_DeleteVoiceMessageSpendLimitOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DeleteVoiceMessageSpendLimitOverride)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DeleteVoiceMessageSpendLimitOverride)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DeleteVoiceMessageSpendLimitOverride)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DeleteVoiceMessageSpendLimitOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DeleteVoiceMessageSpendLimitOverride)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DeleteVoiceMessageSpendLimitOverride)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DeleteVoiceMessageSpendLimitOverride)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DeleteVoiceMessageSpendLimitOverride)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DeleteVoiceMessageSpendLimitOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DeleteVoiceMessageSpendLimitOverride)
