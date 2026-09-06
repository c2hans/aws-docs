---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-controlplaneplacement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster ControlPlanePlacement
<a name="aws-properties-eks-cluster-controlplaneplacement"></a>

The placement configuration for all the control plane instances of your local Amazon EKS cluster on an AWS Outpost. For more information, see [Capacity considerations](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html) in the *Amazon EKS User Guide*.

## Syntax
<a name="aws-properties-eks-cluster-controlplaneplacement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-controlplaneplacement-syntax.json"></a>

```
{
  "[GroupName](#cfn-eks-cluster-controlplaneplacement-groupname)" : {{String}},
  "[SpreadLevel](#cfn-eks-cluster-controlplaneplacement-spreadlevel)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-cluster-controlplaneplacement-syntax.yaml"></a>

```
  [GroupName](#cfn-eks-cluster-controlplaneplacement-groupname): {{String}}
  [SpreadLevel](#cfn-eks-cluster-controlplaneplacement-spreadlevel): {{String}}
```

## Properties
<a name="aws-properties-eks-cluster-controlplaneplacement-properties"></a>

`GroupName`  <a name="cfn-eks-cluster-controlplaneplacement-groupname"></a>
The name of the placement group for the Kubernetes control plane instances. This property is only used for a local cluster on an AWS Outpost.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SpreadLevel`  <a name="cfn-eks-cluster-controlplaneplacement-spreadlevel"></a>
Optional parameter to specify the placement group spread level for control plane instances. If not provided, Amazon EKS will deploy control plane instances without a placement group.
*Required*: No
*Type*: String
*Allowed values*: `host | rack`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
