---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-sourcepriority.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow SourcePriority
<a name="aws-properties-mediaconnect-flow-sourcepriority"></a>

 The priority you want to assign to a source. You can have a primary stream and a backup stream or two equally prioritized streams.

## Syntax
<a name="aws-properties-mediaconnect-flow-sourcepriority-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-sourcepriority-syntax.json"></a>

```
{
  "[PrimarySource](#cfn-mediaconnect-flow-sourcepriority-primarysource)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-sourcepriority-syntax.yaml"></a>

```
  [PrimarySource](#cfn-mediaconnect-flow-sourcepriority-primarysource): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-sourcepriority-properties"></a>

`PrimarySource`  <a name="cfn-mediaconnect-flow-sourcepriority-primarysource"></a>
 The name of the source you choose as the primary source for this flow.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
