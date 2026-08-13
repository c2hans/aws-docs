---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-personalize-batchsegmentjob-batchsegmentjoboutput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::BatchSegmentJob BatchSegmentJobOutput
<a name="aws-properties-personalize-batchsegmentjob-batchsegmentjoboutput"></a>

The output configuration parameters of a batch segment job.

## Syntax
<a name="aws-properties-personalize-batchsegmentjob-batchsegmentjoboutput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-personalize-batchsegmentjob-batchsegmentjoboutput-syntax.json"></a>

```
{
  "[S3DataDestination](#cfn-personalize-batchsegmentjob-batchsegmentjoboutput-s3datadestination)" : {{S3DataConfig}}
}
```

### YAML
<a name="aws-properties-personalize-batchsegmentjob-batchsegmentjoboutput-syntax.yaml"></a>

```
  [S3DataDestination](#cfn-personalize-batchsegmentjob-batchsegmentjoboutput-s3datadestination): {{
    S3DataConfig}}
```

## Properties
<a name="aws-properties-personalize-batchsegmentjob-batchsegmentjoboutput-properties"></a>

`S3DataDestination`  <a name="cfn-personalize-batchsegmentjob-batchsegmentjoboutput-s3datadestination"></a>
Property description not available.
*Required*: Yes
*Type*: [S3DataConfig](aws-properties-personalize-batchsegmentjob-s3dataconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
