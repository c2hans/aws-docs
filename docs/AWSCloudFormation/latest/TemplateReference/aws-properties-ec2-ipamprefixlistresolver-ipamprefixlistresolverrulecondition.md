---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::IPAMPrefixListResolver IpamPrefixListResolverRuleCondition
<a name="aws-properties-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition"></a>

Describes a condition within a CIDR selection rule. Conditions define the criteria for selecting CIDRs from IPAM's database based on resource attributes.

CIDR selection rules define the business logic for selecting CIDRs from IPAM. If a CIDR matches any of the rules, it will be included. If a rule has multiple conditions, the CIDR has to match every condition of that rule. You can create a prefix list resolver without any CIDR selection rules, but it will generate empty versions (containing no CIDRs) until you add rules.

There are three rule types. Only 2 of the 3 rule types support conditions - **IPAM pool CIDR** and **Scope resource CIDR**. **Static CIDR** rules cannot have conditions.
+ **Static CIDR**: A fixed list of CIDRs that do not change (like a manual list replicated across Regions)
+ **IPAM pool CIDR**: CIDRs from specific IPAM pools (like all CIDRs from your IPAM production pool)

  If you choose this option, choose the following:
  + **IPAM scope**: Select the IPAM scope to search for resources
  +  **Conditions:**
    +  **Property**
      + **IPAM pool ID**: Select an IPAM pool that contains the resources
      + **CIDR** (like 10.24.34.0/23)
    + **Operation**: Equals/Not equals
    + **Value**: The value on which to match the condition
+ **Scope resource CIDR**: CIDRs from AWS resources like VPCs, subnets, EIPs within an IPAM scope

  If you choose this option, choose the following:
  + **IPAM scope**: Select the IPAM scope to search for resources
  + **Resource type**: Select a resource, like a VPC or subnet.
  + **Conditions**:
    + **Property**:
      + Resource ID: The unique ID of a resource (like vpc-1234567890abcdef0)
      + Resource owner (like 111122223333)
      + Resource region (like us-east-1)
      + Resource tag (like key: name, value: dev-vpc-1)
      + CIDR (like 10.24.34.0/23)
    + **Operation**: Equals/Not equals
    + **Value**: The value on which to match the condition

## Syntax
<a name="aws-properties-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-syntax.json"></a>

```
{
  "[Cidr](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-cidr)" : {{String}},
  "[IpamPoolId](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-ipampoolid)" : {{String}},
  "[Operation](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-operation)" : {{String}},
  "[ResourceId](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-resourceid)" : {{String}},
  "[ResourceOwner](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-resourceowner)" : {{String}},
  "[ResourceRegion](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-resourceregion)" : {{String}},
  "[ResourceTag](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-resourcetag)" : {{Tag}}
}
```

### YAML
<a name="aws-properties-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-syntax.yaml"></a>

```
  [Cidr](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-cidr): {{String}}
  [IpamPoolId](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-ipampoolid): {{String}}
  [Operation](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-operation): {{String}}
  [ResourceId](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-resourceid): {{String}}
  [ResourceOwner](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-resourceowner): {{String}}
  [ResourceRegion](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-resourceregion): {{String}}
  [ResourceTag](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-resourcetag): {{
    Tag}}
```

## Properties
<a name="aws-properties-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-properties"></a>

`Cidr`  <a name="cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-cidr"></a>
A CIDR block to match against. This condition selects CIDRs that fall within or match the specified CIDR range.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpamPoolId`  <a name="cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-ipampoolid"></a>
The ID of the IPAM pool to match against. This condition selects CIDRs that belong to the specified IPAM pool.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Operation`  <a name="cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-operation"></a>
The operation to perform when evaluating this condition. Valid values include `equals`, `not-equals`, and `subnet-of`.
*Required*: No
*Type*: String
*Allowed values*: `equals | not-equals | subnet-of`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceId`  <a name="cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-resourceid"></a>
The ID of the AWS resource to match against. This condition selects CIDRs associated with the specified resource.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceOwner`  <a name="cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-resourceowner"></a>
The AWS account ID that owns the resources to match against. This condition selects CIDRs from resources owned by the specified account.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceRegion`  <a name="cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-resourceregion"></a>
The AWS Region where the resources are located. This condition selects CIDRs from resources in the specified Region.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceTag`  <a name="cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition-resourcetag"></a>
A tag key-value pair to match against. This condition selects CIDRs from resources that have the specified tag.
*Required*: No
*Type*: [Tag](aws-properties-ec2-ipamprefixlistresolver-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
