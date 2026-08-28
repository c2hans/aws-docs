---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-networkinsightsanalysis-analysissecuritygrouprule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::NetworkInsightsAnalysis AnalysisSecurityGroupRule
<a name="aws-properties-ec2-networkinsightsanalysis-analysissecuritygrouprule"></a>

Describes a security group rule.

## Syntax
<a name="aws-properties-ec2-networkinsightsanalysis-analysissecuritygrouprule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-networkinsightsanalysis-analysissecuritygrouprule-syntax.json"></a>

```
{
  "[Cidr](#cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-cidr)" : {{String}},
  "[Direction](#cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-direction)" : {{String}},
  "[PortRange](#cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-portrange)" : {{PortRange}},
  "[PrefixListId](#cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-prefixlistid)" : {{String}},
  "[Protocol](#cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-protocol)" : {{String}},
  "[SecurityGroupId](#cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-securitygroupid)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-networkinsightsanalysis-analysissecuritygrouprule-syntax.yaml"></a>

```
  [Cidr](#cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-cidr): {{String}}
  [Direction](#cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-direction): {{String}}
  [PortRange](#cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-portrange): {{
    PortRange}}
  [PrefixListId](#cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-prefixlistid): {{String}}
  [Protocol](#cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-protocol): {{String}}
  [SecurityGroupId](#cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-securitygroupid): {{String}}
```

## Properties
<a name="aws-properties-ec2-networkinsightsanalysis-analysissecuritygrouprule-properties"></a>

`Cidr`  <a name="cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-cidr"></a>
The IPv4 address range, in CIDR notation.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Direction`  <a name="cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-direction"></a>
The direction. The following are the possible values:
+ egress
+ ingress
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PortRange`  <a name="cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-portrange"></a>
The port range.
*Required*: No
*Type*: [PortRange](aws-properties-ec2-networkinsightsanalysis-portrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrefixListId`  <a name="cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-prefixlistid"></a>
The prefix list ID.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-protocol"></a>
The protocol name.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupId`  <a name="cfn-ec2-networkinsightsanalysis-analysissecuritygrouprule-securitygroupid"></a>
The security group ID.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
