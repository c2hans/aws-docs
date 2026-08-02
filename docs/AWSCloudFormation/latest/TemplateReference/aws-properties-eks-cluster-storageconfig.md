---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-storageconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster StorageConfig
<a name="aws-properties-eks-cluster-storageconfig"></a>

Request to update the configuration of the storage capability of your EKS Auto Mode cluster. For example, enable the capability. For more information, see EKS Auto Mode block storage capability in the *Amazon EKS User Guide*.

## Syntax
<a name="aws-properties-eks-cluster-storageconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-storageconfig-syntax.json"></a>

```
{
  "[BlockStorage](#cfn-eks-cluster-storageconfig-blockstorage)" : {{BlockStorage}}
}
```

### YAML
<a name="aws-properties-eks-cluster-storageconfig-syntax.yaml"></a>

```
  [BlockStorage](#cfn-eks-cluster-storageconfig-blockstorage): {{
    BlockStorage}}
```

## Properties
<a name="aws-properties-eks-cluster-storageconfig-properties"></a>

`BlockStorage`  <a name="cfn-eks-cluster-storageconfig-blockstorage"></a>
Request to configure EBS Block Storage settings for your EKS Auto Mode cluster.
*Required*: No
*Type*: [BlockStorage](aws-properties-eks-cluster-blockstorage.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
