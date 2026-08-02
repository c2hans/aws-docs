---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_VolumeStatistics.html
---

# VolumeStatistics
<a name="API_VolumeStatistics"></a>

An object that contains information about the amount of email that was delivered to recipients.

## Contents
<a name="API_VolumeStatistics_Contents"></a>

 ** InboxRawCount **   <a name="pinpoint-Type-VolumeStatistics-InboxRawCount"></a>
The total number of emails that arrived in recipients' inboxes.
Type: Long
Required: No

 ** ProjectedInbox **   <a name="pinpoint-Type-VolumeStatistics-ProjectedInbox"></a>
An estimate of the percentage of emails sent from the current domain that will arrive in recipients' inboxes.
Type: Long
Required: No

 ** ProjectedSpam **   <a name="pinpoint-Type-VolumeStatistics-ProjectedSpam"></a>
An estimate of the percentage of emails sent from the current domain that will arrive in recipients' spam or junk mail folders.
Type: Long
Required: No

 ** SpamRawCount **   <a name="pinpoint-Type-VolumeStatistics-SpamRawCount"></a>
The total number of emails that arrived in recipients' spam or junk mail folders.
Type: Long
Required: No

## See Also
<a name="API_VolumeStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/VolumeStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/VolumeStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/VolumeStatistics)
