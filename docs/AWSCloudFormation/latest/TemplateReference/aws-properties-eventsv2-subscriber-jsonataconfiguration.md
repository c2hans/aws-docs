---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-jsonataconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber JsonataConfiguration
<a name="aws-properties-eventsv2-subscriber-jsonataconfiguration"></a>

JSONata transform settings.

## Syntax
<a name="aws-properties-eventsv2-subscriber-jsonataconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-jsonataconfiguration-syntax.json"></a>

```
{
  "[Expression](#cfn-eventsv2-subscriber-jsonataconfiguration-expression)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-jsonataconfiguration-syntax.yaml"></a>

```
  [Expression](#cfn-eventsv2-subscriber-jsonataconfiguration-expression): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-jsonataconfiguration-properties"></a>

`Expression`  <a name="cfn-eventsv2-subscriber-jsonataconfiguration-expression"></a>
The JSONata expression that transforms the event, enclosed in {% %} delimiters.
*Required*: Yes
*Type*: String
*Pattern*: `^\{%[\s\S]+?%\}(?![\s\S])`
*Minimum*: `1`
*Maximum*: `8192`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
