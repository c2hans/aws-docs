---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-vpclattice-servicenetwork-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::ServiceNetwork Tag
<a name="aws-properties-vpclattice-servicenetwork-tag"></a>

Specifies a tag for a service network.

## Syntax
<a name="aws-properties-vpclattice-servicenetwork-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-vpclattice-servicenetwork-tag-syntax.json"></a>

```
{
  "[Key](#cfn-vpclattice-servicenetwork-tag-key)" : {{String}},
  "[Value](#cfn-vpclattice-servicenetwork-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-vpclattice-servicenetwork-tag-syntax.yaml"></a>

```
  [Key](#cfn-vpclattice-servicenetwork-tag-key): {{String}}
  [Value](#cfn-vpclattice-servicenetwork-tag-value): {{String}}
```

## Properties
<a name="aws-properties-vpclattice-servicenetwork-tag-properties"></a>

`Key`  <a name="cfn-vpclattice-servicenetwork-tag-key"></a>
The tag key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-vpclattice-servicenetwork-tag-value"></a>
The tag value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
