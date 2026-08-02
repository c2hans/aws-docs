---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-vpclattice-service-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::Service Tag
<a name="aws-properties-vpclattice-service-tag"></a>

Specifies a tag for a service.

## Syntax
<a name="aws-properties-vpclattice-service-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-vpclattice-service-tag-syntax.json"></a>

```
{
  "[Key](#cfn-vpclattice-service-tag-key)" : {{String}},
  "[Value](#cfn-vpclattice-service-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-vpclattice-service-tag-syntax.yaml"></a>

```
  [Key](#cfn-vpclattice-service-tag-key): {{String}}
  [Value](#cfn-vpclattice-service-tag-value): {{String}}
```

## Properties
<a name="aws-properties-vpclattice-service-tag-properties"></a>

`Key`  <a name="cfn-vpclattice-service-tag-key"></a>
The tag key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-vpclattice-service-tag-value"></a>
The tag value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
