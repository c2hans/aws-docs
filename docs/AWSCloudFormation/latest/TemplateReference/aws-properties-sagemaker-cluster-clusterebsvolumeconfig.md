---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-clusterebsvolumeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster ClusterEbsVolumeConfig
<a name="aws-properties-sagemaker-cluster-clusterebsvolumeconfig"></a>

Defines the configuration for attaching an additional Amazon Elastic Block Store (EBS) volume to each instance of the SageMaker HyperPod cluster instance group. To learn more, see [SageMaker HyperPod release notes: June 20, 2024](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-release-notes.html#sagemaker-hyperpod-release-notes-20240620).

## Syntax
<a name="aws-properties-sagemaker-cluster-clusterebsvolumeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-clusterebsvolumeconfig-syntax.json"></a>

```
{
  "[RootVolume](#cfn-sagemaker-cluster-clusterebsvolumeconfig-rootvolume)" : {{Boolean}},
  "[VolumeKmsKeyId](#cfn-sagemaker-cluster-clusterebsvolumeconfig-volumekmskeyid)" : {{String}},
  "[VolumeSizeInGB](#cfn-sagemaker-cluster-clusterebsvolumeconfig-volumesizeingb)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-clusterebsvolumeconfig-syntax.yaml"></a>

```
  [RootVolume](#cfn-sagemaker-cluster-clusterebsvolumeconfig-rootvolume): {{Boolean}}
  [VolumeKmsKeyId](#cfn-sagemaker-cluster-clusterebsvolumeconfig-volumekmskeyid): {{String}}
  [VolumeSizeInGB](#cfn-sagemaker-cluster-clusterebsvolumeconfig-volumesizeingb): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-clusterebsvolumeconfig-properties"></a>

`RootVolume`  <a name="cfn-sagemaker-cluster-clusterebsvolumeconfig-rootvolume"></a>
Specifies whether the configuration is for the cluster's root or secondary Amazon EBS volume. You can specify two `ClusterEbsVolumeConfig` fields to configure both the root and secondary volumes. Set the value to `True` if you'd like to provide your own customer managed AWS KMS key to encrypt the root volume. When `True`:
+ The configuration is applied to the root volume.
+ You can't specify the `VolumeSizeInGB` field. The size of the root volume is determined for you.
+ You must specify a KMS key ID for `VolumeKmsKeyId` to encrypt the root volume with your own KMS key instead of an AWS owned KMS key.
Otherwise, by default, the value is `False`, and the following applies:
+ The configuration is applied to the secondary volume, while the root volume is encrypted with an AWS owned key.
+ You must specify the `VolumeSizeInGB` field.
+ You can optionally specify the `VolumeKmsKeyId` to encrypt the secondary volume with your own KMS key instead of an AWS owned KMS key.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VolumeKmsKeyId`  <a name="cfn-sagemaker-cluster-clusterebsvolumeconfig-volumekmskeyid"></a>
The ID of a KMS key to encrypt the Amazon EBS volume.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9:/_-]*$`
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VolumeSizeInGB`  <a name="cfn-sagemaker-cluster-clusterebsvolumeconfig-volumesizeingb"></a>
The size in gigabytes (GB) of the additional EBS volume to be attached to the instances in the SageMaker HyperPod cluster instance group. The additional EBS volume is attached to each instance within the SageMaker HyperPod cluster instance group and mounted to `/opt/sagemaker`.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `16384`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
