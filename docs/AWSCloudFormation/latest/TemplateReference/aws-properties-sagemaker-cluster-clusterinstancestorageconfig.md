---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-clusterinstancestorageconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster ClusterInstanceStorageConfig
<a name="aws-properties-sagemaker-cluster-clusterinstancestorageconfig"></a>

Defines the configuration for attaching additional storage to the instances in the SageMaker HyperPod cluster instance group. To learn more, see [SageMaker HyperPod release notes: June 20, 2024](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-release-notes.html#sagemaker-hyperpod-release-notes-20240620).

## Syntax
<a name="aws-properties-sagemaker-cluster-clusterinstancestorageconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-clusterinstancestorageconfig-syntax.json"></a>

```
{
  "[EbsVolumeConfig](#cfn-sagemaker-cluster-clusterinstancestorageconfig-ebsvolumeconfig)" : {{ClusterEbsVolumeConfig}},
  "[FsxLustreConfig](#cfn-sagemaker-cluster-clusterinstancestorageconfig-fsxlustreconfig)" : {{ClusterFsxLustreConfig}},
  "[FsxOpenZfsConfig](#cfn-sagemaker-cluster-clusterinstancestorageconfig-fsxopenzfsconfig)" : {{ClusterFsxOpenZfsConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-clusterinstancestorageconfig-syntax.yaml"></a>

```
  [EbsVolumeConfig](#cfn-sagemaker-cluster-clusterinstancestorageconfig-ebsvolumeconfig): {{
    ClusterEbsVolumeConfig}}
  [FsxLustreConfig](#cfn-sagemaker-cluster-clusterinstancestorageconfig-fsxlustreconfig): {{
    ClusterFsxLustreConfig}}
  [FsxOpenZfsConfig](#cfn-sagemaker-cluster-clusterinstancestorageconfig-fsxopenzfsconfig): {{
    ClusterFsxOpenZfsConfig}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-clusterinstancestorageconfig-properties"></a>

`EbsVolumeConfig`  <a name="cfn-sagemaker-cluster-clusterinstancestorageconfig-ebsvolumeconfig"></a>
Defines the configuration for attaching additional Amazon Elastic Block Store (EBS) volumes to the instances in the SageMaker HyperPod cluster instance group. The additional EBS volume is attached to each instance within the SageMaker HyperPod cluster instance group and mounted to `/opt/sagemaker`.
*Required*: No
*Type*: [ClusterEbsVolumeConfig](aws-properties-sagemaker-cluster-clusterebsvolumeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FsxLustreConfig`  <a name="cfn-sagemaker-cluster-clusterinstancestorageconfig-fsxlustreconfig"></a>
Defines the configuration for attaching an Amazon FSx for Lustre file system to the instances in the SageMaker HyperPod cluster instance group.
*Required*: No
*Type*: [ClusterFsxLustreConfig](aws-properties-sagemaker-cluster-clusterfsxlustreconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FsxOpenZfsConfig`  <a name="cfn-sagemaker-cluster-clusterinstancestorageconfig-fsxopenzfsconfig"></a>
Defines the configuration for attaching an Amazon FSx for OpenZFS file system to the instances in the SageMaker HyperPod cluster instance group.
*Required*: No
*Type*: [ClusterFsxOpenZfsConfig](aws-properties-sagemaker-cluster-clusterfsxopenzfsconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
