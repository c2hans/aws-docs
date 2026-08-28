---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ReactiveOrganizationInsightSummary.html
---

# ReactiveOrganizationInsightSummary
<a name="API_ReactiveOrganizationInsightSummary"></a>

Information about a reactive insight. This object is returned by `DescribeInsight`.

## Contents
<a name="API_ReactiveOrganizationInsightSummary_Contents"></a>

 ** AccountId **   <a name="DevOpsGuru-Type-ReactiveOrganizationInsightSummary-AccountId"></a>
The ID of the AWS account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** Id **   <a name="DevOpsGuru-Type-ReactiveOrganizationInsightSummary-Id"></a>
The ID of the insight summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[\w-]*$`
Required: No

 ** InsightTimeRange **   <a name="DevOpsGuru-Type-ReactiveOrganizationInsightSummary-InsightTimeRange"></a>
 A time ranged that specifies when the observed behavior in an insight started and ended.
Type: [InsightTimeRange](API_InsightTimeRange.md) object
Required: No

 ** Name **   <a name="DevOpsGuru-Type-ReactiveOrganizationInsightSummary-Name"></a>
The name of the insight summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 530.
Pattern: `^[\s\S]*$`
Required: No

 ** OrganizationalUnitId **   <a name="DevOpsGuru-Type-ReactiveOrganizationInsightSummary-OrganizationalUnitId"></a>
The ID of the organizational unit.
Type: String
Length Constraints: Maximum length of 68.
Pattern: `^ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}$`
Required: No

 ** ResourceCollection **   <a name="DevOpsGuru-Type-ReactiveOrganizationInsightSummary-ResourceCollection"></a>
 A collection of AWS resources supported by DevOps Guru. The two types of AWS resource collections supported are AWS CloudFormation stacks and AWS resources that contain the same AWS tag. DevOps Guru can be configured to analyze the AWS resources that are defined in the stacks or that are tagged using the same tag *key*. You can specify up to 1000 AWS CloudFormation stacks.
Type: [ResourceCollection](API_ResourceCollection.md) object
Required: No

 ** ServiceCollection **   <a name="DevOpsGuru-Type-ReactiveOrganizationInsightSummary-ServiceCollection"></a>
A collection of the names of AWS services.
Type: [ServiceCollection](API_ServiceCollection.md) object
Required: No

 ** Severity **   <a name="DevOpsGuru-Type-ReactiveOrganizationInsightSummary-Severity"></a>
 An array of severity values used to search for insights. For more information, see [Understanding insight severities](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-insights.html#understanding-insights-severities) in the *Amazon DevOps Guru User Guide*.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

 ** Status **   <a name="DevOpsGuru-Type-ReactiveOrganizationInsightSummary-Status"></a>
 An array of status values used to search for insights.
Type: String
Valid Values: `ONGOING | CLOSED`
Required: No

## See Also
<a name="API_ReactiveOrganizationInsightSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/ReactiveOrganizationInsightSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/ReactiveOrganizationInsightSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/ReactiveOrganizationInsightSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
