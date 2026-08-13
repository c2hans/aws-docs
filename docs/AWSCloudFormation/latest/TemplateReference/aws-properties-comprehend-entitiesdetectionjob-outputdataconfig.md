---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-comprehend-entitiesdetectionjob-outputdataconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Comprehend::EntitiesDetectionJob OutputDataConfig
<a name="aws-properties-comprehend-entitiesdetectionjob-outputdataconfig"></a>

Provides configuration parameters for the output of inference jobs.

## Syntax
<a name="aws-properties-comprehend-entitiesdetectionjob-outputdataconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-comprehend-entitiesdetectionjob-outputdataconfig-syntax.json"></a>

```
{
  "[S3Uri](#cfn-comprehend-entitiesdetectionjob-outputdataconfig-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-comprehend-entitiesdetectionjob-outputdataconfig-syntax.yaml"></a>

```
  [S3Uri](#cfn-comprehend-entitiesdetectionjob-outputdataconfig-s3uri): {{String}}
```

## Properties
<a name="aws-properties-comprehend-entitiesdetectionjob-outputdataconfig-properties"></a>

`S3Uri`  <a name="cfn-comprehend-entitiesdetectionjob-outputdataconfig-s3uri"></a>
When you use the `OutputDataConfig` object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same Region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output file.
When the topic detection job is finished, the service creates an output file in a directory specific to the job. The `S3Uri` field contains the location of the output file, called `output.tar.gz`. It is a compressed archive that contains the ouput of the operation.
 For a PII entity detection job, the output file is plain text, not a compressed archive. The output file name is the same as the input file, with `.out` appended at the end.
*Required*: Yes
*Type*: String
*Pattern*: `^s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
