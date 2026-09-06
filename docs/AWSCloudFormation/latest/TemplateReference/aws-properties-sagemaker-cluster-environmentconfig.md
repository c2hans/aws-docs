---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-environmentconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster EnvironmentConfig
<a name="aws-properties-sagemaker-cluster-environmentconfig"></a>

The configuration for the restricted instance groups (RIG) environment.

## Syntax
<a name="aws-properties-sagemaker-cluster-environmentconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-environmentconfig-syntax.json"></a>

```
{
  "[FSxLustreConfig](#cfn-sagemaker-cluster-environmentconfig-fsxlustreconfig)" : {{FSxLustreConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-environmentconfig-syntax.yaml"></a>

```
  [FSxLustreConfig](#cfn-sagemaker-cluster-environmentconfig-fsxlustreconfig): {{
    FSxLustreConfig}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-environmentconfig-properties"></a>

`FSxLustreConfig`  <a name="cfn-sagemaker-cluster-environmentconfig-fsxlustreconfig"></a>
Configuration settings for an Amazon FSx for Lustre file system to be used with the cluster.
*Required*: No
*Type*: [FSxLustreConfig](aws-properties-sagemaker-cluster-fsxlustreconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
