---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_OrganizationStatistics.html
---

# OrganizationStatistics
<a name="API_OrganizationStatistics"></a>

Information about the coverage statistics of the features for the entire AWS organization.

When you create a new AWS organization, it might take up to 24 hours to generate the statistics summary for this organization.

## Contents
<a name="API_OrganizationStatistics_Contents"></a>

 ** activeAccountsCount **   <a name="guardduty-Type-OrganizationStatistics-activeAccountsCount"></a>
Total number of active accounts in your AWS organization that are associated with GuardDuty.
Type: Integer
Required: No

 ** countByFeature **   <a name="guardduty-Type-OrganizationStatistics-countByFeature"></a>
Retrieves the coverage statistics for each feature.
Type: Array of [OrganizationFeatureStatistics](API_OrganizationFeatureStatistics.md) objects
Required: No

 ** enabledAccountsCount **   <a name="guardduty-Type-OrganizationStatistics-enabledAccountsCount"></a>
Total number of accounts that have enabled GuardDuty.
Type: Integer
Required: No

 ** memberAccountsCount **   <a name="guardduty-Type-OrganizationStatistics-memberAccountsCount"></a>
Total number of accounts in your AWS organization that are associated with GuardDuty.
Type: Integer
Required: No

 ** totalAccountsCount **   <a name="guardduty-Type-OrganizationStatistics-totalAccountsCount"></a>
Total number of accounts in your AWS organization.
Type: Integer
Required: No

## See Also
<a name="API_OrganizationStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/OrganizationStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/OrganizationStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/OrganizationStatistics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
