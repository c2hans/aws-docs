---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-processingjob-datasetdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ProcessingJob DatasetDefinition
<a name="aws-properties-sagemaker-processingjob-datasetdefinition"></a>

Configuration for Dataset Definition inputs. The Dataset Definition input must specify exactly one of either `AthenaDatasetDefinition` or `RedshiftDatasetDefinition` types.

## Syntax
<a name="aws-properties-sagemaker-processingjob-datasetdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-processingjob-datasetdefinition-syntax.json"></a>

```
{
  "[AthenaDatasetDefinition](#cfn-sagemaker-processingjob-datasetdefinition-athenadatasetdefinition)" : {{AthenaDatasetDefinition}},
  "[DataDistributionType](#cfn-sagemaker-processingjob-datasetdefinition-datadistributiontype)" : {{String}},
  "[InputMode](#cfn-sagemaker-processingjob-datasetdefinition-inputmode)" : {{String}},
  "[LocalPath](#cfn-sagemaker-processingjob-datasetdefinition-localpath)" : {{String}},
  "[RedshiftDatasetDefinition](#cfn-sagemaker-processingjob-datasetdefinition-redshiftdatasetdefinition)" : {{RedshiftDatasetDefinition}}
}
```

### YAML
<a name="aws-properties-sagemaker-processingjob-datasetdefinition-syntax.yaml"></a>

```
  [AthenaDatasetDefinition](#cfn-sagemaker-processingjob-datasetdefinition-athenadatasetdefinition): {{
    AthenaDatasetDefinition}}
  [DataDistributionType](#cfn-sagemaker-processingjob-datasetdefinition-datadistributiontype): {{String}}
  [InputMode](#cfn-sagemaker-processingjob-datasetdefinition-inputmode): {{String}}
  [LocalPath](#cfn-sagemaker-processingjob-datasetdefinition-localpath): {{String}}
  [RedshiftDatasetDefinition](#cfn-sagemaker-processingjob-datasetdefinition-redshiftdatasetdefinition): {{
    RedshiftDatasetDefinition}}
```

## Properties
<a name="aws-properties-sagemaker-processingjob-datasetdefinition-properties"></a>

`AthenaDatasetDefinition`  <a name="cfn-sagemaker-processingjob-datasetdefinition-athenadatasetdefinition"></a>
Configuration for Athena Dataset Definition input.
*Required*: No
*Type*: [AthenaDatasetDefinition](aws-properties-sagemaker-processingjob-athenadatasetdefinition.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataDistributionType`  <a name="cfn-sagemaker-processingjob-datasetdefinition-datadistributiontype"></a>
Whether the generated dataset is `FullyReplicated` or `ShardedByS3Key` (default).
*Required*: No
*Type*: String
*Allowed values*: `FullyReplicated | ShardedByS3Key`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InputMode`  <a name="cfn-sagemaker-processingjob-datasetdefinition-inputmode"></a>
Whether to use `File` or `Pipe` input mode. In `File` (default) mode, Amazon SageMaker copies the data from the input source onto the local Amazon Elastic Block Store (Amazon EBS) volumes before starting your training algorithm. This is the most commonly used input mode. In `Pipe` mode, Amazon SageMaker streams input data from the source directly to your algorithm without using the EBS volume.
*Required*: No
*Type*: String
*Allowed values*: `File | Pipe`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LocalPath`  <a name="cfn-sagemaker-processingjob-datasetdefinition-localpath"></a>
The local path where you want Amazon SageMaker to download the Dataset Definition inputs to run a processing job. `LocalPath` is an absolute path to the input data. This is a required parameter when `AppManaged` is `False` (default).
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RedshiftDatasetDefinition`  <a name="cfn-sagemaker-processingjob-datasetdefinition-redshiftdatasetdefinition"></a>
Configuration for Redshift Dataset Definition input.
*Required*: No
*Type*: [RedshiftDatasetDefinition](aws-properties-sagemaker-processingjob-redshiftdatasetdefinition.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
