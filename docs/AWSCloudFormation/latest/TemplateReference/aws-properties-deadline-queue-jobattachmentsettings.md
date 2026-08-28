---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-queue-jobattachmentsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Queue JobAttachmentSettings
<a name="aws-properties-deadline-queue-jobattachmentsettings"></a>

The job attachment settings. These are the Amazon S3 bucket name and the Amazon S3 prefix.

## Syntax
<a name="aws-properties-deadline-queue-jobattachmentsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-queue-jobattachmentsettings-syntax.json"></a>

```
{
  "[RootPrefix](#cfn-deadline-queue-jobattachmentsettings-rootprefix)" : {{String}},
  "[S3BucketName](#cfn-deadline-queue-jobattachmentsettings-s3bucketname)" : {{String}}
}
```

### YAML
<a name="aws-properties-deadline-queue-jobattachmentsettings-syntax.yaml"></a>

```
  [RootPrefix](#cfn-deadline-queue-jobattachmentsettings-rootprefix): {{String}}
  [S3BucketName](#cfn-deadline-queue-jobattachmentsettings-s3bucketname): {{String}}
```

## Properties
<a name="aws-properties-deadline-queue-jobattachmentsettings-properties"></a>

`RootPrefix`  <a name="cfn-deadline-queue-jobattachmentsettings-rootprefix"></a>
The root prefix.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3BucketName`  <a name="cfn-deadline-queue-jobattachmentsettings-s3bucketname"></a>
The Amazon S3 bucket name.
*Required*: Yes
*Type*: String
*Pattern*: `(?!^(\d+\.)+\d+$)(^(([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])\.)*([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])$)`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
