---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-vpclattice-targetgroup-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::TargetGroup Tag
<a name="aws-properties-vpclattice-targetgroup-tag"></a>

Specifies a tag for a target group.

## Syntax
<a name="aws-properties-vpclattice-targetgroup-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-vpclattice-targetgroup-tag-syntax.json"></a>

```
{
  "[Key](#cfn-vpclattice-targetgroup-tag-key)" : {{String}},
  "[Value](#cfn-vpclattice-targetgroup-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-vpclattice-targetgroup-tag-syntax.yaml"></a>

```
  [Key](#cfn-vpclattice-targetgroup-tag-key): {{String}}
  [Value](#cfn-vpclattice-targetgroup-tag-value): {{String}}
```

## Properties
<a name="aws-properties-vpclattice-targetgroup-tag-properties"></a>

`Key`  <a name="cfn-vpclattice-targetgroup-tag-key"></a>
The tag key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-vpclattice-targetgroup-tag-value"></a>
The tag value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
