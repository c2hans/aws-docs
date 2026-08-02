---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamPrefixListResolverRuleConditionRequest.html
---

# IpamPrefixListResolverRuleConditionRequest
<a name="API_IpamPrefixListResolverRuleConditionRequest"></a>

Describes a condition used when creating or modifying resolver rules.

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
<a name="API_IpamPrefixListResolverRuleConditionRequest_Contents"></a>

 ** Operation **
The operation to perform when evaluating this condition.
Type: String
Valid Values: `equals | not-equals | subnet-of`
Required: Yes

 ** Cidr **
A CIDR block to match against. This condition selects CIDRs that fall within or match the specified CIDR range.
Type: String
Required: No

 ** IpamPoolId **
The ID of the IPAM pool to match against. This condition selects CIDRs that belong to the specified IPAM pool.
Type: String
Required: No

 ** ResourceId **
The ID of the AWS resource to match against. This condition selects CIDRs associated with the specified resource.
Type: String
Required: No

 ** ResourceOwner **
The AWS account ID that owns the resources to match against. This condition selects CIDRs from resources owned by the specified account.
Type: String
Required: No

 ** ResourceRegion **
The AWS Region where the resources are located. This condition selects CIDRs from resources in the specified Region.
Type: String
Required: No

 ** ResourceTag **
A tag key-value pair to match against. This condition selects CIDRs from resources that have the specified tag.
Type: [RequestIpamResourceTag](API_RequestIpamResourceTag.md) object
Required: No

## See Also
<a name="API_IpamPrefixListResolverRuleConditionRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamPrefixListResolverRuleConditionRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamPrefixListResolverRuleConditionRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamPrefixListResolverRuleConditionRequest)
