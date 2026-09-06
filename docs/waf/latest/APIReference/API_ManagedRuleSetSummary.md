---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ManagedRuleSetSummary.html
---

# ManagedRuleSetSummary
<a name="API_ManagedRuleSetSummary"></a>

High-level information for a managed rule set.

**Note**
This is intended for use only by vendors of managed rule sets. Vendors are AWS and AWS Marketplace sellers.
Vendors, you can use the managed rule set APIs to provide controlled rollout of your versioned managed rule group offerings for your customers. The APIs are `ListManagedRuleSets`, `GetManagedRuleSet`, `PutManagedRuleSetVersions`, and `UpdateManagedRuleSetVersionExpiryDate`.

## Contents
<a name="API_ManagedRuleSetSummary_Contents"></a>

 ** ARN **   <a name="WAF-Type-ManagedRuleSetSummary-ARN"></a>
The Amazon Resource Name (ARN) of the entity.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** Description **   <a name="WAF-Type-ManagedRuleSetSummary-Description"></a>
A description of the set that helps with identification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[\w+=:#@/\-,\.][\w+=:#@/\-,\.\s]+[\w+=:#@/\-,\.]$`
Required: No

 ** Id **   <a name="WAF-Type-ManagedRuleSetSummary-Id"></a>
A unique identifier for the managed rule set. The ID is returned in the responses to commands like `list`. You provide it to operations like `get` and `update`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`
Required: No

 ** LabelNamespace **   <a name="WAF-Type-ManagedRuleSetSummary-LabelNamespace"></a>
The label namespace prefix for the managed rule groups that are offered to customers from this managed rule set. All labels that are added by rules in the managed rule group have this prefix.
+ The syntax for the label namespace prefix for a managed rule group is the following:

   `awswaf:managed:<vendor>:<rule group name>`:
+ When a rule with a label matches a web request, AWS WAF adds the fully qualified label to the request. A fully qualified label is made up of the label namespace from the rule group or web ACL where the rule is defined and the label from the rule, separated by a colon:

   `<label namespace>:<label from rule>`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9A-Za-z_\-:]+$`
Required: No

 ** LockToken **   <a name="WAF-Type-ManagedRuleSetSummary-LockToken"></a>
A token used for optimistic locking. AWS WAF returns a token to your `get` and `list` requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like `update` and `delete`. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a `WAFOptimisticLockException`. If this happens, perform another `get`, and use the new token returned by that operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`
Required: No

 ** Name **   <a name="WAF-Type-ManagedRuleSetSummary-Name"></a>
The name of the managed rule set. You use this, along with the rule set ID, to identify the rule set.
This name is assigned to the corresponding managed rule group, which your customers can access and use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\w\-]+$`
Required: No

## See Also
<a name="API_ManagedRuleSetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ManagedRuleSetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ManagedRuleSetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ManagedRuleSetSummary)
