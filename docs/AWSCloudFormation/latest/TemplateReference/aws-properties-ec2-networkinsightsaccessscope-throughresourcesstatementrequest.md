---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-networkinsightsaccessscope-throughresourcesstatementrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::NetworkInsightsAccessScope ThroughResourcesStatementRequest
<a name="aws-properties-ec2-networkinsightsaccessscope-throughresourcesstatementrequest"></a>

Describes a through resource statement.

## Syntax
<a name="aws-properties-ec2-networkinsightsaccessscope-throughresourcesstatementrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-networkinsightsaccessscope-throughresourcesstatementrequest-syntax.json"></a>

```
{
  "[ResourceStatement](#cfn-ec2-networkinsightsaccessscope-throughresourcesstatementrequest-resourcestatement)" : {{ResourceStatementRequest}}
}
```

### YAML
<a name="aws-properties-ec2-networkinsightsaccessscope-throughresourcesstatementrequest-syntax.yaml"></a>

```
  [ResourceStatement](#cfn-ec2-networkinsightsaccessscope-throughresourcesstatementrequest-resourcestatement): {{
    ResourceStatementRequest}}
```

## Properties
<a name="aws-properties-ec2-networkinsightsaccessscope-throughresourcesstatementrequest-properties"></a>

`ResourceStatement`  <a name="cfn-ec2-networkinsightsaccessscope-throughresourcesstatementrequest-resourcestatement"></a>
The resource statement.
*Required*: No
*Type*: [ResourceStatementRequest](aws-properties-ec2-networkinsightsaccessscope-resourcestatementrequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
