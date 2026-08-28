---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-transitgatewaymeteringpolicy-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TransitGatewayMeteringPolicy Tag
<a name="aws-properties-ec2-transitgatewaymeteringpolicy-tag"></a>

Describes a tag.

## Syntax
<a name="aws-properties-ec2-transitgatewaymeteringpolicy-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-transitgatewaymeteringpolicy-tag-syntax.json"></a>

```
{
  "[Key](#cfn-ec2-transitgatewaymeteringpolicy-tag-key)" : {{String}},
  "[Value](#cfn-ec2-transitgatewaymeteringpolicy-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-transitgatewaymeteringpolicy-tag-syntax.yaml"></a>

```
  [Key](#cfn-ec2-transitgatewaymeteringpolicy-tag-key): {{String}}
  [Value](#cfn-ec2-transitgatewaymeteringpolicy-tag-value): {{String}}
```

## Properties
<a name="aws-properties-ec2-transitgatewaymeteringpolicy-tag-properties"></a>

`Key`  <a name="cfn-ec2-transitgatewaymeteringpolicy-tag-key"></a>
The key of the tag.
Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ec2-transitgatewaymeteringpolicy-tag-value"></a>
The value of the tag.
Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
