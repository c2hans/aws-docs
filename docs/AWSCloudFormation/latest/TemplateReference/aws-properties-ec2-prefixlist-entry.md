---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-prefixlist-entry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::PrefixList Entry
<a name="aws-properties-ec2-prefixlist-entry"></a>

An entry for a prefix list.

## Syntax
<a name="aws-properties-ec2-prefixlist-entry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-prefixlist-entry-syntax.json"></a>

```
{
  "[Cidr](#cfn-ec2-prefixlist-entry-cidr)" : {{String}},
  "[Description](#cfn-ec2-prefixlist-entry-description)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-prefixlist-entry-syntax.yaml"></a>

```
  [Cidr](#cfn-ec2-prefixlist-entry-cidr): {{String}}
  [Description](#cfn-ec2-prefixlist-entry-description): {{String}}
```

## Properties
<a name="aws-properties-ec2-prefixlist-entry-properties"></a>

`Cidr`  <a name="cfn-ec2-prefixlist-entry-cidr"></a>
The CIDR block.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `46`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-ec2-prefixlist-entry-description"></a>
A description for the entry.
Constraints: Up to 255 characters in length.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
