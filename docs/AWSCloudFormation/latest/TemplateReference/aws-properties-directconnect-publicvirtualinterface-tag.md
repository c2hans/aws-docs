---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-directconnect-publicvirtualinterface-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DirectConnect::PublicVirtualInterface Tag
<a name="aws-properties-directconnect-publicvirtualinterface-tag"></a>

Information about a tag.

## Syntax
<a name="aws-properties-directconnect-publicvirtualinterface-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-directconnect-publicvirtualinterface-tag-syntax.json"></a>

```
{
  "[Key](#cfn-directconnect-publicvirtualinterface-tag-key)" : {{String}},
  "[Value](#cfn-directconnect-publicvirtualinterface-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-directconnect-publicvirtualinterface-tag-syntax.yaml"></a>

```
  [Key](#cfn-directconnect-publicvirtualinterface-tag-key): {{String}}
  [Value](#cfn-directconnect-publicvirtualinterface-tag-value): {{String}}
```

## Properties
<a name="aws-properties-directconnect-publicvirtualinterface-tag-properties"></a>

`Key`  <a name="cfn-directconnect-publicvirtualinterface-tag-key"></a>
The key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-directconnect-publicvirtualinterface-tag-value"></a>
The value.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
