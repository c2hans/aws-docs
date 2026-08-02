---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-outpostconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster OutpostConfig
<a name="aws-properties-eks-cluster-outpostconfig"></a>

The configuration of your local Amazon EKS cluster on an AWS Outpost. Before creating a cluster on an Outpost, review [Creating a local cluster on an Outpost](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-local-cluster-create.html) in the *Amazon EKS User Guide*. This API isn't available for Amazon EKS clusters on the AWS cloud.

## Syntax
<a name="aws-properties-eks-cluster-outpostconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-outpostconfig-syntax.json"></a>

```
{
  "[ControlPlaneInstanceType](#cfn-eks-cluster-outpostconfig-controlplaneinstancetype)" : {{String}},
  "[ControlPlanePlacement](#cfn-eks-cluster-outpostconfig-controlplaneplacement)" : {{ControlPlanePlacement}},
  "[EtcdInstanceType](#cfn-eks-cluster-outpostconfig-etcdinstancetype)" : {{String}},
  "[EtcdPlacement](#cfn-eks-cluster-outpostconfig-etcdplacement)" : {{EtcdPlacement}},
  "[OutpostArns](#cfn-eks-cluster-outpostconfig-outpostarns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-eks-cluster-outpostconfig-syntax.yaml"></a>

```
  [ControlPlaneInstanceType](#cfn-eks-cluster-outpostconfig-controlplaneinstancetype): {{String}}
  [ControlPlanePlacement](#cfn-eks-cluster-outpostconfig-controlplaneplacement): {{
    ControlPlanePlacement}}
  [EtcdInstanceType](#cfn-eks-cluster-outpostconfig-etcdinstancetype): {{String}}
  [EtcdPlacement](#cfn-eks-cluster-outpostconfig-etcdplacement): {{
    EtcdPlacement}}
  [OutpostArns](#cfn-eks-cluster-outpostconfig-outpostarns): {{
    - String}}
```

## Properties
<a name="aws-properties-eks-cluster-outpostconfig-properties"></a>

`ControlPlaneInstanceType`  <a name="cfn-eks-cluster-outpostconfig-controlplaneinstancetype"></a>
The Amazon EC2 instance type for the Kubernetes control plane instances of your local Amazon EKS cluster on AWS Outposts. This instance type applies to all control plane instances and cannot be changed after cluster creation.
For more information, see [Capacity considerations](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html) in the *Amazon EKS User Guide*.

*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ControlPlanePlacement`  <a name="cfn-eks-cluster-outpostconfig-controlplaneplacement"></a>
An object representing the placement configuration for all the control plane instances of your local Amazon EKS cluster on an AWS Outpost. For more information, see [Capacity considerations](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html) in the *Amazon EKS User Guide*.
*Required*: No
*Type*: [ControlPlanePlacement](aws-properties-eks-cluster-controlplaneplacement.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EtcdInstanceType`  <a name="cfn-eks-cluster-outpostconfig-etcdinstancetype"></a>
The Amazon EC2 instance type for etcd instances of your local Amazon EKS cluster on AWS Outposts. This instance type applies to all etcd instances and cannot be changed after cluster creation.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EtcdPlacement`  <a name="cfn-eks-cluster-outpostconfig-etcdplacement"></a>
An object representing the placement configuration for the etcd instances of your local Amazon EKS cluster on an AWS Outpost. For more information, see [Capacity considerations](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html) in the *Amazon EKS User Guide*.
*Required*: No
*Type*: [EtcdPlacement](aws-properties-eks-cluster-etcdplacement.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutpostArns`  <a name="cfn-eks-cluster-outpostconfig-outpostarns"></a>
The ARN of the Outpost that you want to use for your local Amazon EKS cluster on Outposts. Only a single Outpost ARN is supported.
*Required*: Yes
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
