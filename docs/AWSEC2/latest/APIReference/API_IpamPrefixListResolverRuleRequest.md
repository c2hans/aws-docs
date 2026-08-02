---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamPrefixListResolverRuleRequest.html
---

# IpamPrefixListResolverRuleRequest
<a name="API_IpamPrefixListResolverRuleRequest"></a>

Describes a CIDR selection rule to include in a request. This is used when creating or modifying resolver rules.

CIDR selection rules define the business logic for selecting CIDRs from IPAM. If a CIDR matches any of the rules, it will be included. If a rule has multiple conditions, the CIDR has to match every condition of that rule. You can create a prefix list resolver without any CIDR selection rules, but it will generate empty versions (containing no CIDRs) until you add rules.

There are three rule types. Only 2 of the 3 rule types support conditions - **IPAM pool CIDR** and **Scope resource CIDR**. **Static CIDR** rules cannot have conditions.
+  **Static CIDR**: A fixed list of CIDRs that do not change (like a manual list replicated across Regions)
+  **IPAM pool CIDR**: CIDRs from specific IPAM pools (like all CIDRs from your IPAM production pool)

  If you choose this option, choose the following:
  +  **IPAM scope**: Select the IPAM scope to search for resources
  +  **Conditions:**
    +  **Property**
      +  **IPAM pool ID**: Select an IPAM pool that contains the resources
      +  **CIDR** (like 10.24.34.0/23)
    +  **Operation**: Equals/Not equals
    +  **Value**: The value on which to match the condition
+  **Scope resource CIDR**: CIDRs from AWS resources like VPCs, subnets, EIPs within an IPAM scope

  If you choose this option, choose the following:
  +  **IPAM scope**: Select the IPAM scope to search for resources
  +  **Resource type**: Select a resource, like a VPC or subnet.
  +  **Conditions**:
    +  **Property**:
      + Resource ID: The unique ID of a resource (like vpc-1234567890abcdef0)
      + Resource owner (like 111122223333)
      + Resource region (like us-east-1)
      + Resource tag (like key: name, value: dev-vpc-1)
      + CIDR (like 10.24.34.0/23)
    +  **Operation**: Equals/Not equals
    +  **Value**: The value on which to match the condition

## Contents
<a name="API_IpamPrefixListResolverRuleRequest_Contents"></a>

 ** RuleType **
The type of CIDR selection rule. Valid values include `include` for selecting CIDRs that match the conditions, and `exclude` for excluding CIDRs that match the conditions.
Type: String
Valid Values: `static-cidr | ipam-resource-cidr | ipam-pool-cidr`
Required: Yes

 ** Condition.N **
The conditions that determine which CIDRs are selected by this rule. Conditions specify criteria such as resource type, tags, account IDs, and Regions.
Type: Array of [IpamPrefixListResolverRuleConditionRequest](API_IpamPrefixListResolverRuleConditionRequest.md) objects
Required: No

 ** IpamScopeId **
The ID of the IPAM scope from which to select CIDRs. This determines whether to select from public or private IP address space.
Type: String
Required: No

 ** ResourceType **
For rules of type `ipam-resource-cidr`, this is the resource type.
Type: String
Valid Values: `vpc | subnet | eip | public-ipv4-pool | ipv6-pool | eni | anycast-ip-list`
Required: No

 ** StaticCidr **
A fixed list of CIDRs that do not change (like a manual list replicated across Regions).
Type: String
Required: No

## See Also
<a name="API_IpamPrefixListResolverRuleRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamPrefixListResolverRuleRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamPrefixListResolverRuleRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamPrefixListResolverRuleRequest)
