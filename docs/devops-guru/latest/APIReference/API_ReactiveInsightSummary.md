---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ReactiveInsightSummary.html
---

# ReactiveInsightSummary
<a name="API_ReactiveInsightSummary"></a>

 Information about a reactive insight. This object is returned by `DescribeInsight.`

## Contents
<a name="API_ReactiveInsightSummary_Contents"></a>

 ** AssociatedResourceArns **   <a name="DevOpsGuru-Type-ReactiveInsightSummary-AssociatedResourceArns"></a>
The Amazon Resource Names (ARNs) of the AWS resources that generated this insight.
Type: Array of strings
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** Id **   <a name="DevOpsGuru-Type-ReactiveInsightSummary-Id"></a>
 The ID of a reactive summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[\w-]*$`
Required: No

 ** InsightTimeRange **   <a name="DevOpsGuru-Type-ReactiveInsightSummary-InsightTimeRange"></a>
 A time ranged that specifies when the observed behavior in an insight started and ended.
Type: [InsightTimeRange](API_InsightTimeRange.md) object
Required: No

 ** Name **   <a name="DevOpsGuru-Type-ReactiveInsightSummary-Name"></a>
 The name of a reactive insight.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 530.
Pattern: `^[\s\S]*$`
Required: No

 ** ResourceCollection **   <a name="DevOpsGuru-Type-ReactiveInsightSummary-ResourceCollection"></a>
 A collection of AWS resources supported by DevOps Guru. The two types of AWS resource collections supported are AWS CloudFormation stacks and AWS resources that contain the same AWS tag. DevOps Guru can be configured to analyze the AWS resources that are defined in the stacks or that are tagged using the same tag *key*. You can specify up to 1000 AWS CloudFormation stacks.
Type: [ResourceCollection](API_ResourceCollection.md) object
Required: No

 ** ServiceCollection **   <a name="DevOpsGuru-Type-ReactiveInsightSummary-ServiceCollection"></a>
A collection of the names of AWS services.
Type: [ServiceCollection](API_ServiceCollection.md) object
Required: No

 ** Severity **   <a name="DevOpsGuru-Type-ReactiveInsightSummary-Severity"></a>
The severity of the insight. For more information, see [Understanding insight severities](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-insights.html#understanding-insights-severities) in the *Amazon DevOps Guru User Guide*.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

 ** Status **   <a name="DevOpsGuru-Type-ReactiveInsightSummary-Status"></a>
 The status of a reactive insight.
Type: String
Valid Values: `ONGOING | CLOSED`
Required: No

## See Also
<a name="API_ReactiveInsightSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/ReactiveInsightSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/ReactiveInsightSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/ReactiveInsightSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
