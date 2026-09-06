---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-resourceweight.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster ResourceWeight
<a name="aws-properties-eks-cluster-resourceweight"></a>

A resource weight entry for the scheduler scoring strategy.

## Syntax
<a name="aws-properties-eks-cluster-resourceweight-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-resourceweight-syntax.json"></a>

```
{
  "[Name](#cfn-eks-cluster-resourceweight-name)" : {{String}},
  "[Weight](#cfn-eks-cluster-resourceweight-weight)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-eks-cluster-resourceweight-syntax.yaml"></a>

```
  [Name](#cfn-eks-cluster-resourceweight-name): {{String}}
  [Weight](#cfn-eks-cluster-resourceweight-weight): {{Integer}}
```

## Properties
<a name="aws-properties-eks-cluster-resourceweight-properties"></a>

`Name`  <a name="cfn-eks-cluster-resourceweight-name"></a>
The name of the resource (for example, `cpu` or `memory`).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weight`  <a name="cfn-eks-cluster-resourceweight-weight"></a>
The weight assigned to the resource for scoring. Must be between 1 and 100.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
