---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_SendQuota.html
---

# SendQuota
<a name="API_SendQuota"></a>

An object that contains information about the per-day and per-second sending limits for your Amazon Pinpoint account in the current AWS Region.

## Contents
<a name="API_SendQuota_Contents"></a>

 ** Max24HourSend **   <a name="pinpoint-Type-SendQuota-Max24HourSend"></a>
The maximum number of emails that you can send in the current AWS Region over a 24-hour period. This value is also called your *sending quota*.
Type: Double
Required: No

 ** MaxSendRate **   <a name="pinpoint-Type-SendQuota-MaxSendRate"></a>
The maximum number of emails that you can send per second in the current AWS Region. This value is also called your *maximum sending rate* or your *maximum TPS (transactions per second) rate*.
Type: Double
Required: No

 ** SentLast24Hours **   <a name="pinpoint-Type-SendQuota-SentLast24Hours"></a>
The number of emails sent from your Amazon Pinpoint account in the current AWS Region over the past 24 hours.
Type: Double
Required: No

## See Also
<a name="API_SendQuota_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/SendQuota)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/SendQuota)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/SendQuota)
