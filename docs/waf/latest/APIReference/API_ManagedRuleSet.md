---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ManagedRuleSet.html
---

# ManagedRuleSet
<a name="API_ManagedRuleSet"></a>

A set of rules that is managed by AWS and AWS Marketplace sellers to provide versioned managed rule groups for customers of AWS WAF.

**Note**
This is intended for use only by vendors of managed rule sets. Vendors are AWS and AWS Marketplace sellers.
Vendors, you can use the managed rule set APIs to provide controlled rollout of your versioned managed rule group offerings for your customers. The APIs are `ListManagedRuleSets`, `GetManagedRuleSet`, `PutManagedRuleSetVersions`, and `UpdateManagedRuleSetVersionExpiryDate`.

## Contents
<a name="API_ManagedRuleSet_Contents"></a>

 ** ARN **   <a name="WAF-Type-ManagedRuleSet-ARN"></a>
The Amazon Resource Name (ARN) of the entity.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*\S.*`
Required: Yes

 ** Id **   <a name="WAF-Type-ManagedRuleSet-Id"></a>
A unique identifier for the managed rule set. The ID is returned in the responses to commands like `list`. You provide it to operations like `get` and `update`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`
Required: Yes

 ** Name **   <a name="WAF-Type-ManagedRuleSet-Name"></a>
The name of the managed rule set. You use this, along with the rule set ID, to identify the rule set.
This name is assigned to the corresponding managed rule group, which your customers can access and use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\w\-]+$`
Required: Yes

 ** Description **   <a name="WAF-Type-ManagedRuleSet-Description"></a>
A description of the set that helps with identification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[\w+=:#@/\-,\.][\w+=:#@/\-,\.\s]+[\w+=:#@/\-,\.]$`
Required: No

 ** LabelNamespace **   <a name="WAF-Type-ManagedRuleSet-LabelNamespace"></a>
The label namespace prefix for the managed rule groups that are offered to customers from this managed rule set. All labels that are added by rules in the managed rule group have this prefix.
+ The syntax for the label namespace prefix for a managed rule group is the following:

   `awswaf:managed:<vendor>:<rule group name>`:
+ When a rule with a label matches a web request, AWS WAF adds the fully qualified label to the request. A fully qualified label is made up of the label namespace from the rule group or web ACL where the rule is defined and the label from the rule, separated by a colon:

   `<label namespace>:<label from rule>`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9A-Za-z_\-:]+$`
Required: No

 ** PublishedVersions **   <a name="WAF-Type-ManagedRuleSet-PublishedVersions"></a>
The versions of this managed rule set that are available for use by customers.
Type: String to [ManagedRuleSetVersion](API_ManagedRuleSetVersion.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[\w#:\.\-/]+$`
Required: No

 ** RecommendedVersion **   <a name="WAF-Type-ManagedRuleSet-RecommendedVersion"></a>
The version that you would like your customers to use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[\w#:\.\-/]+$`
Required: No

## See Also
<a name="API_ManagedRuleSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ManagedRuleSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ManagedRuleSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ManagedRuleSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
