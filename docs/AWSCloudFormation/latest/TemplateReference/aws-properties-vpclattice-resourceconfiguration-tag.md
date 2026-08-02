---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-vpclattice-resourceconfiguration-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::ResourceConfiguration Tag
<a name="aws-properties-vpclattice-resourceconfiguration-tag"></a>

The tags for the resource configuration.

## Syntax
<a name="aws-properties-vpclattice-resourceconfiguration-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-vpclattice-resourceconfiguration-tag-syntax.json"></a>

```
{
  "[Key](#cfn-vpclattice-resourceconfiguration-tag-key)" : {{String}},
  "[Value](#cfn-vpclattice-resourceconfiguration-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-vpclattice-resourceconfiguration-tag-syntax.yaml"></a>

```
  [Key](#cfn-vpclattice-resourceconfiguration-tag-key): {{String}}
  [Value](#cfn-vpclattice-resourceconfiguration-tag-value): {{String}}
```

## Properties
<a name="aws-properties-vpclattice-resourceconfiguration-tag-properties"></a>

`Key`  <a name="cfn-vpclattice-resourceconfiguration-tag-key"></a>
The tag key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-vpclattice-resourceconfiguration-tag-value"></a>
The tag value.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
