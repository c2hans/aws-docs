---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-storageinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster StorageInfo
<a name="aws-properties-msk-cluster-storageinfo"></a>

Contains information about storage volumes attached to Amazon MSK broker nodes.

## Syntax
<a name="aws-properties-msk-cluster-storageinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-storageinfo-syntax.json"></a>

```
{
  "[EBSStorageInfo](#cfn-msk-cluster-storageinfo-ebsstorageinfo)" : {{EBSStorageInfo}}
}
```

### YAML
<a name="aws-properties-msk-cluster-storageinfo-syntax.yaml"></a>

```
  [EBSStorageInfo](#cfn-msk-cluster-storageinfo-ebsstorageinfo): {{
    EBSStorageInfo}}
```

## Properties
<a name="aws-properties-msk-cluster-storageinfo-properties"></a>

`EBSStorageInfo`  <a name="cfn-msk-cluster-storageinfo-ebsstorageinfo"></a>
EBS volume information.
*Required*: No
*Type*: [EBSStorageInfo](aws-properties-msk-cluster-ebsstorageinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
