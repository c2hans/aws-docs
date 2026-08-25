---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-personalize-batchinferencejob-batchinferencejoboutput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::BatchInferenceJob BatchInferenceJobOutput
<a name="aws-properties-personalize-batchinferencejob-batchinferencejoboutput"></a>

The output configuration parameters of a batch inference job.

## Syntax
<a name="aws-properties-personalize-batchinferencejob-batchinferencejoboutput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-personalize-batchinferencejob-batchinferencejoboutput-syntax.json"></a>

```
{
  "[S3DataDestination](#cfn-personalize-batchinferencejob-batchinferencejoboutput-s3datadestination)" : {{S3DataConfig}}
}
```

### YAML
<a name="aws-properties-personalize-batchinferencejob-batchinferencejoboutput-syntax.yaml"></a>

```
  [S3DataDestination](#cfn-personalize-batchinferencejob-batchinferencejoboutput-s3datadestination): {{
    S3DataConfig}}
```

## Properties
<a name="aws-properties-personalize-batchinferencejob-batchinferencejoboutput-properties"></a>

`S3DataDestination`  <a name="cfn-personalize-batchinferencejob-batchinferencejoboutput-s3datadestination"></a>
Information on the Amazon S3 bucket in which the batch inference job's output is stored.
*Required*: Yes
*Type*: [S3DataConfig](aws-properties-personalize-batchinferencejob-s3dataconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
