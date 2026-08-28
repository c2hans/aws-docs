---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_AggregateConformancePackComplianceSummary.html
---

# AggregateConformancePackComplianceSummary
<a name="API_AggregateConformancePackComplianceSummary"></a>

Provides a summary of compliance based on either account ID or region.

## Contents
<a name="API_AggregateConformancePackComplianceSummary_Contents"></a>

 ** ComplianceSummary **   <a name="config-Type-AggregateConformancePackComplianceSummary-ComplianceSummary"></a>
Returns an `AggregateConformancePackComplianceCount` object.
Type: [AggregateConformancePackComplianceCount](API_AggregateConformancePackComplianceCount.md) object
Required: No

 ** GroupName **   <a name="config-Type-AggregateConformancePackComplianceSummary-GroupName"></a>
Groups the result based on AWS account ID or AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_AggregateConformancePackComplianceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/AggregateConformancePackComplianceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/AggregateConformancePackComplianceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/AggregateConformancePackComplianceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
