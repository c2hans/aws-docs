---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_OrganizationFeatureStatisticsAdditionalConfiguration.html
---

# OrganizationFeatureStatisticsAdditionalConfiguration
<a name="API_OrganizationFeatureStatisticsAdditionalConfiguration"></a>

Information about the coverage statistic for the additional configuration of the feature.

## Contents
<a name="API_OrganizationFeatureStatisticsAdditionalConfiguration_Contents"></a>

 ** enabledAccountsCount **   <a name="guardduty-Type-OrganizationFeatureStatisticsAdditionalConfiguration-enabledAccountsCount"></a>
Total number of accounts that have enabled the additional configuration.
Type: Integer
Required: No

 ** name **   <a name="guardduty-Type-OrganizationFeatureStatisticsAdditionalConfiguration-name"></a>
Name of the additional configuration within a feature.
Type: String
Valid Values: `EKS_ADDON_MANAGEMENT | ECS_FARGATE_AGENT_MANAGEMENT | EC2_AGENT_MANAGEMENT`
Required: No

## See Also
<a name="API_OrganizationFeatureStatisticsAdditionalConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/OrganizationFeatureStatisticsAdditionalConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/OrganizationFeatureStatisticsAdditionalConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/OrganizationFeatureStatisticsAdditionalConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
