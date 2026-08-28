---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-inputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow InputConfiguration
<a name="aws-properties-mediaconnect-flow-inputconfiguration"></a>

 The transport parameters that are associated with an incoming media stream.

## Syntax
<a name="aws-properties-mediaconnect-flow-inputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-inputconfiguration-syntax.json"></a>

```
{
  "[InputPort](#cfn-mediaconnect-flow-inputconfiguration-inputport)" : {{Integer}},
  "[Interface](#cfn-mediaconnect-flow-inputconfiguration-interface)" : {{Interface}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-inputconfiguration-syntax.yaml"></a>

```
  [InputPort](#cfn-mediaconnect-flow-inputconfiguration-inputport): {{Integer}}
  [Interface](#cfn-mediaconnect-flow-inputconfiguration-interface): {{
    Interface}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-inputconfiguration-properties"></a>

`InputPort`  <a name="cfn-mediaconnect-flow-inputconfiguration-inputport"></a>
 The port that the flow listens on for an incoming media stream.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interface`  <a name="cfn-mediaconnect-flow-inputconfiguration-interface"></a>
 The VPC interface where the media stream comes in from.
*Required*: Yes
*Type*: [Interface](aws-properties-mediaconnect-flow-interface.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
