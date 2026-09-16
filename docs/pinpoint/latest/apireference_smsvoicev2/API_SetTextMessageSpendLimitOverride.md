---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_SetTextMessageSpendLimitOverride.html
---

# SetTextMessageSpendLimitOverride
<a name="API_SetTextMessageSpendLimitOverride"></a>

Sets an account level monthly spend limit override for sending text messages. The requested spend limit must be less than or equal to the `MaxLimit`, which is set by AWS.

## Request Syntax
<a name="API_SetTextMessageSpendLimitOverride_RequestSyntax"></a>

```
{
   "MonthlyLimit": {{number}}
}
```

## Request Parameters
<a name="API_SetTextMessageSpendLimitOverride_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MonthlyLimit](#API_SetTextMessageSpendLimitOverride_RequestSyntax) **   <a name="pinpoint-SetTextMessageSpendLimitOverride-request-MonthlyLimit"></a>
The new monthly limit to enforce on text messages.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 1000000000.
Required: Yes

## Response Syntax
<a name="API_SetTextMessageSpendLimitOverride_ResponseSyntax"></a>

```
{
   "MonthlyLimit": number
}
```

## Response Elements
<a name="API_SetTextMessageSpendLimitOverride_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MonthlyLimit](#API_SetTextMessageSpendLimitOverride_ResponseSyntax) **   <a name="pinpoint-SetTextMessageSpendLimitOverride-response-MonthlyLimit"></a>
The current monthly limit to enforce on sending text messages.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 1000000000.

## Errors
<a name="API_SetTextMessageSpendLimitOverride_Errors"></a>

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
<a name="API_SetTextMessageSpendLimitOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/SetTextMessageSpendLimitOverride)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/SetTextMessageSpendLimitOverride)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/SetTextMessageSpendLimitOverride)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/SetTextMessageSpendLimitOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/SetTextMessageSpendLimitOverride)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/SetTextMessageSpendLimitOverride)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/SetTextMessageSpendLimitOverride)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/SetTextMessageSpendLimitOverride)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/SetTextMessageSpendLimitOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/SetTextMessageSpendLimitOverride)
