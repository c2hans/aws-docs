---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteNotifyMessageSpendLimitOverride.html
---

# DeleteNotifyMessageSpendLimitOverride
<a name="API_DeleteNotifyMessageSpendLimitOverride"></a>

Deletes an account-level monthly spending limit override for sending notify messages. Deleting a spend limit override will set the `EnforcedLimit` to equal the `MaxLimit`, which is controlled by AWS. For more information on spend limits (quotas) see [Quotas ](https://docs.aws.amazon.com/sms-voice/latest/userguide/quotas.html) in the * AWS End User Messaging SMS User Guide*.

## Response Syntax
<a name="API_DeleteNotifyMessageSpendLimitOverride_ResponseSyntax"></a>

```
{
   "MonthlyLimit": number
}
```

## Response Elements
<a name="API_DeleteNotifyMessageSpendLimitOverride_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MonthlyLimit](#API_DeleteNotifyMessageSpendLimitOverride_ResponseSyntax) **   <a name="pinpoint-DeleteNotifyMessageSpendLimitOverride-response-MonthlyLimit"></a>
The current monthly limit, in US dollars.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 1000000000.

## Errors
<a name="API_DeleteNotifyMessageSpendLimitOverride_Errors"></a>

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
<a name="API_DeleteNotifyMessageSpendLimitOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DeleteNotifyMessageSpendLimitOverride)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DeleteNotifyMessageSpendLimitOverride)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DeleteNotifyMessageSpendLimitOverride)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DeleteNotifyMessageSpendLimitOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DeleteNotifyMessageSpendLimitOverride)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DeleteNotifyMessageSpendLimitOverride)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DeleteNotifyMessageSpendLimitOverride)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DeleteNotifyMessageSpendLimitOverride)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DeleteNotifyMessageSpendLimitOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DeleteNotifyMessageSpendLimitOverride)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
