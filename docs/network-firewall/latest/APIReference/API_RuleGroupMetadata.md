---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_RuleGroupMetadata.html
---

# RuleGroupMetadata
<a name="API_RuleGroupMetadata"></a>

High-level information about a rule group, returned by [ListRuleGroups](API_ListRuleGroups.md). You can use the information provided in the metadata to retrieve and manage a rule group.

## Contents
<a name="API_RuleGroupMetadata_Contents"></a>

 ** Arn **   <a name="networkfirewall-Type-RuleGroupMetadata-Arn"></a>
The Amazon Resource Name (ARN) of the rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`
Required: No

 ** Name **   <a name="networkfirewall-Type-RuleGroupMetadata-Name"></a>
The descriptive name of the rule group. You can't change the name of a rule group after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

 ** VendorName **   <a name="networkfirewall-Type-RuleGroupMetadata-VendorName"></a>
The name of the AWS Marketplace seller that provides this rule group.
Type: String
Required: No

## See Also
<a name="API_RuleGroupMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/RuleGroupMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/RuleGroupMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/RuleGroupMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
