---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-s3keyfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket S3KeyFilter
<a name="aws-properties-s3-bucket-s3keyfilter"></a>

A container for object key name prefix and suffix filtering rules. For more information about object key name filtering, see [Configuring event notifications using object key name filtering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-how-to-filtering.html) in the *Amazon S3 User Guide*.

**Note**
The same type of filter rule cannot be used more than once. For example, you cannot specify two prefix rules.

## Syntax
<a name="aws-properties-s3-bucket-s3keyfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-s3keyfilter-syntax.json"></a>

```
{
  "[Rules](#cfn-s3-bucket-s3keyfilter-rules)" : {{[ FilterRule, ... ]}}
}
```

### YAML
<a name="aws-properties-s3-bucket-s3keyfilter-syntax.yaml"></a>

```
  [Rules](#cfn-s3-bucket-s3keyfilter-rules): {{
    - FilterRule}}
```

## Properties
<a name="aws-properties-s3-bucket-s3keyfilter-properties"></a>

`Rules`  <a name="cfn-s3-bucket-s3keyfilter-rules"></a>
A list of containers for the key-value pair that defines the criteria for the filter rule.
*Required*: Yes
*Type*: Array of [FilterRule](aws-properties-s3-bucket-filterrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
