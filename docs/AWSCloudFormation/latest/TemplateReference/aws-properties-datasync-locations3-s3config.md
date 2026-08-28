---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locations3-s3config.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationS3 S3Config
<a name="aws-properties-datasync-locations3-s3config"></a>

Specifies the Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that DataSync uses to access your S3 bucket.

For more information, see [Providing DataSync access to S3 buckets](https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#create-s3-location-access).

## Syntax
<a name="aws-properties-datasync-locations3-s3config-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-locations3-s3config-syntax.json"></a>

```
{
  "[BucketAccessRoleArn](#cfn-datasync-locations3-s3config-bucketaccessrolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-datasync-locations3-s3config-syntax.yaml"></a>

```
  [BucketAccessRoleArn](#cfn-datasync-locations3-s3config-bucketaccessrolearn): {{String}}
```

## Properties
<a name="aws-properties-datasync-locations3-s3config-properties"></a>

`BucketAccessRoleArn`  <a name="cfn-datasync-locations3-s3config-bucketaccessrolearn"></a>
Specifies the ARN of the IAM role that DataSync uses to access your S3 bucket.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):iam::[0-9]{12}:role/.*$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
