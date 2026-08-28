---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DomainIspPlacement.html
---

# DomainIspPlacement
<a name="API_DomainIspPlacement"></a>

An object that contains inbox placement data for email sent from one of your email domains to a specific email provider.

## Contents
<a name="API_DomainIspPlacement_Contents"></a>

 ** InboxPercentage **   <a name="SES-Type-DomainIspPlacement-InboxPercentage"></a>
The percentage of messages that were sent from the selected domain to the specified email provider that arrived in recipients' inboxes.
Type: Double
Required: No

 ** InboxRawCount **   <a name="SES-Type-DomainIspPlacement-InboxRawCount"></a>
The total number of messages that were sent from the selected domain to the specified email provider that arrived in recipients' inboxes.
Type: Long
Required: No

 ** IspName **   <a name="SES-Type-DomainIspPlacement-IspName"></a>
The name of the email provider that the inbox placement data applies to.
Type: String
Required: No

 ** SpamPercentage **   <a name="SES-Type-DomainIspPlacement-SpamPercentage"></a>
The percentage of messages that were sent from the selected domain to the specified email provider that arrived in recipients' spam or junk mail folders.
Type: Double
Required: No

 ** SpamRawCount **   <a name="SES-Type-DomainIspPlacement-SpamRawCount"></a>
The total number of messages that were sent from the selected domain to the specified email provider that arrived in recipients' spam or junk mail folders.
Type: Long
Required: No

## See Also
<a name="API_DomainIspPlacement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/DomainIspPlacement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/DomainIspPlacement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/DomainIspPlacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
