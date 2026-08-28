---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-s3logdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe S3LogDestination
<a name="aws-properties-pipes-pipe-s3logdestination"></a>

Represents the Amazon S3 logging configuration settings for the pipe.

## Syntax
<a name="aws-properties-pipes-pipe-s3logdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-s3logdestination-syntax.json"></a>

```
{
  "[BucketName](#cfn-pipes-pipe-s3logdestination-bucketname)" : {{String}},
  "[BucketOwner](#cfn-pipes-pipe-s3logdestination-bucketowner)" : {{String}},
  "[OutputFormat](#cfn-pipes-pipe-s3logdestination-outputformat)" : {{String}},
  "[Prefix](#cfn-pipes-pipe-s3logdestination-prefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-s3logdestination-syntax.yaml"></a>

```
  [BucketName](#cfn-pipes-pipe-s3logdestination-bucketname): {{String}}
  [BucketOwner](#cfn-pipes-pipe-s3logdestination-bucketowner): {{String}}
  [OutputFormat](#cfn-pipes-pipe-s3logdestination-outputformat): {{String}}
  [Prefix](#cfn-pipes-pipe-s3logdestination-prefix): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-s3logdestination-properties"></a>

`BucketName`  <a name="cfn-pipes-pipe-s3logdestination-bucketname"></a>
The name of the Amazon S3 bucket to which EventBridge delivers the log records for the pipe.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BucketOwner`  <a name="cfn-pipes-pipe-s3logdestination-bucketowner"></a>
The AWS account that owns the Amazon S3 bucket to which EventBridge delivers the log records for the pipe.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputFormat`  <a name="cfn-pipes-pipe-s3logdestination-outputformat"></a>
The format EventBridge uses for the log records.
EventBridge currently only supports `json` formatting.
*Required*: No
*Type*: String
*Allowed values*: `json | plain | w3c`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-pipes-pipe-s3logdestination-prefix"></a>
The prefix text with which to begin Amazon S3 log object names.
For more information, see [Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) in the *Amazon Simple Storage Service User Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
