---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-s3contentbaselocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application S3ContentBaseLocation
<a name="aws-properties-kinesisanalyticsv2-application-s3contentbaselocation"></a>

The base location of the Amazon Data Analytics application.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-s3contentbaselocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-s3contentbaselocation-syntax.json"></a>

```
{
  "[BasePath](#cfn-kinesisanalyticsv2-application-s3contentbaselocation-basepath)" : {{String}},
  "[BucketARN](#cfn-kinesisanalyticsv2-application-s3contentbaselocation-bucketarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-s3contentbaselocation-syntax.yaml"></a>

```
  [BasePath](#cfn-kinesisanalyticsv2-application-s3contentbaselocation-basepath): {{String}}
  [BucketARN](#cfn-kinesisanalyticsv2-application-s3contentbaselocation-bucketarn): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-s3contentbaselocation-properties"></a>

`BasePath`  <a name="cfn-kinesisanalyticsv2-application-s3contentbaselocation-basepath"></a>
The base path for the S3 bucket.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9/!-_.*'()]+$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BucketARN`  <a name="cfn-kinesisanalyticsv2-application-s3contentbaselocation-bucketarn"></a>
The Amazon Resource Name (ARN) of the S3 bucket.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:.*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
