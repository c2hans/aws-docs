---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamPrefixListResolverRule.html
---

# IpamPrefixListResolverRule
<a name="API_IpamPrefixListResolverRule"></a>

Describes a CIDR selection rule.

CIDR selection rules define the business logic for selecting CIDRs from IPAM. If a CIDR matches any of the rules, it will be included. If a rule has multiple conditions, the CIDR has to match every condition of that rule. You can create a prefix list resolver without any CIDR selection rules, but it will generate empty versions (containing no CIDRs) until you add rules.

## Contents
<a name="API_IpamPrefixListResolverRule_Contents"></a>

 ** ConditionSet.N **
The conditions that determine which CIDRs are selected by this rule. Conditions specify criteria such as resource type, tags, account IDs, and Regions.
Type: Array of [IpamPrefixListResolverRuleCondition](API_IpamPrefixListResolverRuleCondition.md) objects
Required: No

 ** ipamScopeId **
The ID of the IPAM scope from which to select CIDRs. This determines whether to select from public or private IP address space.
Type: String
Required: No

 ** resourceType **
For rules of type `ipam-resource-cidr`, this is the resource type.
Type: String
Valid Values: `vpc | subnet | eip | public-ipv4-pool | ipv6-pool | eni | anycast-ip-list`
Required: No

 ** ruleType **
The type of CIDR selection rule. Valid values include `include` for selecting CIDRs that match the conditions, and `exclude` for excluding CIDRs that match the conditions.
Type: String
Valid Values: `static-cidr | ipam-resource-cidr | ipam-pool-cidr`
Required: No

 ** staticCidr **
A fixed list of CIDRs that do not change (like a manual list replicated across Regions).
Type: String
Required: No

## See Also
<a name="API_IpamPrefixListResolverRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamPrefixListResolverRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamPrefixListResolverRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamPrefixListResolverRule)
