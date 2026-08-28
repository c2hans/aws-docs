---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_SearchOrganizationInsightsFilters.html
---

# SearchOrganizationInsightsFilters
<a name="API_SearchOrganizationInsightsFilters"></a>

 Filters you can use to specify which events are returned when `ListEvents` is called.

## Contents
<a name="API_SearchOrganizationInsightsFilters_Contents"></a>

 ** ResourceCollection **   <a name="DevOpsGuru-Type-SearchOrganizationInsightsFilters-ResourceCollection"></a>
 A collection of AWS resources supported by DevOps Guru. The two types of AWS resource collections supported are AWS CloudFormation stacks and AWS resources that contain the same AWS tag. DevOps Guru can be configured to analyze the AWS resources that are defined in the stacks or that are tagged using the same tag *key*. You can specify up to 1000 AWS CloudFormation stacks.
Type: [ResourceCollection](API_ResourceCollection.md) object
Required: No

 ** ServiceCollection **   <a name="DevOpsGuru-Type-SearchOrganizationInsightsFilters-ServiceCollection"></a>
A collection of the names of AWS services.
Type: [ServiceCollection](API_ServiceCollection.md) object
Required: No

 ** Severities **   <a name="DevOpsGuru-Type-SearchOrganizationInsightsFilters-Severities"></a>
 An array of severity values used to search for insights.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

 ** Statuses **   <a name="DevOpsGuru-Type-SearchOrganizationInsightsFilters-Statuses"></a>
 An array of status values used to search for insights.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `ONGOING | CLOSED`
Required: No

## See Also
<a name="API_SearchOrganizationInsightsFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/SearchOrganizationInsightsFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/SearchOrganizationInsightsFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/SearchOrganizationInsightsFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
