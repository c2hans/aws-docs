---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-clusterfsxopenzfsconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster ClusterFsxOpenZfsConfig
<a name="aws-properties-sagemaker-cluster-clusterfsxopenzfsconfig"></a>

Defines the configuration for attaching an Amazon FSx for OpenZFS file system to instances in a SageMaker HyperPod cluster instance group.

## Syntax
<a name="aws-properties-sagemaker-cluster-clusterfsxopenzfsconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-clusterfsxopenzfsconfig-syntax.json"></a>

```
{
  "[DnsName](#cfn-sagemaker-cluster-clusterfsxopenzfsconfig-dnsname)" : {{String}},
  "[MountPath](#cfn-sagemaker-cluster-clusterfsxopenzfsconfig-mountpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-clusterfsxopenzfsconfig-syntax.yaml"></a>

```
  [DnsName](#cfn-sagemaker-cluster-clusterfsxopenzfsconfig-dnsname): {{String}}
  [MountPath](#cfn-sagemaker-cluster-clusterfsxopenzfsconfig-mountpath): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-clusterfsxopenzfsconfig-properties"></a>

`DnsName`  <a name="cfn-sagemaker-cluster-clusterfsxopenzfsconfig-dnsname"></a>
The DNS name of the Amazon FSx for OpenZFS file system.
*Required*: Yes
*Type*: String
*Pattern*: `^((fs|fc)i?-[0-9a-f]{8,}\..{4,253})$`
*Minimum*: `16`
*Maximum*: `275`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MountPath`  <a name="cfn-sagemaker-cluster-clusterfsxopenzfsconfig-mountpath"></a>
The local path where the Amazon FSx for OpenZFS file system is mounted on instances.
*Required*: No
*Type*: String
*Pattern*: `^/(?!/)(?!.*/$)[a-zA-Z0-9._-]+(/[a-zA-Z0-9._-]+)*$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
