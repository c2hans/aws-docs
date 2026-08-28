---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-networkinsightsaccessscope-pathstatementrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::NetworkInsightsAccessScope PathStatementRequest
<a name="aws-properties-ec2-networkinsightsaccessscope-pathstatementrequest"></a>

Describes a path statement.

## Syntax
<a name="aws-properties-ec2-networkinsightsaccessscope-pathstatementrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-networkinsightsaccessscope-pathstatementrequest-syntax.json"></a>

```
{
  "[PacketHeaderStatement](#cfn-ec2-networkinsightsaccessscope-pathstatementrequest-packetheaderstatement)" : {{PacketHeaderStatementRequest}},
  "[ResourceStatement](#cfn-ec2-networkinsightsaccessscope-pathstatementrequest-resourcestatement)" : {{ResourceStatementRequest}}
}
```

### YAML
<a name="aws-properties-ec2-networkinsightsaccessscope-pathstatementrequest-syntax.yaml"></a>

```
  [PacketHeaderStatement](#cfn-ec2-networkinsightsaccessscope-pathstatementrequest-packetheaderstatement): {{
    PacketHeaderStatementRequest}}
  [ResourceStatement](#cfn-ec2-networkinsightsaccessscope-pathstatementrequest-resourcestatement): {{
    ResourceStatementRequest}}
```

## Properties
<a name="aws-properties-ec2-networkinsightsaccessscope-pathstatementrequest-properties"></a>

`PacketHeaderStatement`  <a name="cfn-ec2-networkinsightsaccessscope-pathstatementrequest-packetheaderstatement"></a>
The packet header statement.
*Required*: No
*Type*: [PacketHeaderStatementRequest](aws-properties-ec2-networkinsightsaccessscope-packetheaderstatementrequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceStatement`  <a name="cfn-ec2-networkinsightsaccessscope-pathstatementrequest-resourcestatement"></a>
The resource statement.
*Required*: No
*Type*: [ResourceStatementRequest](aws-properties-ec2-networkinsightsaccessscope-resourcestatementrequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
