---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-groupidentifier.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SpotFleet GroupIdentifier
<a name="aws-properties-ec2-spotfleet-groupidentifier"></a>

Describes a security group.

## Syntax
<a name="aws-properties-ec2-spotfleet-groupidentifier-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-spotfleet-groupidentifier-syntax.json"></a>

```
{
  "[GroupId](#cfn-ec2-spotfleet-groupidentifier-groupid)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-spotfleet-groupidentifier-syntax.yaml"></a>

```
  [GroupId](#cfn-ec2-spotfleet-groupidentifier-groupid): {{String}}
```

## Properties
<a name="aws-properties-ec2-spotfleet-groupidentifier-properties"></a>

`GroupId`  <a name="cfn-ec2-spotfleet-groupidentifier-groupid"></a>
The ID of the security group.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
