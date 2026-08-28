---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_OverallVolume.html
---

# OverallVolume
<a name="API_OverallVolume"></a>

An object that contains information about email that was sent from the selected domain.

## Contents
<a name="API_OverallVolume_Contents"></a>

 ** DomainIspPlacements **   <a name="pinpoint-Type-OverallVolume-DomainIspPlacements"></a>
An object that contains inbox and junk mail placement metrics for individual email providers.
Type: Array of [DomainIspPlacement](API_DomainIspPlacement.md) objects
Required: No

 ** ReadRatePercent **   <a name="pinpoint-Type-OverallVolume-ReadRatePercent"></a>
The percentage of emails that were sent from the domain that were read by their recipients.
Type: Double
Required: No

 ** VolumeStatistics **   <a name="pinpoint-Type-OverallVolume-VolumeStatistics"></a>
An object that contains information about the numbers of messages that arrived in recipients' inboxes and junk mail folders.
Type: [VolumeStatistics](API_VolumeStatistics.md) object
Required: No

## See Also
<a name="API_OverallVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/OverallVolume)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/OverallVolume)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/OverallVolume)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint Email. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-email` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
