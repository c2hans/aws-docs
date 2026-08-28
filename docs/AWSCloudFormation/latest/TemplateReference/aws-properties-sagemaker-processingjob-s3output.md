---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-processingjob-s3output.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ProcessingJob S3Output
<a name="aws-properties-sagemaker-processingjob-s3output"></a>

Configuration for uploading output data to Amazon S3 from the processing container.

## Syntax
<a name="aws-properties-sagemaker-processingjob-s3output-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-processingjob-s3output-syntax.json"></a>

```
{
  "[LocalPath](#cfn-sagemaker-processingjob-s3output-localpath)" : {{String}},
  "[S3UploadMode](#cfn-sagemaker-processingjob-s3output-s3uploadmode)" : {{String}},
  "[S3Uri](#cfn-sagemaker-processingjob-s3output-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-processingjob-s3output-syntax.yaml"></a>

```
  [LocalPath](#cfn-sagemaker-processingjob-s3output-localpath): {{String}}
  [S3UploadMode](#cfn-sagemaker-processingjob-s3output-s3uploadmode): {{String}}
  [S3Uri](#cfn-sagemaker-processingjob-s3output-s3uri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-processingjob-s3output-properties"></a>

`LocalPath`  <a name="cfn-sagemaker-processingjob-s3output-localpath"></a>
The local path of a directory where you want Amazon SageMaker to upload its contents to Amazon S3. `LocalPath` is an absolute path to a directory containing output files. This directory will be created by the platform and exist when your container's entrypoint is invoked.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3UploadMode`  <a name="cfn-sagemaker-processingjob-s3output-s3uploadmode"></a>
Whether to upload the results of the processing job continuously or after the job completes.
*Required*: Yes
*Type*: String
*Allowed values*: `Continuous | EndOfJob`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Uri`  <a name="cfn-sagemaker-processingjob-s3output-s3uri"></a>
The URI of the Amazon S3 prefix Amazon SageMaker downloads data required to run a processing job.
*Required*: Yes
*Type*: String
*Pattern*: `(https|s3)://([^/]+)/?(.*)`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
