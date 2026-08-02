---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelpackage-transformresources.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelPackage TransformResources
<a name="aws-properties-sagemaker-modelpackage-transformresources"></a>

Describes the resources, including ML instance types and ML instance count, to use for transform job.

## Syntax
<a name="aws-properties-sagemaker-modelpackage-transformresources-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelpackage-transformresources-syntax.json"></a>

```
{
  "[InstanceCount](#cfn-sagemaker-modelpackage-transformresources-instancecount)" : {{Integer}},
  "[InstanceType](#cfn-sagemaker-modelpackage-transformresources-instancetype)" : {{String}},
  "[VolumeKmsKeyId](#cfn-sagemaker-modelpackage-transformresources-volumekmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelpackage-transformresources-syntax.yaml"></a>

```
  [InstanceCount](#cfn-sagemaker-modelpackage-transformresources-instancecount): {{Integer}}
  [InstanceType](#cfn-sagemaker-modelpackage-transformresources-instancetype): {{String}}
  [VolumeKmsKeyId](#cfn-sagemaker-modelpackage-transformresources-volumekmskeyid): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelpackage-transformresources-properties"></a>

`InstanceCount`  <a name="cfn-sagemaker-modelpackage-transformresources-instancecount"></a>
The number of ML compute instances to use in the transform job. The default value is `1`, and the maximum is `100`. For distributed transform jobs, specify a value greater than `1`.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceType`  <a name="cfn-sagemaker-modelpackage-transformresources-instancetype"></a>
The ML compute instance type for the transform job. If you are using built-in algorithms to transform moderately sized datasets, we recommend using ml.m4.xlarge or `ml.m5.large`instance types.
*Required*: Yes
*Type*: String
*Allowed values*: `ml.m4.xlarge | ml.m4.2xlarge | ml.m4.4xlarge | ml.m4.10xlarge | ml.m4.16xlarge | ml.c4.xlarge | ml.c4.2xlarge | ml.c4.4xlarge | ml.c4.8xlarge | ml.p2.xlarge | ml.p2.8xlarge | ml.p2.16xlarge | ml.p3.2xlarge | ml.p3.8xlarge | ml.p3.16xlarge | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.18xlarge | ml.m5.large | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.12xlarge | ml.m5.24xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.c6i.large | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.4xlarge | ml.c6i.8xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.r6i.large | ml.r6i.xlarge | ml.r6i.2xlarge | ml.r6i.4xlarge | ml.r6i.8xlarge | ml.r6i.12xlarge | ml.r6i.16xlarge | ml.r6i.24xlarge | ml.r6i.32xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.c7i.large | ml.c7i.xlarge | ml.c7i.2xlarge | ml.c7i.4xlarge | ml.c7i.8xlarge | ml.c7i.12xlarge | ml.c7i.16xlarge | ml.c7i.24xlarge | ml.c7i.48xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.12xlarge | ml.g5.16xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.trn1.2xlarge | ml.trn1.32xlarge | ml.inf2.xlarge | ml.inf2.8xlarge | ml.inf2.24xlarge | ml.inf2.48xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.12xlarge | ml.g6.16xlarge | ml.g6.24xlarge | ml.g6.48xlarge`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VolumeKmsKeyId`  <a name="cfn-sagemaker-modelpackage-transformresources-volumekmskeyid"></a>
The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt model data on the storage volume attached to the ML compute instance(s) that run the batch transform job.
Certain Nitro-based instances include local storage, dependent on the instance type. Local storage volumes are encrypted using a hardware module on the instance. You can't request a `VolumeKmsKeyId` when using an instance type with local storage.
For a list of instance types that support local instance storage, see [Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes).
For more information about local instance storage encryption, see [SSD Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html).
 The `VolumeKmsKeyId` can be any of the following formats:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
+ Alias name: `alias/ExampleAlias`
+ Alias name ARN: `arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias`
*Required*: No
*Type*: String
*Pattern*: `.*`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
