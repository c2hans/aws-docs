---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-networkinsightsaccessscope-accessscopepathrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::NetworkInsightsAccessScope AccessScopePathRequest
<a name="aws-properties-ec2-networkinsightsaccessscope-accessscopepathrequest"></a>

Describes a path.

## Syntax
<a name="aws-properties-ec2-networkinsightsaccessscope-accessscopepathrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-networkinsightsaccessscope-accessscopepathrequest-syntax.json"></a>

```
{
  "[Destination](#cfn-ec2-networkinsightsaccessscope-accessscopepathrequest-destination)" : {{PathStatementRequest}},
  "[Source](#cfn-ec2-networkinsightsaccessscope-accessscopepathrequest-source)" : {{PathStatementRequest}},
  "[ThroughResources](#cfn-ec2-networkinsightsaccessscope-accessscopepathrequest-throughresources)" : {{[ ThroughResourcesStatementRequest, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-networkinsightsaccessscope-accessscopepathrequest-syntax.yaml"></a>

```
  [Destination](#cfn-ec2-networkinsightsaccessscope-accessscopepathrequest-destination): {{
    PathStatementRequest}}
  [Source](#cfn-ec2-networkinsightsaccessscope-accessscopepathrequest-source): {{
    PathStatementRequest}}
  [ThroughResources](#cfn-ec2-networkinsightsaccessscope-accessscopepathrequest-throughresources): {{
    - ThroughResourcesStatementRequest}}
```

## Properties
<a name="aws-properties-ec2-networkinsightsaccessscope-accessscopepathrequest-properties"></a>

`Destination`  <a name="cfn-ec2-networkinsightsaccessscope-accessscopepathrequest-destination"></a>
The destination.
*Required*: No
*Type*: [PathStatementRequest](aws-properties-ec2-networkinsightsaccessscope-pathstatementrequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Source`  <a name="cfn-ec2-networkinsightsaccessscope-accessscopepathrequest-source"></a>
The source.
*Required*: No
*Type*: [PathStatementRequest](aws-properties-ec2-networkinsightsaccessscope-pathstatementrequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ThroughResources`  <a name="cfn-ec2-networkinsightsaccessscope-accessscopepathrequest-throughresources"></a>
The through resources.
*Required*: No
*Type*: Array of [ThroughResourcesStatementRequest](aws-properties-ec2-networkinsightsaccessscope-throughresourcesstatementrequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
