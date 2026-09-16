---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_GetSendQuota.html
---

# GetSendQuota
<a name="API_GetSendQuota"></a>

Provides the sending limits for the Amazon SES account.

You can execute this operation no more than once per second.

## Response Elements
<a name="API_GetSendQuota_ResponseElements"></a>

The following elements are returned by the service.

 ** Max24HourSend **
The maximum number of emails the user is allowed to send in a 24-hour interval. A value of -1 signifies an unlimited quota.
Type: Double

 ** MaxSendRate **
The maximum number of emails that Amazon SES can accept from the user's account per second.
The rate at which Amazon SES accepts the user's messages might be less than the maximum send rate.
Type: Double

 ** SentLast24Hours **
The number of emails sent during the previous 24 hours.
Type: Double

## Errors
<a name="API_GetSendQuota_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetSendQuota_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/GetSendQuota)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/GetSendQuota)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/GetSendQuota)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/GetSendQuota)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/GetSendQuota)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/GetSendQuota)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/GetSendQuota)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/GetSendQuota)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/GetSendQuota)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/GetSendQuota)
