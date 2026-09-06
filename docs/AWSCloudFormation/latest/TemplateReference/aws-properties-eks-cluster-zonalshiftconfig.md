---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-zonalshiftconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster ZonalShiftConfig
<a name="aws-properties-eks-cluster-zonalshiftconfig"></a>

The configuration for zonal shift for the cluster.

## Syntax
<a name="aws-properties-eks-cluster-zonalshiftconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-zonalshiftconfig-syntax.json"></a>

```
{
  "[Enabled](#cfn-eks-cluster-zonalshiftconfig-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-eks-cluster-zonalshiftconfig-syntax.yaml"></a>

```
  [Enabled](#cfn-eks-cluster-zonalshiftconfig-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-eks-cluster-zonalshiftconfig-properties"></a>

`Enabled`  <a name="cfn-eks-cluster-zonalshiftconfig-enabled"></a>
If zonal shift is enabled, AWS configures zonal autoshift for the cluster.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
