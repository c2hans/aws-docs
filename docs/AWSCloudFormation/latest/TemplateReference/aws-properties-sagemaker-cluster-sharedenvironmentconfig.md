---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-sharedenvironmentconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster SharedEnvironmentConfig
<a name="aws-properties-sagemaker-cluster-sharedenvironmentconfig"></a>

<a name="aws-properties-sagemaker-cluster-sharedenvironmentconfig-description"></a>The `SharedEnvironmentConfig` property type specifies Property description not available. for an [AWS::SageMaker::Cluster](aws-resource-sagemaker-cluster.md).

## Syntax
<a name="aws-properties-sagemaker-cluster-sharedenvironmentconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-sharedenvironmentconfig-syntax.json"></a>

```
{
  "[FSxLustreConfig](#cfn-sagemaker-cluster-sharedenvironmentconfig-fsxlustreconfig)" : {{FSxLustreConfig}},
  "[FSxLustreDeletionPolicy](#cfn-sagemaker-cluster-sharedenvironmentconfig-fsxlustredeletionpolicy)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-sharedenvironmentconfig-syntax.yaml"></a>

```
  [FSxLustreConfig](#cfn-sagemaker-cluster-sharedenvironmentconfig-fsxlustreconfig): {{
    FSxLustreConfig}}
  [FSxLustreDeletionPolicy](#cfn-sagemaker-cluster-sharedenvironmentconfig-fsxlustredeletionpolicy): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-sharedenvironmentconfig-properties"></a>

`FSxLustreConfig`  <a name="cfn-sagemaker-cluster-sharedenvironmentconfig-fsxlustreconfig"></a>
Property description not available.
*Required*: No
*Type*: [FSxLustreConfig](aws-properties-sagemaker-cluster-fsxlustreconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FSxLustreDeletionPolicy`  <a name="cfn-sagemaker-cluster-sharedenvironmentconfig-fsxlustredeletionpolicy"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `Keep | DeleteIfNotUsed`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
