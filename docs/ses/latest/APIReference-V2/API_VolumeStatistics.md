---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_VolumeStatistics.html
---

# VolumeStatistics
<a name="API_VolumeStatistics"></a>

An object that contains information about the amount of email that was delivered to recipients.

## Contents
<a name="API_VolumeStatistics_Contents"></a>

 ** InboxRawCount **   <a name="SES-Type-VolumeStatistics-InboxRawCount"></a>
The total number of emails that arrived in recipients' inboxes.
Type: Long
Required: No

 ** ProjectedInbox **   <a name="SES-Type-VolumeStatistics-ProjectedInbox"></a>
An estimate of the percentage of emails sent from the current domain that will arrive in recipients' inboxes.
Type: Long
Required: No

 ** ProjectedSpam **   <a name="SES-Type-VolumeStatistics-ProjectedSpam"></a>
An estimate of the percentage of emails sent from the current domain that will arrive in recipients' spam or junk mail folders.
Type: Long
Required: No

 ** SpamRawCount **   <a name="SES-Type-VolumeStatistics-SpamRawCount"></a>
The total number of emails that arrived in recipients' spam or junk mail folders.
Type: Long
Required: No

## See Also
<a name="API_VolumeStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/VolumeStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/VolumeStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/VolumeStatistics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
