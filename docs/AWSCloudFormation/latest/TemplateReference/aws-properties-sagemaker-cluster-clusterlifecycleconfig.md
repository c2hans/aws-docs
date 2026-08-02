---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-clusterlifecycleconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster ClusterLifeCycleConfig
<a name="aws-properties-sagemaker-cluster-clusterlifecycleconfig"></a>

The lifecycle configuration for a SageMaker HyperPod cluster.

## Syntax
<a name="aws-properties-sagemaker-cluster-clusterlifecycleconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-clusterlifecycleconfig-syntax.json"></a>

```
{
  "[OnCreate](#cfn-sagemaker-cluster-clusterlifecycleconfig-oncreate)" : {{String}},
  "[OnInitComplete](#cfn-sagemaker-cluster-clusterlifecycleconfig-oninitcomplete)" : {{String}},
  "[SourceS3Uri](#cfn-sagemaker-cluster-clusterlifecycleconfig-sources3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-clusterlifecycleconfig-syntax.yaml"></a>

```
  [OnCreate](#cfn-sagemaker-cluster-clusterlifecycleconfig-oncreate): {{String}}
  [OnInitComplete](#cfn-sagemaker-cluster-clusterlifecycleconfig-oninitcomplete): {{String}}
  [SourceS3Uri](#cfn-sagemaker-cluster-clusterlifecycleconfig-sources3uri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-clusterlifecycleconfig-properties"></a>

`OnCreate`  <a name="cfn-sagemaker-cluster-clusterlifecycleconfig-oncreate"></a>
The file name of the entrypoint script of lifecycle scripts under `SourceS3Uri`. This entrypoint script runs during cluster creation.
*Required*: No
*Type*: String
*Pattern*: `^[\S\s]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnInitComplete`  <a name="cfn-sagemaker-cluster-clusterlifecycleconfig-oninitcomplete"></a>
The file name of the entrypoint script of lifecycle scripts under `SourceS3Uri`. This script runs on the node after the AMI-based initialization is complete.
*Required*: No
*Type*: String
*Pattern*: `^[\S\s]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceS3Uri`  <a name="cfn-sagemaker-cluster-clusterlifecycleconfig-sources3uri"></a>
An Amazon S3 bucket path where your lifecycle scripts are stored.
Make sure that the S3 bucket path starts with `s3://sagemaker-`. The [IAM role for SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod) has the managed [https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-cluster.html](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-cluster.html) attached, which allows access to S3 buckets with the specific prefix `sagemaker-`.
*Required*: No
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
