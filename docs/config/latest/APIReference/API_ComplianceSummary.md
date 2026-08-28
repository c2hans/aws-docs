---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ComplianceSummary.html
---

# ComplianceSummary
<a name="API_ComplianceSummary"></a>

The number of AWS Config rules or AWS resources that are compliant and noncompliant.

## Contents
<a name="API_ComplianceSummary_Contents"></a>

 ** ComplianceSummaryTimestamp **   <a name="config-Type-ComplianceSummary-ComplianceSummaryTimestamp"></a>
The time that AWS Config created the compliance summary.
Type: Timestamp
Required: No

 ** CompliantResourceCount **   <a name="config-Type-ComplianceSummary-CompliantResourceCount"></a>
The number of AWS Config rules or AWS resources that are compliant, up to a maximum of 25 for rules and 100 for resources.
Type: [ComplianceContributorCount](API_ComplianceContributorCount.md) object
Required: No

 ** NonCompliantResourceCount **   <a name="config-Type-ComplianceSummary-NonCompliantResourceCount"></a>
The number of AWS Config rules or AWS resources that are noncompliant, up to a maximum of 25 for rules and 100 for resources.
Type: [ComplianceContributorCount](API_ComplianceContributorCount.md) object
Required: No

## See Also
<a name="API_ComplianceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ComplianceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ComplianceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ComplianceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
