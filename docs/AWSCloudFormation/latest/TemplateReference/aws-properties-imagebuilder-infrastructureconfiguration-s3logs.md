---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-infrastructureconfiguration-s3logs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::InfrastructureConfiguration S3Logs
<a name="aws-properties-imagebuilder-infrastructureconfiguration-s3logs"></a>

Amazon S3 logging configuration.

## Syntax
<a name="aws-properties-imagebuilder-infrastructureconfiguration-s3logs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-infrastructureconfiguration-s3logs-syntax.json"></a>

```
{
  "[S3BucketName](#cfn-imagebuilder-infrastructureconfiguration-s3logs-s3bucketname)" : {{String}},
  "[S3KeyPrefix](#cfn-imagebuilder-infrastructureconfiguration-s3logs-s3keyprefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-infrastructureconfiguration-s3logs-syntax.yaml"></a>

```
  [S3BucketName](#cfn-imagebuilder-infrastructureconfiguration-s3logs-s3bucketname): {{String}}
  [S3KeyPrefix](#cfn-imagebuilder-infrastructureconfiguration-s3logs-s3keyprefix): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-infrastructureconfiguration-s3logs-properties"></a>

`S3BucketName`  <a name="cfn-imagebuilder-infrastructureconfiguration-s3logs-s3bucketname"></a>
The S3 bucket in which to store the logs.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3KeyPrefix`  <a name="cfn-imagebuilder-infrastructureconfiguration-s3logs-s3keyprefix"></a>
The Amazon S3 path to the bucket where the logs are stored.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
