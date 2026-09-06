---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ComplianceSummaryItem.html
---

# ComplianceSummaryItem
<a name="API_ComplianceSummaryItem"></a>

A summary of compliance information by compliance type.

## Contents
<a name="API_ComplianceSummaryItem_Contents"></a>

 ** ComplianceType **   <a name="systemsmanager-Type-ComplianceSummaryItem-ComplianceType"></a>
The type of compliance item. For example, the compliance type can be Association, Patch, or Custom:string.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([A-Za-z0-9_\-]\w+|Custom:[a-zA-Z0-9_\-]\w+)$`
Required: No

 ** CompliantSummary **   <a name="systemsmanager-Type-ComplianceSummaryItem-CompliantSummary"></a>
A list of COMPLIANT items for the specified compliance type.
Type: [CompliantSummary](API_CompliantSummary.md) object
Required: No

 ** NonCompliantSummary **   <a name="systemsmanager-Type-ComplianceSummaryItem-NonCompliantSummary"></a>
A list of NON\_COMPLIANT items for the specified compliance type.
Type: [NonCompliantSummary](API_NonCompliantSummary.md) object
Required: No

## See Also
<a name="API_ComplianceSummaryItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ComplianceSummaryItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ComplianceSummaryItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ComplianceSummaryItem)
