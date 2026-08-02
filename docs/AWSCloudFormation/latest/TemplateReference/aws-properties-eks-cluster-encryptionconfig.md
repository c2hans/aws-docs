---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-encryptionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster EncryptionConfig
<a name="aws-properties-eks-cluster-encryptionconfig"></a>

The encryption configuration for the cluster.

## Syntax
<a name="aws-properties-eks-cluster-encryptionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-encryptionconfig-syntax.json"></a>

```
{
  "[Provider](#cfn-eks-cluster-encryptionconfig-provider)" : {{Provider}},
  "[Resources](#cfn-eks-cluster-encryptionconfig-resources)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-eks-cluster-encryptionconfig-syntax.yaml"></a>

```
  [Provider](#cfn-eks-cluster-encryptionconfig-provider): {{
    Provider}}
  [Resources](#cfn-eks-cluster-encryptionconfig-resources): {{
    - String}}
```

## Properties
<a name="aws-properties-eks-cluster-encryptionconfig-properties"></a>

`Provider`  <a name="cfn-eks-cluster-encryptionconfig-provider"></a>
The encryption provider for the cluster.
*Required*: No
*Type*: [Provider](aws-properties-eks-cluster-provider.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Resources`  <a name="cfn-eks-cluster-encryptionconfig-resources"></a>
Specifies the resources to be encrypted. The only supported value is `secrets`.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
