---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ResourceComplianceSummaryItem.html
---

# ResourceComplianceSummaryItem
<a name="API_ResourceComplianceSummaryItem"></a>

Compliance summary information for a specific resource.

## Contents
<a name="API_ResourceComplianceSummaryItem_Contents"></a>

 ** ComplianceType **   <a name="systemsmanager-Type-ResourceComplianceSummaryItem-ComplianceType"></a>
The compliance type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([A-Za-z0-9_\-]\w+|Custom:[a-zA-Z0-9_\-]\w+)$`
Required: No

 ** CompliantSummary **   <a name="systemsmanager-Type-ResourceComplianceSummaryItem-CompliantSummary"></a>
A list of items that are compliant for the resource.
Type: [CompliantSummary](API_CompliantSummary.md) object
Required: No

 ** ExecutionSummary **   <a name="systemsmanager-Type-ResourceComplianceSummaryItem-ExecutionSummary"></a>
Information about the execution.
Type: [ComplianceExecutionSummary](API_ComplianceExecutionSummary.md) object
Required: No

 ** NonCompliantSummary **   <a name="systemsmanager-Type-ResourceComplianceSummaryItem-NonCompliantSummary"></a>
A list of items that aren't compliant for the resource.
Type: [NonCompliantSummary](API_NonCompliantSummary.md) object
Required: No

 ** OverallSeverity **   <a name="systemsmanager-Type-ResourceComplianceSummaryItem-OverallSeverity"></a>
The highest severity item found for the resource. The resource is compliant for this item.
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | INFORMATIONAL | UNSPECIFIED`
Required: No

 ** ResourceId **   <a name="systemsmanager-Type-ResourceComplianceSummaryItem-ResourceId"></a>
The resource ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** ResourceType **   <a name="systemsmanager-Type-ResourceComplianceSummaryItem-ResourceType"></a>
The resource type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** Status **   <a name="systemsmanager-Type-ResourceComplianceSummaryItem-Status"></a>
The compliance status for the resource.
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT`
Required: No

## See Also
<a name="API_ResourceComplianceSummaryItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ResourceComplianceSummaryItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ResourceComplianceSummaryItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ResourceComplianceSummaryItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
