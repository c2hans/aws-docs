---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-controlplanescalingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster ControlPlaneScalingConfig
<a name="aws-properties-eks-cluster-controlplanescalingconfig"></a>

The control plane scaling tier configuration. For more information, see EKS Provisioned Control Plane in the Amazon EKS User Guide.

## Syntax
<a name="aws-properties-eks-cluster-controlplanescalingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-controlplanescalingconfig-syntax.json"></a>

```
{
  "[Tier](#cfn-eks-cluster-controlplanescalingconfig-tier)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-cluster-controlplanescalingconfig-syntax.yaml"></a>

```
  [Tier](#cfn-eks-cluster-controlplanescalingconfig-tier): {{String}}
```

## Properties
<a name="aws-properties-eks-cluster-controlplanescalingconfig-properties"></a>

`Tier`  <a name="cfn-eks-cluster-controlplanescalingconfig-tier"></a>
The control plane scaling tier configuration. Available options are `standard`, `tier-xl`, `tier-2xl`, `tier-4xl, or tier-8xl`. For more information, see EKS Provisioned Control Plane in the Amazon EKS User Guide.
*Required*: No
*Type*: String
*Allowed values*: `standard | tier-xl | tier-2xl | tier-4xl | tier-8xl | tier-ultra`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
