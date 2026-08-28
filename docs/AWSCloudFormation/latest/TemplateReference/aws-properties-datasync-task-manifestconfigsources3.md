---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-task-manifestconfigsources3.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::Task ManifestConfigSourceS3
<a name="aws-properties-datasync-task-manifestconfigsources3"></a>

<a name="aws-properties-datasync-task-manifestconfigsources3-description"></a>The `ManifestConfigSourceS3` property type specifies Property description not available. for an [AWS::DataSync::Task](aws-resource-datasync-task.md).

## Syntax
<a name="aws-properties-datasync-task-manifestconfigsources3-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-task-manifestconfigsources3-syntax.json"></a>

```
{
  "[BucketAccessRoleArn](#cfn-datasync-task-manifestconfigsources3-bucketaccessrolearn)" : {{String}},
  "[ManifestObjectPath](#cfn-datasync-task-manifestconfigsources3-manifestobjectpath)" : {{String}},
  "[ManifestObjectVersionId](#cfn-datasync-task-manifestconfigsources3-manifestobjectversionid)" : {{String}},
  "[S3BucketArn](#cfn-datasync-task-manifestconfigsources3-s3bucketarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-datasync-task-manifestconfigsources3-syntax.yaml"></a>

```
  [BucketAccessRoleArn](#cfn-datasync-task-manifestconfigsources3-bucketaccessrolearn): {{String}}
  [ManifestObjectPath](#cfn-datasync-task-manifestconfigsources3-manifestobjectpath): {{String}}
  [ManifestObjectVersionId](#cfn-datasync-task-manifestconfigsources3-manifestobjectversionid): {{String}}
  [S3BucketArn](#cfn-datasync-task-manifestconfigsources3-s3bucketarn): {{String}}
```

## Properties
<a name="aws-properties-datasync-task-manifestconfigsources3-properties"></a>

`BucketAccessRoleArn`  <a name="cfn-datasync-task-manifestconfigsources3-bucketaccessrolearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):iam::[0-9]{12}:role/.*$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManifestObjectPath`  <a name="cfn-datasync-task-manifestconfigsources3-manifestobjectpath"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}\p{C}]*$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManifestObjectVersionId`  <a name="cfn-datasync-task-manifestconfigsources3-manifestobjectversionid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^.+$`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3BucketArn`  <a name="cfn-datasync-task-manifestconfigsources3-s3bucketarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):(s3|s3-outposts):[a-z\-0-9]*:[0-9]*:.*$`
*Maximum*: `156`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
