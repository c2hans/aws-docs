---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3outposts-bucket-lifecycleconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Outposts::Bucket LifecycleConfiguration
<a name="aws-properties-s3outposts-bucket-lifecycleconfiguration"></a>

The container for the lifecycle configuration for the objects stored in an S3 on Outposts bucket.

## Syntax
<a name="aws-properties-s3outposts-bucket-lifecycleconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3outposts-bucket-lifecycleconfiguration-syntax.json"></a>

```
{
  "[Rules](#cfn-s3outposts-bucket-lifecycleconfiguration-rules)" : {{[ Rule, ... ]}}
}
```

### YAML
<a name="aws-properties-s3outposts-bucket-lifecycleconfiguration-syntax.yaml"></a>

```
  [Rules](#cfn-s3outposts-bucket-lifecycleconfiguration-rules): {{
    - Rule}}
```

## Properties
<a name="aws-properties-s3outposts-bucket-lifecycleconfiguration-properties"></a>

`Rules`  <a name="cfn-s3outposts-bucket-lifecycleconfiguration-rules"></a>
The container for the lifecycle configuration rules for the objects stored in the S3 on Outposts bucket.
*Required*: Yes
*Type*: Array of [Rule](aws-properties-s3outposts-bucket-rule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
