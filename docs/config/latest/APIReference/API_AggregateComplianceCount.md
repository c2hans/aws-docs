---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_AggregateComplianceCount.html
---

# AggregateComplianceCount
<a name="API_AggregateComplianceCount"></a>

Returns the number of compliant and noncompliant rules for one or more accounts and regions in an aggregator.

## Contents
<a name="API_AggregateComplianceCount_Contents"></a>

 ** ComplianceSummary **   <a name="config-Type-AggregateComplianceCount-ComplianceSummary"></a>
The number of compliant and noncompliant AWS Config rules.
Type: [ComplianceSummary](API_ComplianceSummary.md) object
Required: No

 ** GroupName **   <a name="config-Type-AggregateComplianceCount-GroupName"></a>
The 12-digit account ID or region based on the GroupByKey value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_AggregateComplianceCount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/AggregateComplianceCount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/AggregateComplianceCount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/AggregateComplianceCount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
