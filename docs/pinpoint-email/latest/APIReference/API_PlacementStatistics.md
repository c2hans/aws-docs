---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PlacementStatistics.html
---

# PlacementStatistics
<a name="API_PlacementStatistics"></a>

An object that contains inbox placement data for an email provider.

## Contents
<a name="API_PlacementStatistics_Contents"></a>

 ** DkimPercentage **   <a name="pinpoint-Type-PlacementStatistics-DkimPercentage"></a>
The percentage of emails that were authenticated by using DomainKeys Identified Mail (DKIM) during the predictive inbox placement test.
Type: Double
Required: No

 ** InboxPercentage **   <a name="pinpoint-Type-PlacementStatistics-InboxPercentage"></a>
The percentage of emails that arrived in recipients' inboxes during the predictive inbox placement test.
Type: Double
Required: No

 ** MissingPercentage **   <a name="pinpoint-Type-PlacementStatistics-MissingPercentage"></a>
The percentage of emails that didn't arrive in recipients' inboxes at all during the predictive inbox placement test.
Type: Double
Required: No

 ** SpamPercentage **   <a name="pinpoint-Type-PlacementStatistics-SpamPercentage"></a>
The percentage of emails that arrived in recipients' spam or junk mail folders during the predictive inbox placement test.
Type: Double
Required: No

 ** SpfPercentage **   <a name="pinpoint-Type-PlacementStatistics-SpfPercentage"></a>
The percentage of emails that were authenticated by using Sender Policy Framework (SPF) during the predictive inbox placement test.
Type: Double
Required: No

## See Also
<a name="API_PlacementStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/PlacementStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/PlacementStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/PlacementStatistics)
