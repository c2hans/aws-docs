---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PlacementStatistics.html
---

# PlacementStatistics
<a name="API_PlacementStatistics"></a>

An object that contains inbox placement data for an email provider.

## Contents
<a name="API_PlacementStatistics_Contents"></a>

 ** DkimPercentage **   <a name="SES-Type-PlacementStatistics-DkimPercentage"></a>
The percentage of emails that were authenticated by using DomainKeys Identified Mail (DKIM) during the predictive inbox placement test.
Type: Double
Required: No

 ** InboxPercentage **   <a name="SES-Type-PlacementStatistics-InboxPercentage"></a>
The percentage of emails that arrived in recipients' inboxes during the predictive inbox placement test.
Type: Double
Required: No

 ** MissingPercentage **   <a name="SES-Type-PlacementStatistics-MissingPercentage"></a>
The percentage of emails that didn't arrive in recipients' inboxes at all during the predictive inbox placement test.
Type: Double
Required: No

 ** SpamPercentage **   <a name="SES-Type-PlacementStatistics-SpamPercentage"></a>
The percentage of emails that arrived in recipients' spam or junk mail folders during the predictive inbox placement test.
Type: Double
Required: No

 ** SpfPercentage **   <a name="SES-Type-PlacementStatistics-SpfPercentage"></a>
The percentage of emails that were authenticated by using Sender Policy Framework (SPF) during the predictive inbox placement test.
Type: Double
Required: No

## See Also
<a name="API_PlacementStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/PlacementStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/PlacementStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/PlacementStatistics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
