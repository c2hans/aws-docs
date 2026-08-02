---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-ipamprefixlistresolver-ipamprefixlistresolverrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::IPAMPrefixListResolver IpamPrefixListResolverRule
<a name="aws-properties-ec2-ipamprefixlistresolver-ipamprefixlistresolverrule"></a>

Describes a CIDR selection rule.

CIDR selection rules define the business logic for selecting CIDRs from IPAM. If a CIDR matches any of the rules, it will be included. If a rule has multiple conditions, the CIDR has to match every condition of that rule. You can create a prefix list resolver without any CIDR selection rules, but it will generate empty versions (containing no CIDRs) until you add rules.

## Syntax
<a name="aws-properties-ec2-ipamprefixlistresolver-ipamprefixlistresolverrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-ipamprefixlistresolver-ipamprefixlistresolverrule-syntax.json"></a>

```
{
  "[Conditions](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrule-conditions)" : {{[ IpamPrefixListResolverRuleCondition, ... ]}},
  "[IpamScopeId](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrule-ipamscopeid)" : {{String}},
  "[ResourceType](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrule-resourcetype)" : {{String}},
  "[RuleType](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrule-ruletype)" : {{String}},
  "[StaticCidr](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrule-staticcidr)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-ipamprefixlistresolver-ipamprefixlistresolverrule-syntax.yaml"></a>

```
  [Conditions](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrule-conditions): {{
    - IpamPrefixListResolverRuleCondition}}
  [IpamScopeId](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrule-ipamscopeid): {{String}}
  [ResourceType](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrule-resourcetype): {{String}}
  [RuleType](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrule-ruletype): {{String}}
  [StaticCidr](#cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrule-staticcidr): {{String}}
```

## Properties
<a name="aws-properties-ec2-ipamprefixlistresolver-ipamprefixlistresolverrule-properties"></a>

`Conditions`  <a name="cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrule-conditions"></a>
The conditions that determine which CIDRs are selected by this rule. Conditions specify criteria such as resource type, tags, account IDs, and Regions.
*Required*: No
*Type*: Array of [IpamPrefixListResolverRuleCondition](aws-properties-ec2-ipamprefixlistresolver-ipamprefixlistresolverrulecondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpamScopeId`  <a name="cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrule-ipamscopeid"></a>
The ID of the IPAM scope from which to select CIDRs. This determines whether to select from public or private IP address space.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceType`  <a name="cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrule-resourcetype"></a>
For rules of type `ipam-resource-cidr`, this is the resource type.
*Required*: No
*Type*: String
*Allowed values*: `vpc | subnet | eip | public-ipv4-pool`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleType`  <a name="cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrule-ruletype"></a>
The type of CIDR selection rule. Valid values include `static-cidr` for specifying a fixed CIDR, `ipam-resource-cidr` for CIDRs from resources such as VPCs and subnets, and `ipam-pool-cidr` for CIDRs from IPAM pools.
*Required*: Yes
*Type*: String
*Allowed values*: `static-cidr | ipam-resource-cidr | ipam-pool-cidr`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StaticCidr`  <a name="cfn-ec2-ipamprefixlistresolver-ipamprefixlistresolverrule-staticcidr"></a>
A fixed CIDR that does not change. This property can only be specified for rules of type `static-cidr`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
