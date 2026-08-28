---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelQualityJobDefinition ClusterConfig
<a name="aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig"></a>

The configuration for the cluster of resources used to run the processing job.

## Syntax
<a name="aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig-syntax.json"></a>

```
{
  "[InstanceCount](#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-instancecount)" : {{Integer}},
  "[InstanceType](#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-instancetype)" : {{String}},
  "[VolumeKmsKeyId](#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-volumekmskeyid)" : {{String}},
  "[VolumeSizeInGB](#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-volumesizeingb)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig-syntax.yaml"></a>

```
  [InstanceCount](#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-instancecount): {{Integer}}
  [InstanceType](#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-instancetype): {{String}}
  [VolumeKmsKeyId](#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-volumekmskeyid): {{String}}
  [VolumeSizeInGB](#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-volumesizeingb): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig-properties"></a>

`InstanceCount`  <a name="cfn-sagemaker-modelqualityjobdefinition-clusterconfig-instancecount"></a>
The number of ML compute instances to use in the model monitoring job. For distributed processing jobs, specify a value greater than 1. The default value is 1.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceType`  <a name="cfn-sagemaker-modelqualityjobdefinition-clusterconfig-instancetype"></a>
The ML compute instance type for the processing job.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VolumeKmsKeyId`  <a name="cfn-sagemaker-modelqualityjobdefinition-clusterconfig-volumekmskeyid"></a>
The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the model monitoring job.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VolumeSizeInGB`  <a name="cfn-sagemaker-modelqualityjobdefinition-clusterconfig-volumesizeingb"></a>
The size of the ML storage volume, in gigabytes, that you want to provision. You must specify sufficient ML storage for your scenario.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `16384`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
