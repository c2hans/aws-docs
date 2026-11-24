---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-mskheader.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber MskHeader

A single Kafka record header. Key and Value each accept a literal or a JSONata expression.

## Syntax
<a name="aws-properties-eventsv2-subscriber-mskheader-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-mskheader-syntax.json"></a>

```json
{
  "[Key](#cfn-eventsv2-subscriber-mskheader-key)" : {{String}},
  "[Value](#cfn-eventsv2-subscriber-mskheader-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-mskheader-syntax.yaml"></a>

```yaml
  [Key](#cfn-eventsv2-subscriber-mskheader-key): {{String}}
  [Value](#cfn-eventsv2-subscriber-mskheader-value): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-mskheader-properties"></a>

`Key`  <a name="cfn-eventsv2-subscriber-mskheader-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Maximum*: `8192`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-eventsv2-subscriber-mskheader-value"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `8192`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
