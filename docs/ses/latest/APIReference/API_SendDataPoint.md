---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_SendDataPoint.html
---

# SendDataPoint
<a name="API_SendDataPoint"></a>

Represents sending statistics data. Each `SendDataPoint` contains statistics for a 15-minute period of sending activity.

## Contents
<a name="API_SendDataPoint_Contents"></a>

 ** Bounces **
Number of emails that have bounced.
Type: Long
Required: No

 ** Complaints **
Number of unwanted emails that were rejected by recipients.
Type: Long
Required: No

 ** DeliveryAttempts **
Number of emails that have been sent.
Type: Long
Required: No

 ** Rejects **
Number of emails rejected by Amazon SES.
Type: Long
Required: No

 ** Timestamp **
Time of the data point.
Type: Timestamp
Required: No

## See Also
<a name="API_SendDataPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/SendDataPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/SendDataPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/SendDataPoint)
