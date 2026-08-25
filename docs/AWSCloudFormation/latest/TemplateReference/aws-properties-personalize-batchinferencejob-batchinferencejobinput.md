---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-personalize-batchinferencejob-batchinferencejobinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::BatchInferenceJob BatchInferenceJobInput
<a name="aws-properties-personalize-batchinferencejob-batchinferencejobinput"></a>

The input configuration of a batch inference job.

## Syntax
<a name="aws-properties-personalize-batchinferencejob-batchinferencejobinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-personalize-batchinferencejob-batchinferencejobinput-syntax.json"></a>

```
{
  "[S3DataSource](#cfn-personalize-batchinferencejob-batchinferencejobinput-s3datasource)" : {{S3DataConfig}}
}
```

### YAML
<a name="aws-properties-personalize-batchinferencejob-batchinferencejobinput-syntax.yaml"></a>

```
  [S3DataSource](#cfn-personalize-batchinferencejob-batchinferencejobinput-s3datasource): {{
    S3DataConfig}}
```

## Properties
<a name="aws-properties-personalize-batchinferencejob-batchinferencejobinput-properties"></a>

`S3DataSource`  <a name="cfn-personalize-batchinferencejob-batchinferencejobinput-s3datasource"></a>
The URI of the Amazon S3 location that contains your input data. The Amazon S3 bucket must be in the same region as the API endpoint you are calling.
*Required*: Yes
*Type*: [S3DataConfig](aws-properties-personalize-batchinferencejob-s3dataconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
