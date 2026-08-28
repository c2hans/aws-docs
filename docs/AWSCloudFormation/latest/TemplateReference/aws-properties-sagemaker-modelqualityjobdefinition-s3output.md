---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelqualityjobdefinition-s3output.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelQualityJobDefinition S3Output
<a name="aws-properties-sagemaker-modelqualityjobdefinition-s3output"></a>

The Amazon S3 storage location where the results of a monitoring job are saved.

## Syntax
<a name="aws-properties-sagemaker-modelqualityjobdefinition-s3output-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelqualityjobdefinition-s3output-syntax.json"></a>

```
{
  "[LocalPath](#cfn-sagemaker-modelqualityjobdefinition-s3output-localpath)" : {{String}},
  "[S3UploadMode](#cfn-sagemaker-modelqualityjobdefinition-s3output-s3uploadmode)" : {{String}},
  "[S3Uri](#cfn-sagemaker-modelqualityjobdefinition-s3output-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelqualityjobdefinition-s3output-syntax.yaml"></a>

```
  [LocalPath](#cfn-sagemaker-modelqualityjobdefinition-s3output-localpath): {{String}}
  [S3UploadMode](#cfn-sagemaker-modelqualityjobdefinition-s3output-s3uploadmode): {{String}}
  [S3Uri](#cfn-sagemaker-modelqualityjobdefinition-s3output-s3uri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelqualityjobdefinition-s3output-properties"></a>

`LocalPath`  <a name="cfn-sagemaker-modelqualityjobdefinition-s3output-localpath"></a>
The local path to the Amazon S3 storage location where Amazon SageMaker saves the results of a monitoring job. LocalPath is an absolute path for the output data.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3UploadMode`  <a name="cfn-sagemaker-modelqualityjobdefinition-s3output-s3uploadmode"></a>
Whether to upload the results of the monitoring job continuously or after the job completes.
*Required*: No
*Type*: String
*Allowed values*: `Continuous | EndOfJob`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Uri`  <a name="cfn-sagemaker-modelqualityjobdefinition-s3output-s3uri"></a>
A URI that identifies the Amazon S3 storage location where Amazon SageMaker saves the results of a monitoring job.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
