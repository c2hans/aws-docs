---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-personalize-batchsegmentjob-batchsegmentjobinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::BatchSegmentJob BatchSegmentJobInput
<a name="aws-properties-personalize-batchsegmentjob-batchsegmentjobinput"></a>

The input configuration of a batch segment job.

## Syntax
<a name="aws-properties-personalize-batchsegmentjob-batchsegmentjobinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-personalize-batchsegmentjob-batchsegmentjobinput-syntax.json"></a>

```
{
  "[S3DataSource](#cfn-personalize-batchsegmentjob-batchsegmentjobinput-s3datasource)" : {{S3DataConfig}}
}
```

### YAML
<a name="aws-properties-personalize-batchsegmentjob-batchsegmentjobinput-syntax.yaml"></a>

```
  [S3DataSource](#cfn-personalize-batchsegmentjob-batchsegmentjobinput-s3datasource): {{
    S3DataConfig}}
```

## Properties
<a name="aws-properties-personalize-batchsegmentjob-batchsegmentjobinput-properties"></a>

`S3DataSource`  <a name="cfn-personalize-batchsegmentjob-batchsegmentjobinput-s3datasource"></a>
Property description not available.
*Required*: Yes
*Type*: [S3DataConfig](aws-properties-personalize-batchsegmentjob-s3dataconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
