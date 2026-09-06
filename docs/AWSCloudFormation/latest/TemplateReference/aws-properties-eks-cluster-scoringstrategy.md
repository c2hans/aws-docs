---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-scoringstrategy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster ScoringStrategy
<a name="aws-properties-eks-cluster-scoringstrategy"></a>

The scoring strategy configuration for the NodeResourcesFit scheduler plugin.

## Syntax
<a name="aws-properties-eks-cluster-scoringstrategy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-scoringstrategy-syntax.json"></a>

```
{
  "[Resources](#cfn-eks-cluster-scoringstrategy-resources)" : {{[ ResourceWeight, ... ]}},
  "[Type](#cfn-eks-cluster-scoringstrategy-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-cluster-scoringstrategy-syntax.yaml"></a>

```
  [Resources](#cfn-eks-cluster-scoringstrategy-resources): {{
    - ResourceWeight}}
  [Type](#cfn-eks-cluster-scoringstrategy-type): {{String}}
```

## Properties
<a name="aws-properties-eks-cluster-scoringstrategy-properties"></a>

`Resources`  <a name="cfn-eks-cluster-scoringstrategy-resources"></a>
The resource weights used for scoring nodes.
*Required*: No
*Type*: Array of [ResourceWeight](aws-properties-eks-cluster-resourceweight.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-eks-cluster-scoringstrategy-type"></a>
The scoring strategy type. Valid values are `LeastAllocated` or `MostAllocated`.
*Required*: No
*Type*: String
*Allowed values*: `LeastAllocated | MostAllocated`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
