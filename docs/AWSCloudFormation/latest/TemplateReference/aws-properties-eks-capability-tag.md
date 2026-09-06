---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-capability-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Capability Tag
<a name="aws-properties-eks-capability-tag"></a>

<a name="aws-properties-eks-capability-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::EKS::Capability](aws-resource-eks-capability.md).

## Syntax
<a name="aws-properties-eks-capability-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-capability-tag-syntax.json"></a>

```
{
  "[Key](#cfn-eks-capability-tag-key)" : {{String}},
  "[Value](#cfn-eks-capability-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-capability-tag-syntax.yaml"></a>

```
  [Key](#cfn-eks-capability-tag-key): {{String}}
  [Value](#cfn-eks-capability-tag-value): {{String}}
```

## Properties
<a name="aws-properties-eks-capability-tag-properties"></a>

`Key`  <a name="cfn-eks-capability-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-eks-capability-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
