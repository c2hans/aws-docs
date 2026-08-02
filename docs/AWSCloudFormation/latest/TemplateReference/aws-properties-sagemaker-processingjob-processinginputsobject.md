---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-processingjob-processinginputsobject.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ProcessingJob ProcessingInputsObject
<a name="aws-properties-sagemaker-processingjob-processinginputsobject"></a>

The inputs for a processing job. The processing input must specify exactly one of either `S3Input` or `DatasetDefinition` types.

## Syntax
<a name="aws-properties-sagemaker-processingjob-processinginputsobject-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-processingjob-processinginputsobject-syntax.json"></a>

```
{
  "[AppManaged](#cfn-sagemaker-processingjob-processinginputsobject-appmanaged)" : {{Boolean}},
  "[DatasetDefinition](#cfn-sagemaker-processingjob-processinginputsobject-datasetdefinition)" : {{DatasetDefinition}},
  "[InputName](#cfn-sagemaker-processingjob-processinginputsobject-inputname)" : {{String}},
  "[S3Input](#cfn-sagemaker-processingjob-processinginputsobject-s3input)" : {{S3Input}}
}
```

### YAML
<a name="aws-properties-sagemaker-processingjob-processinginputsobject-syntax.yaml"></a>

```
  [AppManaged](#cfn-sagemaker-processingjob-processinginputsobject-appmanaged): {{Boolean}}
  [DatasetDefinition](#cfn-sagemaker-processingjob-processinginputsobject-datasetdefinition): {{
    DatasetDefinition}}
  [InputName](#cfn-sagemaker-processingjob-processinginputsobject-inputname): {{String}}
  [S3Input](#cfn-sagemaker-processingjob-processinginputsobject-s3input): {{
    S3Input}}
```

## Properties
<a name="aws-properties-sagemaker-processingjob-processinginputsobject-properties"></a>

`AppManaged`  <a name="cfn-sagemaker-processingjob-processinginputsobject-appmanaged"></a>
When `True`, input operations such as data download are managed natively by the processing job application. When `False` (default), input operations are managed by Amazon SageMaker.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatasetDefinition`  <a name="cfn-sagemaker-processingjob-processinginputsobject-datasetdefinition"></a>
Configuration for Dataset Definition inputs. The Dataset Definition input must specify exactly one of either `AthenaDatasetDefinition` or `RedshiftDatasetDefinition` types.
*Required*: No
*Type*: [DatasetDefinition](aws-properties-sagemaker-processingjob-datasetdefinition.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InputName`  <a name="cfn-sagemaker-processingjob-processinginputsobject-inputname"></a>
The name for the processing job input.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Input`  <a name="cfn-sagemaker-processingjob-processinginputsobject-s3input"></a>
Configuration for downloading input data from Amazon S3 into the processing container.
*Required*: No
*Type*: [S3Input](aws-properties-sagemaker-processingjob-s3input.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
