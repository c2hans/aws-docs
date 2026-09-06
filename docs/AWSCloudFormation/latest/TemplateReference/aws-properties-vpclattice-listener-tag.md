---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-vpclattice-listener-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::Listener Tag
<a name="aws-properties-vpclattice-listener-tag"></a>

Specifies a tag for a listener.

## Syntax
<a name="aws-properties-vpclattice-listener-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-vpclattice-listener-tag-syntax.json"></a>

```
{
  "[Key](#cfn-vpclattice-listener-tag-key)" : {{String}},
  "[Value](#cfn-vpclattice-listener-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-vpclattice-listener-tag-syntax.yaml"></a>

```
  [Key](#cfn-vpclattice-listener-tag-key): {{String}}
  [Value](#cfn-vpclattice-listener-tag-value): {{String}}
```

## Properties
<a name="aws-properties-vpclattice-listener-tag-properties"></a>

`Key`  <a name="cfn-vpclattice-listener-tag-key"></a>
The tag key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-vpclattice-listener-tag-value"></a>
The tag value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
