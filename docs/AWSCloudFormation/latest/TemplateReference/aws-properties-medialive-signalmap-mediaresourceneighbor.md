---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-signalmap-mediaresourceneighbor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::SignalMap MediaResourceNeighbor
<a name="aws-properties-medialive-signalmap-mediaresourceneighbor"></a>

A direct source or destination neighbor to an Amazon Web Services media resource.

## Syntax
<a name="aws-properties-medialive-signalmap-mediaresourceneighbor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-signalmap-mediaresourceneighbor-syntax.json"></a>

```
{
  "[Arn](#cfn-medialive-signalmap-mediaresourceneighbor-arn)" : {{String}},
  "[Name](#cfn-medialive-signalmap-mediaresourceneighbor-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-signalmap-mediaresourceneighbor-syntax.yaml"></a>

```
  [Arn](#cfn-medialive-signalmap-mediaresourceneighbor-arn): {{String}}
  [Name](#cfn-medialive-signalmap-mediaresourceneighbor-name): {{String}}
```

## Properties
<a name="aws-properties-medialive-signalmap-mediaresourceneighbor-properties"></a>

`Arn`  <a name="cfn-medialive-signalmap-mediaresourceneighbor-arn"></a>
The ARN of a resource used in Amazon Web Services media workflows.
*Required*: Yes
*Type*: String
*Pattern*: `^arn.+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-medialive-signalmap-mediaresourceneighbor-name"></a>
The logical name of an Amazon Web Services media resource.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
