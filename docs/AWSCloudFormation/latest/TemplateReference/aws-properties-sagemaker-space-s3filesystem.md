---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-space-s3filesystem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Space S3FileSystem
<a name="aws-properties-sagemaker-space-s3filesystem"></a>

A custom file system in Amazon S3. This is only supported in Amazon SageMaker Unified Studio.

## Syntax
<a name="aws-properties-sagemaker-space-s3filesystem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-space-s3filesystem-syntax.json"></a>

```
{
  "[S3Uri](#cfn-sagemaker-space-s3filesystem-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-space-s3filesystem-syntax.yaml"></a>

```
  [S3Uri](#cfn-sagemaker-space-s3filesystem-s3uri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-space-s3filesystem-properties"></a>

`S3Uri`  <a name="cfn-sagemaker-space-s3filesystem-s3uri"></a>
The Amazon S3 URI that specifies the location in S3 where files are stored, which is mounted within the Studio environment. For example: `s3://<bucket-name>/<prefix>/`.
*Required*: No
*Type*: String
*Pattern*: `(s3)://([^/]+)/?(.*)`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
