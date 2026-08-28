---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ManagedRuleGroupSummary.html
---

# ManagedRuleGroupSummary
<a name="API_ManagedRuleGroupSummary"></a>

High-level information about a managed rule group, returned by [ListAvailableManagedRuleGroups](API_ListAvailableManagedRuleGroups.md). This provides information like the name and vendor name, that you provide when you add a [ManagedRuleGroupStatement](API_ManagedRuleGroupStatement.md) to a web ACL. Managed rule groups include AWS Managed Rules rule groups and AWS Marketplace managed rule groups. To use any AWS Marketplace managed rule group, first subscribe to the rule group through AWS Marketplace.

## Contents
<a name="API_ManagedRuleGroupSummary_Contents"></a>

 ** Description **   <a name="WAF-Type-ManagedRuleGroupSummary-Description"></a>
The description of the managed rule group, provided by AWS Managed Rules or the AWS Marketplace seller who manages it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[\w+=:#@/\-,\.][\w+=:#@/\-,\.\s]+[\w+=:#@/\-,\.]$`
Required: No

 ** Name **   <a name="WAF-Type-ManagedRuleGroupSummary-Name"></a>
The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\w\-]+$`
Required: No

 ** VendorName **   <a name="WAF-Type-ManagedRuleGroupSummary-VendorName"></a>
The name of the managed rule group vendor. You use this, along with the rule group name, to identify a rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

 ** VersioningSupported **   <a name="WAF-Type-ManagedRuleGroupSummary-VersioningSupported"></a>
Indicates whether the managed rule group is versioned. If it is, you can retrieve the versions list by calling [ListAvailableManagedRuleGroupVersions](API_ListAvailableManagedRuleGroupVersions.md).
Type: Boolean
Required: No

## See Also
<a name="API_ManagedRuleGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ManagedRuleGroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ManagedRuleGroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ManagedRuleGroupSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
