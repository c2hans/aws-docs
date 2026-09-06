---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-vpclattice-rule-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::Rule Tag
<a name="aws-properties-vpclattice-rule-tag"></a>

Specifies a tag for a listener rule.

## Syntax
<a name="aws-properties-vpclattice-rule-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-vpclattice-rule-tag-syntax.json"></a>

```
{
  "[Key](#cfn-vpclattice-rule-tag-key)" : {{String}},
  "[Value](#cfn-vpclattice-rule-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-vpclattice-rule-tag-syntax.yaml"></a>

```
  [Key](#cfn-vpclattice-rule-tag-key): {{String}}
  [Value](#cfn-vpclattice-rule-tag-value): {{String}}
```

## Properties
<a name="aws-properties-vpclattice-rule-tag-properties"></a>

`Key`  <a name="cfn-vpclattice-rule-tag-key"></a>
The tag key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-vpclattice-rule-tag-value"></a>
The tag value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
