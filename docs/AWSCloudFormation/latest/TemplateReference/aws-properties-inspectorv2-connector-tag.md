---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspectorv2-connector-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::Connector Tag
<a name="aws-properties-inspectorv2-connector-tag"></a>

<a name="aws-properties-inspectorv2-connector-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::InspectorV2::Connector](aws-resource-inspectorv2-connector.md).

## Syntax
<a name="aws-properties-inspectorv2-connector-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspectorv2-connector-tag-syntax.json"></a>

```
{
  "[Key](#cfn-inspectorv2-connector-tag-key)" : {{String}},
  "[Value](#cfn-inspectorv2-connector-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-inspectorv2-connector-tag-syntax.yaml"></a>

```
  [Key](#cfn-inspectorv2-connector-tag-key): {{String}}
  [Value](#cfn-inspectorv2-connector-tag-value): {{String}}
```

## Properties
<a name="aws-properties-inspectorv2-connector-tag-properties"></a>

`Key`  <a name="cfn-inspectorv2-connector-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9 _.:/=+\-@]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-inspectorv2-connector-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9 _.:/=+\-@]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
