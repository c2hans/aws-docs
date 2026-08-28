---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-domain-s3filesystemconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Domain S3FileSystemConfig
<a name="aws-properties-sagemaker-domain-s3filesystemconfig"></a>

Configuration for the custom Amazon S3 file system.

## Syntax
<a name="aws-properties-sagemaker-domain-s3filesystemconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-domain-s3filesystemconfig-syntax.json"></a>

```
{
  "[MountPath](#cfn-sagemaker-domain-s3filesystemconfig-mountpath)" : {{String}},
  "[S3Uri](#cfn-sagemaker-domain-s3filesystemconfig-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-domain-s3filesystemconfig-syntax.yaml"></a>

```
  [MountPath](#cfn-sagemaker-domain-s3filesystemconfig-mountpath): {{String}}
  [S3Uri](#cfn-sagemaker-domain-s3filesystemconfig-s3uri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-domain-s3filesystemconfig-properties"></a>

`MountPath`  <a name="cfn-sagemaker-domain-s3filesystemconfig-mountpath"></a>
The file system path where the Amazon S3 storage location will be mounted within the Amazon SageMaker Studio environment.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Uri`  <a name="cfn-sagemaker-domain-s3filesystemconfig-s3uri"></a>
The Amazon S3 URI of the S3 file system configuration.
*Required*: No
*Type*: String
*Pattern*: `(s3)://([^/]+)/?(.*)`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
