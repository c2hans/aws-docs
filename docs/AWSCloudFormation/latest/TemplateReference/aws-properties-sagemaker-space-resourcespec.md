---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-space-resourcespec.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Space ResourceSpec
<a name="aws-properties-sagemaker-space-resourcespec"></a>

Specifies the ARN's of a SageMaker AI image and SageMaker AI image version, and the instance type that the version runs on.

**Note**
When both `SageMakerImageVersionArn` and `SageMakerImageArn` are passed, `SageMakerImageVersionArn` is used. Any updates to `SageMakerImageArn` will not take effect if `SageMakerImageVersionArn` already exists in the `ResourceSpec` because `SageMakerImageVersionArn` always takes precedence. To clear the value set for `SageMakerImageVersionArn`, pass `None` as the value.

## Syntax
<a name="aws-properties-sagemaker-space-resourcespec-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-space-resourcespec-syntax.json"></a>

```
{
  "[InstanceType](#cfn-sagemaker-space-resourcespec-instancetype)" : {{String}},
  "[LifecycleConfigArn](#cfn-sagemaker-space-resourcespec-lifecycleconfigarn)" : {{String}},
  "[SageMakerImageArn](#cfn-sagemaker-space-resourcespec-sagemakerimagearn)" : {{String}},
  "[SageMakerImageVersionArn](#cfn-sagemaker-space-resourcespec-sagemakerimageversionarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-space-resourcespec-syntax.yaml"></a>

```
  [InstanceType](#cfn-sagemaker-space-resourcespec-instancetype): {{String}}
  [LifecycleConfigArn](#cfn-sagemaker-space-resourcespec-lifecycleconfigarn): {{String}}
  [SageMakerImageArn](#cfn-sagemaker-space-resourcespec-sagemakerimagearn): {{String}}
  [SageMakerImageVersionArn](#cfn-sagemaker-space-resourcespec-sagemakerimageversionarn): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-space-resourcespec-properties"></a>

`InstanceType`  <a name="cfn-sagemaker-space-resourcespec-instancetype"></a>
The instance type that the image version runs on.
**JupyterServer apps** only support the `system` value.
For **KernelGateway apps**, the `system` value is translated to `ml.t3.medium`. KernelGateway apps also support all other values for available instance types.
*Required*: No
*Type*: String
*Allowed values*: `system | ml.t3.micro | ml.t3.small | ml.t3.medium | ml.t3.large | ml.t3.xlarge | ml.t3.2xlarge | ml.m5.large | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.8xlarge | ml.m5.12xlarge | ml.m5.16xlarge | ml.m5.24xlarge | ml.c5.large | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.12xlarge | ml.c5.18xlarge | ml.c5.24xlarge | ml.p3.2xlarge | ml.p3.8xlarge | ml.p3.16xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.r5.large | ml.r5.xlarge | ml.r5.2xlarge | ml.r5.4xlarge | ml.r5.8xlarge | ml.r5.12xlarge | ml.r5.16xlarge | ml.r5.24xlarge | ml.p3dn.24xlarge | ml.m5d.large | ml.m5d.xlarge | ml.m5d.2xlarge | ml.m5d.4xlarge | ml.m5d.8xlarge | ml.m5d.12xlarge | ml.m5d.16xlarge | ml.m5d.24xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.12xlarge | ml.g5.16xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.p4d.24xlarge | ml.p4de.24xlarge | ml.geospatial.interactive | ml.trn1.2xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LifecycleConfigArn`  <a name="cfn-sagemaker-space-resourcespec-lifecycleconfigarn"></a>
 The Amazon Resource Name (ARN) of the Lifecycle Configuration attached to the Resource.
*Required*: No
*Type*: String
*Pattern*: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:studio-lifecycle-config/.*`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SageMakerImageArn`  <a name="cfn-sagemaker-space-resourcespec-sagemakerimagearn"></a>
The ARN of the SageMaker AI image that the image version belongs to.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[\w]+)*:sagemaker:.+:[0-9]{12}:image/[a-z0-9]([-.]?[a-z0-9])*$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SageMakerImageVersionArn`  <a name="cfn-sagemaker-space-resourcespec-sagemakerimageversionarn"></a>
The ARN of the image version created on the instance. To clear the value set for `SageMakerImageVersionArn`, pass `None` as the value.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[\w]+)*:sagemaker:.+:[0-9]{12}:image-version/[a-z0-9]([-.]?[a-z0-9])*/[0-9]+$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
