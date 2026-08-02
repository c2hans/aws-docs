---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-clusterfsxlustreconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster ClusterFsxLustreConfig
<a name="aws-properties-sagemaker-cluster-clusterfsxlustreconfig"></a>

Defines the configuration for attaching an Amazon FSx for Lustre file system to instances in a SageMaker HyperPod cluster instance group.

## Syntax
<a name="aws-properties-sagemaker-cluster-clusterfsxlustreconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-clusterfsxlustreconfig-syntax.json"></a>

```
{
  "[DnsName](#cfn-sagemaker-cluster-clusterfsxlustreconfig-dnsname)" : {{String}},
  "[MountName](#cfn-sagemaker-cluster-clusterfsxlustreconfig-mountname)" : {{String}},
  "[MountPath](#cfn-sagemaker-cluster-clusterfsxlustreconfig-mountpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-clusterfsxlustreconfig-syntax.yaml"></a>

```
  [DnsName](#cfn-sagemaker-cluster-clusterfsxlustreconfig-dnsname): {{String}}
  [MountName](#cfn-sagemaker-cluster-clusterfsxlustreconfig-mountname): {{String}}
  [MountPath](#cfn-sagemaker-cluster-clusterfsxlustreconfig-mountpath): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-clusterfsxlustreconfig-properties"></a>

`DnsName`  <a name="cfn-sagemaker-cluster-clusterfsxlustreconfig-dnsname"></a>
The DNS name of the Amazon FSx for Lustre file system.
*Required*: Yes
*Type*: String
*Pattern*: `^((fs|fc)i?-[0-9a-f]{8,}\..{4,253})$`
*Minimum*: `16`
*Maximum*: `275`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MountName`  <a name="cfn-sagemaker-cluster-clusterfsxlustreconfig-mountname"></a>
The mount name of the Amazon FSx for Lustre file system.
*Required*: Yes
*Type*: String
*Pattern*: `^([A-Za-z0-9_-]{1,8})$`
*Minimum*: `1`
*Maximum*: `8`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MountPath`  <a name="cfn-sagemaker-cluster-clusterfsxlustreconfig-mountpath"></a>
The local path where the Amazon FSx for Lustre file system is mounted on instances.
*Required*: No
*Type*: String
*Pattern*: `^/(?!/)(?!.*/$)[a-zA-Z0-9._-]+(/[a-zA-Z0-9._-]+)*$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
