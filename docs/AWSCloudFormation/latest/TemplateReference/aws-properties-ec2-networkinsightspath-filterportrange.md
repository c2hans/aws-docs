---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-networkinsightspath-filterportrange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::NetworkInsightsPath FilterPortRange
<a name="aws-properties-ec2-networkinsightspath-filterportrange"></a>

Describes a port range.

## Syntax
<a name="aws-properties-ec2-networkinsightspath-filterportrange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-networkinsightspath-filterportrange-syntax.json"></a>

```
{
  "[FromPort](#cfn-ec2-networkinsightspath-filterportrange-fromport)" : {{Integer}},
  "[ToPort](#cfn-ec2-networkinsightspath-filterportrange-toport)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ec2-networkinsightspath-filterportrange-syntax.yaml"></a>

```
  [FromPort](#cfn-ec2-networkinsightspath-filterportrange-fromport): {{Integer}}
  [ToPort](#cfn-ec2-networkinsightspath-filterportrange-toport): {{Integer}}
```

## Properties
<a name="aws-properties-ec2-networkinsightspath-filterportrange-properties"></a>

`FromPort`  <a name="cfn-ec2-networkinsightspath-filterportrange-fromport"></a>
The first port in the range.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `65535`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ToPort`  <a name="cfn-ec2-networkinsightspath-filterportrange-toport"></a>
The last port in the range.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `65535`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
