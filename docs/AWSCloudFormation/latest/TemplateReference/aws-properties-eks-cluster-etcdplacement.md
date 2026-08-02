---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-etcdplacement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster EtcdPlacement
<a name="aws-properties-eks-cluster-etcdplacement"></a>

The placement configuration for the etcd instances of your local Amazon EKS cluster on an AWS Outpost. For more information, see [Capacity considerations](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html) in the *Amazon EKS User Guide*.

## Syntax
<a name="aws-properties-eks-cluster-etcdplacement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-etcdplacement-syntax.json"></a>

```
{
  "[SpreadLevel](#cfn-eks-cluster-etcdplacement-spreadlevel)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-cluster-etcdplacement-syntax.yaml"></a>

```
  [SpreadLevel](#cfn-eks-cluster-etcdplacement-spreadlevel): {{String}}
```

## Properties
<a name="aws-properties-eks-cluster-etcdplacement-properties"></a>

`SpreadLevel`  <a name="cfn-eks-cluster-etcdplacement-spreadlevel"></a>
Optional parameter to specify the placement group spread level for etcd instances. If not provided, Amazon EKS will deploy etcd instances without a placement group.
*Required*: No
*Type*: String
*Allowed values*: `host | rack`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
