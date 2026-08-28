---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-networkinsightsaccessscope-resourcestatementrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::NetworkInsightsAccessScope ResourceStatementRequest
<a name="aws-properties-ec2-networkinsightsaccessscope-resourcestatementrequest"></a>

Describes a resource statement.

## Syntax
<a name="aws-properties-ec2-networkinsightsaccessscope-resourcestatementrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-networkinsightsaccessscope-resourcestatementrequest-syntax.json"></a>

```
{
  "[Resources](#cfn-ec2-networkinsightsaccessscope-resourcestatementrequest-resources)" : {{[ String, ... ]}},
  "[ResourceTypes](#cfn-ec2-networkinsightsaccessscope-resourcestatementrequest-resourcetypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-networkinsightsaccessscope-resourcestatementrequest-syntax.yaml"></a>

```
  [Resources](#cfn-ec2-networkinsightsaccessscope-resourcestatementrequest-resources): {{
    - String}}
  [ResourceTypes](#cfn-ec2-networkinsightsaccessscope-resourcestatementrequest-resourcetypes): {{
    - String}}
```

## Properties
<a name="aws-properties-ec2-networkinsightsaccessscope-resourcestatementrequest-properties"></a>

`Resources`  <a name="cfn-ec2-networkinsightsaccessscope-resourcestatementrequest-resources"></a>
The resources.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceTypes`  <a name="cfn-ec2-networkinsightsaccessscope-resourcestatementrequest-resourcetypes"></a>
The resource types.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
